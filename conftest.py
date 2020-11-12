import pytest
import os

from logFile import logger
from config.globalVars import G
from utils.Others.TimeOperation import datetime_strftime
from Models.TestCase import Testcaseresult, saveCase


@pytest.fixture(scope='session', autouse=False)
def log():
    logs = logger.Logger("debug")
    yield logs


@pytest.fixture(scope="function", autouse=True)
def Init(request, log):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    filepath = request.node.nodeid
    G.now_case_startTime = datetime_strftime()
    logger.cmdOUT("TestCase: %s Start, Using Fixtures: %s " % (filepath, str(request.fixturenames)))
    logger.cmdOUT("UsingMarker: %s " % str(request.node.own_markers) + "\r")
    logger.cmdOUT("Start Setting UP " + "\r")
    yield log


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
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
            now_case.nodeid = str(report.nodeid)
            now_case.case_number = str(report.head_line)
            now_case.result = str(report.outcome)
            now_case.create_time = G.now_case_startTime
            G.now_case_startTime = None
            now_case.create_worker = G.OPERATION_WORKER
            now_case.taskname = G.TASK_NAME
            now_case.ending_time = datetime_strftime()
            now_case.ending_worker = G.OPERATION_WORKER
            now_case.marker = str(report.keywords)
            now_case.imgurl = None if not G.now_case_img_url else G.now_case_img_url
            now_case.logs = logs
            saveCase(now_case)
