import pytest

from selenium import webdriver
from config.browser import Browser
from config.globalVars import G
from logFile.logger import Logger
from utils.HTTPRequest.HttpRequest import uploadFileToServer
from utils.Others.TimeOperation import datetime_strftime

log = Logger()
driver = None


@pytest.fixture(scope='session', autouse=False)
def drivers(request):
    """
    driver fixture ,UI相关用例使用，根据G变量中browser检测驱动，如果没有则自动下载，
    :param request:
    :return:
    """
    global driver
    if driver is None:
        Browser.set_browser()
        if G.browser == "CHROME":
            driver = webdriver.Chrome(executable_path=G.DRIVER_PATH)
        else:
            driver = webdriver.Ie(executable_path=G.DRIVER_PATH)
        driver.maximize_window()
    def fn():
        driver.quit()

    request.addfinalizer(fn)
    return driver


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """UI相关用例执行失败自动截图 """
    print('------------------------------------')
    # 获取钩子方法的调用结果
    out = yield
    print('用例执行结果', out)

    # 3. 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    if report.when == 'call' and report.outcome == "failed":
        path1 = str(report.nodeid)
        path2 = path1.split("::")[-1]
        png_path = G.report_path+"/%s_%s.png" % (datetime_strftime(),path2)
        _capture_screenshot(png_path)
        uploadFileToServer(png_path)







def _capture_screenshot(path):
    '''
    截图保存为png
    :return:
    '''
    return driver.get_screenshot_as_file(path)
