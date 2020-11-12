# coding: utf-8
from sqlalchemy import Column, DateTime, LargeBinary, NVARCHAR, Table, VARCHAR
from sqlalchemy.dialects.oracle import NCLOB, NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Datasource(Base):
    __tablename__ = 'datasource'
    __table_args__ = {'comment': '数据源管理'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    index_code = Column(NUMBER(asdecimal=False), comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    system_id = Column(VARCHAR(36), comment='系统ID')
    name = Column(NVARCHAR(64), comment='数据源名称')
    bz = Column(NVARCHAR(2000), comment='备注')
    data = Column(NCLOB, comment='JSON数据/SQL语句/服务地址')
    type = Column(NUMBER(1, 0, False), comment='数据源类型 1-固定 2-SQL 3-服务')
    db_connect_id = Column(VARCHAR(36), comment='SQL类型数据库ID')
    from_id = Column(VARCHAR(36), comment='表单ID')
    ds_level = Column(NUMBER(1, 0, False), comment='数据源级别 1-公共级 2-页面级')


class DbConnect(Base):
    __tablename__ = 'db_connect'
    __table_args__ = {'comment': '数据库连接管理'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    index_code = Column(NUMBER(asdecimal=False), comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    db_name = Column(NVARCHAR(64), comment='数据库名称')
    db_type = Column(NVARCHAR(64), comment='数据库类型--直接写数据库类型名称即可')
    ip = Column(NVARCHAR(36), comment='IP地址')
    user_name = Column(NVARCHAR(36), comment='用户名')
    port = Column(NVARCHAR(8), comment='端口')
    bz = Column(NVARCHAR(2000), comment='备注')
    role_type = Column(NVARCHAR(64), comment='角色类型')
    pwd = Column(NVARCHAR(36), comment='密码(明文)')
    instance_name = Column(NVARCHAR(64), comment='实例名称')


class FilialeManage(Base):
    __tablename__ = 'filiale_manage'
    __table_args__ = {'comment': 'MIS表管理系统-分支机构管理'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    filiale_name = Column(VARCHAR(255), comment='分支机构名称')
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
    bz = Column(VARCHAR(255), comment='备注')


class Form(Base):
    __tablename__ = 'form'
    __table_args__ = {'comment': '条件/事件关联'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    index_code = Column(NUMBER(asdecimal=False), comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    name = Column(NVARCHAR(36), comment='名称')
    form_catalog_id = Column(VARCHAR(36), comment='表单目录外键ID')
    show_name = Column(NVARCHAR(64), comment='表单显示名称')
    source = Column(NUMBER(asdecimal=False), comment='来源 1-自定义表单 2-外部系统')
    pc_url = Column(NVARCHAR(1024), comment='PC端地址')
    mobile_url = Column(NVARCHAR(1024), comment='移动端地址')
    title = Column(NVARCHAR(256), comment='表单标题')


class FormCatalog(Base):
    __tablename__ = 'form_catalog'
    __table_args__ = {'comment': '表单目录树表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    index_code = Column(NUMBER(asdecimal=False), comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    parent_id = Column(VARCHAR(36), comment='父级主键')
    name = Column(NVARCHAR(64), comment='表单目录名称')


class FormDomPromisstion(Base):
    __tablename__ = 'form_dom_promisstion'
    __table_args__ = {'comment': '表单按钮权限'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    index_code = Column(NUMBER(asdecimal=False), comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    form_id = Column(VARCHAR(36), comment='表单外键ID')
    name = Column(NVARCHAR(64), comment='DOM的name')
    bz = Column(NVARCHAR(256), comment='元素备注')
    validate_expression = Column(NVARCHAR(64), comment='验证表达式')
    edit_i_hidden = Column(NUMBER(asdecimal=False), comment='编辑模式是否隐藏 1-是 0-否')
    edit_i_readonly = Column(NUMBER(asdecimal=False), comment='编辑模式是否只读 1-是 0-否')
    edit_i_required = Column(NUMBER(asdecimal=False), comment='编辑模式是否必填 1-是 0-否')
    view_i_hidden = Column(NUMBER(asdecimal=False), comment='查看模式是否隐藏 1-是 0-否')
    view_i_writable = Column(NUMBER(asdecimal=False), comment='查看模式是否可写 1-是 0-否')


class FormRelReport(Base):
    __tablename__ = 'form_rel_report'
    __table_args__ = {'comment': '表单报表关联表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    index_code = Column(NUMBER(asdecimal=False), comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    from_id = Column(VARCHAR(36), comment='表单ID')
    report_id = Column(VARCHAR(36), comment='报表ID，在业务通用模块系统')


class FromContent(Base):
    __tablename__ = 'from_content'
    __table_args__ = {'comment': '表单设计器'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    index_code = Column(NUMBER(asdecimal=False), comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    form_id = Column(VARCHAR(36), comment='表单ID')
    layout_content = Column(LargeBinary, comment='布局内容')
    plug_content = Column(LargeBinary, comment='插件内容')
    ftl_content = Column(LargeBinary, comment='FTL内容')


t_sys_config_childs = Table(
    'sys_config_childs', metadata,
    Column('id', VARCHAR(36), nullable=False, comment='主键'),
    Column('index_code', NUMBER(asdecimal=False), comment='排序编号'),
    Column('create_worker', VARCHAR(36), comment='创建人'),
    Column('create_time', DateTime, comment='创建时间'),
    Column('latest_modify_worker', NVARCHAR(36), comment='最后修改人'),
    Column('latest_modify_time', DateTime, comment='最后修改时间'),
    Column('isvalid', NUMBER(asdecimal=False), comment='是否启用'),
    Column('bz1', NVARCHAR(255), comment='备注1'),
    Column('bz2', NVARCHAR(255), comment='备注2'),
    Column('bz3', NVARCHAR(255), comment='备注3'),
    Column('bz4', NVARCHAR(255), comment='备注4'),
    Column('value', NVARCHAR(128), comment='值'),
    Column('system_id', VARCHAR(36), comment='所属系统ID'),
    Column('name', NVARCHAR(64), comment='名称'),
    Column('bz', NVARCHAR(2000), comment='备注'),
    comment='系统配置'
)


class SysConfigFather(Base):
    __tablename__ = 'sys_config_father'
    __table_args__ = {'comment': '系统配置'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    index_code = Column(NUMBER(asdecimal=False), comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    name = Column(NVARCHAR(64), comment='名称')
    bz = Column(NVARCHAR(2000), comment='备注')
    value = Column(NVARCHAR(128), comment='值')


class SystemManage(Base):
    __tablename__ = 'system_manage'
    __table_args__ = {'comment': 'MIS表管理系统-系统管理'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    system_name = Column(VARCHAR(64), comment='系统名称')
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
    bz = Column(VARCHAR(255), comment='备注')
    mark_value = Column(NVARCHAR(255), comment='标识')
    db_type = Column(NUMBER(1, 0, False), comment='数据库类型 1-Oracle 2-Mysql ...')
    db_ip = Column(NVARCHAR(16), comment='数据库IP地址')
    db_user_name = Column(NVARCHAR(32), comment='数据库用户名')
    db_port = Column(NVARCHAR(8), comment='数据库端口')
    db_pwd = Column(NVARCHAR(32), comment='数据库密码')
    db_role_type = Column(NVARCHAR(16), comment='数据库角色类型')
    system_ip = Column(NVARCHAR(16), comment='系统IP')
    system_port = Column(NVARCHAR(8), comment='系统端口')
