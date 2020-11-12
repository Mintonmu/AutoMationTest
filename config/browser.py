import os
import re
import subprocess
import zipfile

import requests
from bs4 import BeautifulSoup
from config.globalVars import G
from utils.Others.OSOperation import mk_dir
from logFile.logger import Logger
import selenium

log = Logger()


class Browser(object):

    @classmethod
    def set_browser(cls):
        # 检查Chrome版本号
        global version
        if "mac" in G.platform:
            # OS X
            result = subprocess.Popen([r'{}/Google\ Chrome --version'.format(G.chrome_app)],
                                      stdout=subprocess.PIPE, shell=True)
            version = [x.decode("utf-8") for x in result.stdout][0].strip().split(" ")[-1]
            log.warning("您的电脑为 %s 平台, 浏览器为 %s 版本号 %s " % (G.platform, G.browser, version))
        elif "win" in G.platform and G.browser == "CHROME":
            import winreg
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, G.chrome_reg)
                version = winreg.QueryValueEx(key, "version")[0]  # 查询注册表chrome版本号
            except Exception:
                raise Exception("查询注册表chrome版本失败!")
            log.warning("您的电脑为 %s 平台, 浏览器为 %s 版本号 %s " % (G.platform, G.browser, version))

        elif "win" in G.platform and G.browser == "IE":
            log.warning("您的电脑为 %s 平台，浏览器为 %s  ,%s 是不被完整支持的浏览器 " % (G.platform, G.browser, G.browser))
            version = selenium.__version__
        G.browser_ver = version
        file_vr = cls.search_ver(version)
        if file_vr is None:
            raise Exception("未获取到版本号! 请检查!")
        status, file = cls.check_driver(file_vr)
        if not status:
            log.warning("未查询到本地驱动")
            cls.gen_driver(file_vr)
        else:
            log.warning("系统已存在%sdriver, 无需下载!" % G.browser)
            G.DRIVER_PATH = os.path.join(G.web_driver_path, file)






    @classmethod
    def check_driver(cls, version):
        status, filename = False, None
        if os.path.exists(G.web_driver_path):
            pass
        else:
            mk_dir(G.web_driver_path)
        for root, dirs, files in os.walk(G.web_driver_path):
            for file in files:
                if version not in file:
                    try:
                        os.remove(os.path.join(root, file))
                    except Exception:
                        continue
                else:
                    status, filename = True, file

        return status, filename

    @classmethod
    def search_ver_v2(cls, version):
        ver = ".".join(version.split(".")[:2])
        r = requests.get(G.driver_url)
        bs = BeautifulSoup(r.text, features='html.parser')
        rt = [x for x in bs.select("pre a")]
        if not rt:
            raise Exception("可能淘宝镜像挂了，请重试")
        for x in rt:
            if x.text.startswith(ver):
                return x.text.rstrip("/")
        else:
            raise Exception("没有找到当前版本的合适驱动: {}".format(version))

    @classmethod
    def search_ver(cls, version):
        if version != "unknown":
            file_vr = None
            if G.browser == "CHROME":
                number = version.split(".")[0]

                url = G.driver_url + "LATEST_RELEASE"
                r = requests.get(url)
                bs = BeautifulSoup(r.text, 'html.parser')
                latest = bs.text.strip()
                record = "{}/{}/notes.txt".format(G.driver_url, latest)
                info = requests.get(record)
                text = info.text
                vr = re.findall(r"-+ChromeDriver\s+v(\d+\.+\d+)[\s|.|-|]+", text)
                br = re.findall(r"Supports\s+Chrome\s+v(\d+-\d+)", text)
                if not br:
                    return cls.search_ver_v2(version)
                for v, b in zip(vr, br):
                    small, bigger = b.split("-")
                    if int(small) <= int(number) <= int(bigger):
                        # 找到版本号
                        log.info("找到浏览器对应驱动版本号: {}".format(v))
                        file_vr = v
                        break
            elif G.browser == "IE" and G.platform =="windows":
                global req_version
                if version.endswith('0'):
                    req_version = version[:-2]

                url = G.ie_driver_url + req_version + "/"
                r = requests.get(url)
                bs = BeautifulSoup(r.text, 'lxml')
                url_list = bs.find_all(['a'])
                import platform
                posix = platform.architecture()
                log.warning("您的设备为%s%s" % posix)
                vr = "Win32_%s" % version
                v_l = []
                for i in url_list:
                    v_l.append(i.attrs['href'])
                if vr in str(v_l):
                    log.info("找到浏览器对应驱动版本号: {}".format(file_vr))
                    file_vr = vr
            return file_vr


    @classmethod
    def gen_driver(cls, file_vr):
        if file_vr:
            driver =None
            file = None
            r = None
            if G.browser == "CHROME":
                if G.platform == "mac":
                    file = "chromedriver_mac64.zip".format(file_vr)
                    driver = "chromedriver"
                elif "win" in G.platform:
                    file = "chromedriver_win32.zip".format(file_vr)
                    driver = "chromedriver.exe"
                else:
                    file = "chromedriver_linux64.zip".format(file_vr)
                    driver = "chromedriver"
                r = requests.get("{}{}/{}".format(G.driver_url, file_vr, file))
            elif G.browser == "IE":
                file = "IEDriverServer_{}.zip".format(file_vr)
                driver = "IEdriverServer.exe"
                r = requests.get("{}{}/IEDriverServer_{}.zip".format(G.ie_driver_url, req_version, file_vr))

            file_path = os.path.join(G.web_driver_path, file)
            print("开始下载!")
            with open(file_path, "wb") as f:
                f.write(r.content)
            cls.unzip_driver(file)
            cls.change_driver_name(file_vr, driver)

    @classmethod
    def unzip_driver(cls, filename):
        if G.platform == "mac":
            # 解压zip
            os.system('cd {};unzip {}'.format(G.web_driver_path, filename))
            os.path.join(G.web_driver_path, filename)
        elif "win" in G.platform:
            cls.unzip_win(os.path.join(G.web_driver_path, filename))
            os.remove(os.path.join(G.web_driver_path, filename))
        else:
            pass

    @classmethod
    def change_driver_name(cls, version, filename):
        if G.platform == "mac":
            new_file = "{}_{}".format(filename, version)
        elif G.platform == "windows":
            L = filename.split(".")
            new_file = "{}_{}.{}".format("".join(L[:-1]), version, L[-1])
        else:
            new_file = ""
        os.rename(os.path.join(G.web_driver_path, filename),
                  os.path.join(G.web_driver_path, new_file))
        G.DRIVER_PATH = os.path.join(G.web_driver_path, new_file)

    @classmethod
    def unzip_win(cls, filename):
        """unzip zip file"""
        with zipfile.ZipFile(filename) as f:
            for names in f.namelist():
                f.extract(names, G.web_driver_path)
