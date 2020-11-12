
import pytest
from config.globalVars import G
from utils.DBConnect.Oracle import DataBaseOperation

@pytest.fixture()
def DataBaseSession():
    connection_data = G.data_base_config
    connect_data = {"Z_WORKFLOW":connection_data['Z_WORKFLOW']}
    DBsession = DataBaseOperation(connect_data)
    yield DBsession


