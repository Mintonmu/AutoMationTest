
import pytest

from utils.UI.WebPage.LoginPlatform import CreateWorkFlow,LoginPlatform

"""API用例用例代码样本
    preInit为每个测试用例必须使用fixture,preInit  fixture自带log，可以使用该preInit.info preInit.debug preInit.error等打印消息
    
    
    
    
    禁止使用print打印，print函数本工程已屏蔽，打印消息无法显示
    
    
    
    
    其余fixture根据需求使用
"""



@pytest.mark.TestCase("[1]测试登录平台")
def test_loginPlatform(preInit, drivers):
    preInit.info("开始登录平台")
    A = LoginPlatform(driver=drivers)
    A.login()
    assert drivers.title == "HH"




@pytest.mark.TestCase("[1]测试创建工作流")
def test_createworkflow(preInit, drivers):
    preInit.info("开始登录平台")
    A = CreateWorkFlow(drivers)
    A.login()
    A.clickOpen()


