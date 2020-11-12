import os
import sys
import pytest

from Models import z_workflow

import logFile


@pytest.mark.z_workflow
def test_DataBase_TACTIVITYTEMPLATECopy1(DataBaseSession):
    data = {
        "function": sys._getframe().f_code.co_name,
        "filename": os.path.dirname(__file__)
    }

    try:

        oracle_instance = DataBaseSession
        query_result = oracle_instance.query(z_workflow.TACTIVITYTEMPLATECopy1)
        if query_result:
            for i in query_result:
                logFile.debug("确认%s表id为%s的数据的isvalid字段为1" % (i.__tablename__, i.id))
                try:
                    assert i.isvalid == 1
                except Exception as e:
                    error_data = "ERROR:    id 为%s 的数据 isvalid 为%s\r" % (i.id, i.isvalid)
                    logFile.error(error_data)
                    with open(os.path.join(os.path.dirname(__file__),
                                           "DataBaseError_%s_%s.txt" % (
                                           data["filename"].split("/")[-1], data["function"].split("_")[-1])),
                              'a+') as f:
                        f.write(error_data)
                logFile.debug("确认%s表id为%s的数据的bz1-bz4字段为空" % (i.__tablename__, i.id))
                try:
                    assert i.bz1 is None and i.bz2 is None and i.bz3 is None and i.bz4 is None
                except Exception as e:
                    error_data = "ERROR：    id 为%s 的数据 bz1-bz4 分别为bz1:%s  bz:%s  bz3:%s  bz4:%s\r" % (
                        i.id, i.bz1, i.bz2, i.bz3, i.bz4)
                    logFile.error(error_data)
                    with open(os.path.join(os.path.dirname(__file__),
                                           "DataBaseError_%s_%s.txt" % (
                                                   data["filename"].split("/")[-1], data["function"].split("_")[-1])),
                              'a+') as f:
                        f.write(error_data)
                logFile.debug("确认%s表id为%s的数据的创建时间创建人字段不为空" % (i.__tablename__, i.id))
                try:
                    assert i.create_time is not None and i.create_worker is not None
                except Exception as e:
                    error_data = "ERROR：    id 为%s 的数据 创建时间为%s /创建人为 %s \r" % (i.id, i.create_time, i.create_worker)
                    logFile.error(error_data)
                    with open(os.path.join(os.path.dirname(__file__),
                                           "DataBaseError_%s_%s.txt" % (
                                                   data["filename"].split("/")[-1], data["function"].split("_")[-1])),
                              'a+') as f:
                        f.write(error_data)
                logFile.debug("确认%s表id为%s的数据的最后修改时间最后修改人字段不为空" % (i.__tablename__, i.id))
                try:
                    assert i.latest_modify_worker is not None and i.latest_modify_time is not None
                except Exception as e:
                    error_data = "ERROR：    id 为%s 的数据最后修改时间为%s /最后修改时间人为%s \r" % (
                        i.id, i.latest_modify_time, i.latest_modify_worker)
                    logFile.error(error_data)
                    with open(os.path.join(os.path.dirname(__file__),
                                           "DataBaseError_%s_%s.txt" % (
                                                   data["filename"].split("/")[-1], data["function"].split("_")[-1])),
                              'a+') as f:
                        f.write(error_data)
    except Exception as e:
        pass
    finally:
        logFile.info("关闭数据库连接池")
        if oracle_instance:
            oracle_instance.__del__()


            oracle_instance.__del__()