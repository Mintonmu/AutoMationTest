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
    # """
    # 当测试失败的时候，自动截图，展示到html报告中
    # :param item:
    # """
    # pytest_html = item.config.pluginmanager.getplugin('html')
    # outcome = yield
    # report = outcome.get_result()
    # extra = getattr(report, 'extra', [])
    #
    # if report.when == 'call' or report.when == "setup":
    #     xfail = hasattr(report, 'wasxfail')
    #     if (report.skipped and xfail) or (report.failed and not xfail):
    #         file_name = report.nodeid.replace("::", "_") + ".png"
    #         screen_img = _capture_screenshot()
    #         if file_name:
    #             html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:304px;height:228px;" ' \
    #                    'onclick="window.open(this.src)" align="right"/></div>' % screen_img
    #             extra.append(pytest_html.extras.html(html))
    #     report.extra = extra
    #     report.description = str(item.function.__doc__)
    #     report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")
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
    截图保存为base64
    :return:
    '''
    return driver.get_screenshot_as_file(path)
