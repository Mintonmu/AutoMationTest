import pytest
from utils.HTTPRequest.HttpRequest import httprequest


@pytest.mark.z_user_org_right
def test_111(log):
    request_api_url = "/z_user_org_right/LoginApi/getToken"
    request_data = {
        "name": "",
        "pwd": ""
    }
    request_method = "POST"
    res = httprequest(api_url = request_api_url,
                request_data = request_data,
                request_method = request_method)
    log.info(res)
    assert res[0] == 200

@pytest.mark.z_user_org_right
def test_Login_Api_Get_Token_GET(example_USER_fixture,Init):
    Init.info("这是测试一个用例")
    Init.info("测试USER fixture")
    sss = example_USER_fixture.Login_Api_Get_Token_GET()
    Init.info("本次测试状态码为 %s  " % sss[0])
    Init.info("本次测试返回值为 %s  " % sss[1])
    Init.info("本次测试响应头为 %s  " % sss[2])

