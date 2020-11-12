
import pytest

from WebPage.LoginPlatform import CreateWorkFlow,LoginPlatform


@pytest.mark.z_user_org_right
def test_loginPlatform(drivers, Init):
    Init.info("开始登录平台")
    A = LoginPlatform(driver=drivers)
    A.login()
    assert drivers.title == "HH"




@pytest.mark.z_user_org_right
def test_createworkflow(drivers,  Init):
    Init.info("开始登录平台")
    A = CreateWorkFlow(drivers)
    A.login()
    A.clickOpen()


