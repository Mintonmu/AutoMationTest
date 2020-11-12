import os
import sys
from selenium.webdriver.common.by import By


class GlobalVars(object):
    OPERATION_WORKER = "PYTHON AUTOMATION TEST"
    TASK_NAME = "DAILY" # TASK_NAME为Local不会上传测试结果至数据库，["DAILY","LOCAL","Task_name"]
    now_case_img_url = None
    now_case_startTime = None
    # API 服务器IP
    Server_IP = ""
    Server_Port = 80
    UploadFileAPI = "/FileInfoApi/uploadFileByOtherSystem"
    # API 测试验证ticket，当前api无验证，采用ticket，如后续api增加验证，则填入Server_Checking_Username与password
    Server_Checking_ticket = {"zjugis.api.ticket": (None, "wwkj&key&zdww1402")}
    Server_Checking_Username = ""
    Server_Checking_password = ""

    # 工程路径相关
    root = os.path.dirname(__file__)
    suite_dir = os.path.join(root, "TestCase")
    skip_suite = None
    project_root = os.path.dirname(root)
    report_path = os.path.join(project_root, 'report')
    log_path = os.path.join(project_root, 'log')
    # 数据库配置，与服务器保持一致，默认根据Server_IP连接，使用ORM映射获得数据
    data_base_config = {
        'Z_AUTO_DEPLOY':
            {'ip': 'ip', 'ListenerPort': 1521, 'password': '',
             'InstanceName': ''},
        'Z_USER_ORG_RIGHT':
            {'ip': '', 'ListenerPort': 1521, 'password': '',
             'InstanceName': ''},
        'Z_BUSSINESS_COMMOM':
            {'ip': '', 'ListenerPort': 1521, 'password': '',
             'InstanceName': ''},
        'Z_FILE_MANAGEMENT':
            {'ip': '', 'ListenerPort': 1521, 'password': '',
             'InstanceName': ''},
        'Z_MIDDLEWARE_MQ':
            {'ip': '', 'ListenerPort': 1521, 'password': '',
             'InstanceName': ''},
        'Z_SPRING_DEMO':
            {'ip': '', 'ListenerPort': 1521, 'password': '',
             'InstanceName': 'develop'},
        'Z_WORKFLOW':
            {'ip': '1', 'ListenerPort': 1521, 'password': '',
             'InstanceName': ''},
        'Z_WEB_CONTAINER':
            {'ip': '', 'ListenerPort': 1521, 'password': '',
             'InstanceName': ''}}

    """
    
    
    
    UI相关
    请勿修改
    
    
    
    """
    SYSUsername = ""
    SYSPassword = ""
    # selenium UI测试重试次数
    RETRY = 3
    # 等待时间，如果超过该时间浏览器未返回数据，自动停止测试
    TIME_OUT = 1
    # selenium驱动存放地址
    resource_path = os.path.join(project_root, "resource")
    web_driver_path = os.path.join(resource_path, "webdriver")
    ELEMENT_PATH = os.path.join(os.path.dirname(web_driver_path), "PageElement")
    # 默认为CHROME， IE后续可能会适配，但是IE适配难度较高，暂时不考虑
    browser = "CHROME"
    # CHROME版本，自动采集
    browser_version = None
    # selenium 驱动包TaoBao 镜像站
    ie_driver_url = "https://npm.taobao.org/mirrors/selenium/"
    driver_url = "https://npm.taobao.org/mirrors/chromedriver/"
    # 当前电脑平台，默认为mac，非mac设备运行时会自动改为windows或者linux(linux不适配，需考虑排除无界面设备）
    platform = "mac"  # 默认为mac
    kernel = sys.platform
    if "darwin" in kernel:
        # MAC os
        chrome_app = r"/Applications/Google\ Chrome.app/Contents/MacOS/"  # mac os chrome安装地址
    elif "win" in kernel:
        platform = "windows"
        # Win
        chrome_reg = r"SOFTWARE\Google\Chrome\BLBeacon"  # win chrome注册表地址
        instant_client = os.path.join(resource_path, "instant_client")
    else:
        platform = "linux"
        browser = "firefox"
    # 根据后续自动安装驱动返回
    DRIVER_PATH = None
    # 定位元素语法
    LOCATE_MODE = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'id': By.ID,
        'class': By.CLASS_NAME,
        "fulltext": By.LINK_TEXT,
        "parttext": By.PARTIAL_LINK_TEXT
    }


G = GlobalVars()
