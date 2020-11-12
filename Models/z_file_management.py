# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, LargeBinary, NVARCHAR, Text, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Catalog(Base):
    __tablename__ = 'catalog'
    __table_args__ = {'comment': '?????'}

    id = Column(VARCHAR(36), primary_key=True, comment='??ID')
    parent_id = Column(VARCHAR(36), index=True, comment='????')
    catalog_name = Column(NVARCHAR(1024), index=True, comment='????')
    index_code = Column(Integer, index=True, comment='????')
    create_worker = Column(NVARCHAR(36), comment='???')
    create_time = Column(DateTime, comment='????')
    latest_modify_worker = Column(NVARCHAR(36), comment='?????')
    latest_modify_time = Column(DateTime, comment='??????')
    isvalid = Column(Integer, comment='????')
    bz1 = Column(NVARCHAR(255), comment='??1')
    bz2 = Column(NVARCHAR(255), comment='??2')
    bz3 = Column(NVARCHAR(255), comment='??3')
    bz4 = Column(NVARCHAR(255), comment='??4')


class FileChunk(Base):
    __tablename__ = 'file_chunk'
    __table_args__ = {'comment': '文件分片片数表'}

    id = Column(VARCHAR(36), primary_key=True, comment='文件分片片数表ID')
    chunks = Column(NUMBER(asdecimal=False), comment='总片数')
    index_code = Column(NUMBER(asdecimal=False), index=True, comment='排序编号')
    create_worker = Column(NVARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否合法')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    file_md5 = Column(NVARCHAR(36), comment='文件MD5值')


class FileContent(Base):
    __tablename__ = 'file_content'
    __table_args__ = {'comment': '文件内容表'}

    id = Column(VARCHAR(36), primary_key=True, comment='文件内容ID')
    file_chunk_id = Column(VARCHAR(36), comment='文件ID')
    content = Column(LargeBinary, comment='文件内容')
    chunk = Column(NUMBER(asdecimal=False), comment='当前分片')
    index_code = Column(NUMBER(asdecimal=False), index=True, comment='排序编号')
    create_worker = Column(NVARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否合法')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    originpath = Column(VARCHAR(255), comment='文件源路径')


class FileInfo(Base):
    __tablename__ = 'file_info'
    __table_args__ = {'comment': '文件信息表'}

    id = Column(VARCHAR(36), primary_key=True, comment='文件ID')
    file_name = Column(NVARCHAR(1024), index=True, comment='文件名称')
    file_suffix = Column(NVARCHAR(64), index=True, comment='文件后缀名')
    file_size = Column(NUMBER(asdecimal=False), comment='文件大小（单位为K）')
    upload_date = Column(DateTime, comment='上传日期')
    upload_login_name = Column(NVARCHAR(64), comment='上传人登陆名')
    upload_real_name = Column(NVARCHAR(64), comment='上传人姓名')
    index_code = Column(NUMBER(asdecimal=False), index=True, comment='排序编号')
    create_worker = Column(NVARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否合法')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    belong_catalog_id = Column(VARCHAR(36), index=True, comment='所属目录Id')
    file_initial_name = Column(NVARCHAR(1024), index=True, comment='文件初始名称')
    file_chunk_id = Column(VARCHAR(36), comment='分片片数表Id')


class FileRelCatalog(Base):
    __tablename__ = 'file_rel_catalog'
    __table_args__ = {'comment': '文件目录关联表'}

    id = Column(VARCHAR(36), primary_key=True, comment='文件目录关联ID')
    file_info_id = Column(VARCHAR(36), comment='文件ID')
    file_catalog_id = Column(VARCHAR(36), comment='目录ID')
    index_code = Column(NUMBER(asdecimal=False), index=True, comment='排序编号')
    create_worker = Column(NVARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime)
    isvalid = Column(NUMBER(asdecimal=False), comment='是否合法')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')


class KeyValue(Base):
    __tablename__ = 'key_value'
    __table_args__ = {'comment': '键值对配置'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    key = Column(NVARCHAR(64), comment='键')
    index_code = Column(NUMBER(asdecimal=False), comment='排序序号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(VARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否合法')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    value = Column(Text, comment='值')
