import pytest
import os
import sys

from logFile import logger
from config.globalVars import G
from utils.Others.TimeOperation import datetime_strftime
from Models.TestCase import Testcaseresult, saveCase

"""
总工程的conftest为pytest工程共享配置，每个测试函数均可调用，
各个测试模块文件夹中定义的fixture仅仅该文件夹下的代码可以调用
fixture可以实现各种初始化，后置处理

"""


def pytest_runtest_setup(item):
    for mark in item.iter_markers(name="TestCase"):
        print("TestCase args={} kwargs={}".format(mark.args, mark.kwargs))
        sys.stdout.flush()

@pytest.fixture(scope='session', autouse=False)
def log():
    """ log fixture 打印消息"""
    logs = logger.Logger("debug")
    yield logs


@pytest.fixture(scope="function", autouse=True)
def preInit(request, log):
    """初始化fixture 返回log对象
    fixture可以调用其他fixture

    """
    log.info("Start Setting UP " + "\r")
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    filepath = request.node.nodeid
    G.now_case_startTime = datetime_strftime()
    log.info("TestCase: %s Start, Using Fixtures: %s " % (filepath, str(request.fixturenames)))
    G.now_case_level = request.node.own_markers[0].args[0].split("]")[0][1]
    G.now_case_name = request.node.own_markers[0].args[0].split("]")[1]
    G.now_case_number = request.node.name
    log.info("UsingMarker: %s CaseLevel: Level %s CaseName:%s" % (request.node.own_markers[0].name, G.now_case_level, G.now_case_name ) + "\r")

    yield log


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """"
    pytest后置处理fixture，无需调用，用例结束自动调用

    不能修改 该fixture负责生成日志，上传记录等。


    """
    print('------------------------------------')
    out = yield
    report = out.get_result()
    if report.when == 'call':
        logpath = os.path.join(G.log_path, "%s_%s.log" % (datetime_strftime(), report.head_line))
        logs = ''
        with open(logpath, "a+") as  f:
            f.write("当前节点: %s " % report.nodeid + "\r")
            logs += "当前节点: %s " % report.nodeid + "\r"
            f.write("TestCaseName: %s   Result: %s   Duration: %sS " % (
                report.head_line, report.outcome, report.duration) + "\r")
            logs += "TestCaseName: %s   Result: %s   Duration: %sS " % (
                report.head_line, report.outcome, report.duration) + "\r"
            for i in report.sections:
                for j in i:
                    if "Captured" in j:
                        f.write("-" * 20 + j + "-" * 20 + "\r")
                        logs += "-" * 20 + j + "-" * 20 + "\r"
                    else:
                        f.write(j + "\r")
                        logs += j + "\r"
                if report.longreprtext:
                    f.write(report.longreprtext + "\r")
                    logs += report.longreprtext + "\r"
        if G.TASK_NAME != "Local":
            # TASK_NAME 为Local时不会上传测试记录，但会在本地留下日志信息
            now_case = Testcaseresult()
            now_case.case_number = G.now_case_number
            now_case.case_name = G.now_case_name
            now_case.Level = G.now_case_level
            now_case.result = str(report.outcome)
            now_case.create_time = G.now_case_startTime
            now_case.create_worker = G.OPERATION_WORKER
            now_case.taskname = G.TASK_NAME
            now_case.ending_time = datetime_strftime()
            now_case.ending_worker = G.OPERATION_WORKER
            now_case.marker = str(report.keywords)
            now_case.imgurl = None if not G.now_case_img_url else G.now_case_img_url
            now_case.logs = logs
            saveCase(now_case)