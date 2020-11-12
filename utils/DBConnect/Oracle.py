import sqlalchemy
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class DataBaseOperation(object):

    def __init__(self, configs):
        os.environ["NLS_LANG"] = "GERMAN_GERMANY.UTF8"  # 解决中文乱码
        config = None
        data_base_account = None
        for k, v in configs.items():
            config = v
            data_base_account = k
        data_base_ip = config.get("ip")
        data_base_listener_port = config.get("ListenerPort")
        data_base_instance_name = config.get('InstanceName')
        data_base_password = config.get("password")
        self.db_engine = None
        self.meta = None

        if data_base_ip and data_base_password and data_base_listener_port and data_base_instance_name and data_base_account and data_base_password:
            self.db_engine = sqlalchemy.create_engine('oracle+cx_oracle://%s:%s@%s:%s/%s' % (
                data_base_account, data_base_password, data_base_ip, data_base_listener_port, data_base_instance_name
            ), echo=True)
            session_maker = sessionmaker(bind=self.db_engine)
            self.session = session_maker()

    def query(self, table_name, filer=None, order=None):
        """

        :param table_name: 表名
        :param filer: 过滤器
        :param order: 排序
        :return: 符合条件的数据实例
        """
        data = None
        if filer:
            if order:
                data = self.session.query(table_name).filter_by(filer).order_by(order)
            else:
                data = self.session.query(table_name).filter_by(filer)
        else:
            if order:
                data = self.session.query(table_name).order_by(order)
            else:
                data = self.session.query(table_name)

        return data

    def insert(self, instance):
        """
        :param instance:ORM实例，通过query查询得到
        :return:
        """
        try:
            self.session.add(instance)
        except Exception as e :
            # 如果插入失败，则回退
            self.session.rollback()

    def delete(self,instance):
        """
        :param instance: 删除的ORM实例，通过query查询得到
        :return:
        """
        try:
            self.session.delete(instance)
        except Exception as e :
            # 删除实例失败，oracle回退
            self.session.rollback()

    def update(self, instance):
        """实例"""
        if hasattr(instance, 'id'):
            try:
                self.query(table_name=instance.__class__, filer=instance.id).update(values=instance.__dict__)
            except Exception as e:
                self.session.rollback()

    def __del__(self):
        #自动commit
        self.session.commit()
        #实例销毁时关闭Oracle连接池
        self.session.close()
        self.db_engine.dispose()


