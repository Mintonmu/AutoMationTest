
import pytest
from config.globalVars import G
from utils.DBConnect.Oracle import DataBaseOperation

@pytest.fixture()
def DataBaseSession(request):
    """ 数据库相关用例使用，返回已连接ORACLE SEssion """
    connection_data = G.data_base_config
    connect_data = {"Z_WORKFLOW":connection_data['Z_WORKFLOW']}
    DBsession = DataBaseOperation(connect_data)
    dbsession = DBsession.session

    def finalStep():
        """
        用例结束调用，关闭DBSession连接
        :return:
        """
        dbsession.close_all()

    request.addfinalizer(finalStep)
    return dbsession





