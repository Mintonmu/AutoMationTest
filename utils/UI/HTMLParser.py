import os
from utils.HTTPRequest.HttpRequest import httprequest
from bs4 import BeautifulSoup
from config.globalVars import G
import yaml
from selenium import webdriver
from WebPage.BasePage import WebPage
from utils.UI.read_element import Element

class Parser(object):

    def __init__(self, ip_or_dns, api_url,port=82):
        self.port = port
        self.ip = ip_or_dns
        self.api_url = api_url
        self.roots = os.path.dirname(__file__)
        self.resource_root = os.path.join(os.path.join(os.path.dirname(os.path.dirname(self.roots)), "resource"), "PageElement")
        self.run()

    def run(self):
        self.parse()

    def getHTML(self):
        request_data = None
        req = httprequest(request_method="GET", request_data=request_data, port=self.port, api_url=self.api_url)
        htmls = req[1]
        if htmls:
            return htmls
        else:
            raise ArithmeticError("none")

    def filefatch(self):
        filename = "".join(self.api_url.split("/"))+".yaml"
        fileList = os.listdir(G.ELEMENT_PATH)
        if  filename in fileList:
            os.remove(G.ELEMENT_PATH+"/"+ filename)
        yamlpath = os.path.join(G.ELEMENT_PATH, filename)
        return yamlpath

    def dumpyaml(self,desired_caps, filename):
        with open(filename, "w", encoding="utf-8") as f:
            yaml.dump(desired_caps, f,)

    def parse(self):
        html= self.getHTML()
        soup = BeautifulSoup(html, 'lxml')
        # print(soup)
        print(type(soup))
        print(soup.prettify())
        path = self.filefatch()
        li = soup.find_all(["input","div"])
        desired_caps = dict()
        for i in li:
            if len(i.attrs) > 1 :
                if "name" in i.attrs:
                    desired_caps[i.attrs['name']]="name=%s" % i.attrs['name']
        self.dumpyaml(desired_caps=desired_caps, filename=path)

"""爬取页面上的定位元素"""

class SeleniumParser(object):

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=G.DRIVER_PATH)
        self.basePage = WebPage(driver=self.driver)

    def read_login_config(self):
        self.configs = Element('z_user_org_rightLoginindex')

    def login(self):
        self.basePage.get_url("http://114.215.200.79:81/z_user_org_right/Login/index")
        self.html = self.basePage.get_source()
        self.basePage.input_text(self.configs["userName"],"Admin")
        self.basePage.input_text(self.configs["userPwd"],"zjugis1402!")
        self.basePage.is_click(self.configs["btnLogin"])


    def get_page_source(self,url):
        self.basePage.get_url(url)
        self.html = self.basePage.page_source


    def filefatch(self,url):
        filename = "".join(url.split("/")[3:]) + ".yaml"
        fileList = os.listdir(G.ELEMENT_PATH)
        if filename in fileList:
            os.remove(G.ELEMENT_PATH + "/" + filename)
        yamlpath = os.path.join(G.ELEMENT_PATH, filename)
        return yamlpath

    def dumpyaml(self,desired_caps, filename):
        with open(filename, "w", encoding="utf-8") as f:
            yaml.dump(desired_caps, f,)

    def parse(self):
        soup = BeautifulSoup(self.basePage.get_source(), 'lxml')
        print(soup.prettify())
        path = self.filefatch(self.driver.current_url)
        li = soup.find_all(["input", "div"])
        desired_caps = dict()
        for i in li:
            if len(i.attrs) :
                if "name" in i.attrs:
                    desired_caps[i.attrs['name']] = "name=%s" % i.attrs['name']
                elif "class" in i.attrs:
                        pass

        self.dumpyaml(desired_caps=desired_caps, filename=path)

test = SeleniumParser()
test.read_login_config()
test.login()
test.parse()
