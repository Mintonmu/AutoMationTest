from sqlalchemy import Column, DateTime, VARCHAR, NCHAR, Integer, create_engine, CLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
metadata = Base.metadata


class Testcaseresult(Base):
    __tablename__ = 'testcaseresult'
    __table_args__ = {'comment': '测试数据管理'}

    id = Column(Integer, primary_key=True, comment='主键')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(VARCHAR(36), comment='创建时间')
    ending_worker = Column(VARCHAR(36), comment='最后修改人')
    ending_time = Column(VARCHAR(36), comment='最后修改时间')
    logs = Column(CLOB(10000), comment='测试日志')
    result = Column(NCHAR(200), comment='测试结果')
    case_name = Column(NCHAR(200), comment='用例名')
    case_number = Column(NCHAR(200), comment='用例编号')
    marker = Column(NCHAR(200), comment='用例模块(Marker)')
    nodeid = Column(NCHAR(400), comment='用例节点')
    imgurl = Column(NCHAR(400), comment='截图')
    taskname = Column(NCHAR(400), comment='任务名')

engine = create_engine("oracle+cx_oracle://username:password@ip:port/instance_name",
                                    max_overflow = 5) #创建引擎


def init_db(): #初始化表
    Base.metadata.create_all(bind=engine)

def getModel():
    cmd = r"""sqlacodegen oracle+cx_oracle://username:password@ip:port/instance_name --outfile filename.py"""


def saveCase(instance):
    Session_class = sessionmaker(bind=engine)
    Session = Session_class()
    try:
        Session.add(instance)
    except Exception as e:
        Session.rollback()
    Session.commit()
    Session.close_all()
