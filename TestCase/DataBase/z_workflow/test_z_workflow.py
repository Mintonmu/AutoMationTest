import os
import sys
import pytest
from sqlalchemy import or_

from Models import z_workflow

"""API用例用例代码样本
    preInit为每个测试用例必须使用fixture,preInit  fixture自带log，可以使用该preInit.info preInit.debug preInit.error等打印消息




    禁止使用print打印，print函数本工程已屏蔽，打印消息无法显示




    其余fixture根据需求使用
"""



@pytest.mark.TestCase("[1]测试数据库")
def test_DataBase_TACTIVITYTEMPLATE(preInit, DataBaseSession):
    data = {
        "function": sys._getframe().f_code.co_name,
        "filename": os.path.dirname(__file__)
    }
    dbsession = DataBaseSession
    try:


        queryset = dbsession.query(z_workflow.TActivityTemplate).filter(or_(z_workflow.TActivityTemplate.bz1 != None , z_workflow.TActivityTemplate.bz1 != None,
                                                                         z_workflow.TActivityTemplate.bz3 != None , z_workflow.TActivityTemplate.bz4 != None ,
                                                                         z_workflow.TActivityTemplate.isvalid != 1)
                                                                         )

        if queryset:
            with open(os.path.join(os.path.dirname(__file__),
                                   "DataBaseError_%s_%s.txt" % (
                                           data["filename"].split("/")[-1], data["function"].split("_")[-1])),
                      'a+') as f:
                for i in queryset:
                    if i.bz1 != None or i.bz2 !=None or i.bz3 != None or i.bz4 != None:
                        error_data = "ERROR：    id 为%s 的数据 bz1-bz4 分别为bz1:%s  bz:%s  bz3:%s  bz4:%s\r" % (
                            i.id, i.bz1, i.bz2, i.bz3, i.bz4)
                        f.write(error_data)
                        preInit.error(error_data)
                    if i.isvalid != 1 :
                        error_data = "ERROR:    id 为%s 的数据 isvalid 为%s\r" % (i.id, i.isvalid)
                        preInit.error(error_data)
                        f.write(error_data)
                    if i.create_time == None or i.create_worker == None:
                        error_data = "ERROR：    id 为%s 的数据 创建时间为%s /创建人为 %s \r" % (i.id, i.create_time, i.create_worker)
                        preInit.error(error_data)
                        f.write(error_data)
        else:
            preInit.info("未查询到本数据库有违规数据")
    except Exception as e :
        dbsession.rollback()




