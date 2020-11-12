import pytest
from config.globalVars import G
from utils.HTTPRequest.RequestBase import ZUserOrgRight



@pytest.fixture(scope="function")
def example_USER_fixture():
    USER_FIXTURE = ZUserOrgRight(pattern="/z_user_org_right")
    yield USER_FIXTURE




