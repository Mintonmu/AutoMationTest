import pytest


"""API用例用例代码样本
    preInit为每个测试用例必须使用fixture,preInit  fixture自带log，可以使用该preInit.info preInit.debug preInit.error等打印消息
    
    
    
    
    禁止使用print打印，print函数本工程已屏蔽，打印消息无法显示
    
    
    
    
    其余fixture根据需求使用
"""

@pytest.mark.TestCase("[1]测试获取登录API验证是否正常")
def test_Login_Api_Get_Token_GET(preInit, example_USER_fixture):
    preInit.info("这是测试一个用例")
    preInit.info("测试USER fixture")
    sss = example_USER_fixture.Login_Api_Get_Token_GET()
    preInit.info("本次测试状态码为 %s  " % sss[0])
    preInit.info("本次测试返回值为 %s  " % sss[1])
    preInit.info("本次测试响应头为 %s  " % sss[2])

