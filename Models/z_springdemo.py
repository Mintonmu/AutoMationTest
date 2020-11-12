# coding: utf-8
from sqlalchemy import Column, DateTime, NVARCHAR, Table, VARCHAR
from sqlalchemy.dialects.oracle import NCLOB, NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


t_form = Table(
    'form', metadata,
    Column('id', VARCHAR(36), comment='ID'),
    Column('bool_field', NUMBER(1, 0, False), comment='bool类型，开关控件，男女选择'),
    Column('int_field', NUMBER(asdecimal=False), comment='int类型，下拉框value存储'),
    Column('string_field', NVARCHAR(256), comment='string类型，文本输入'),
    Column('date_field', DateTime, comment='日期类型，日期选择框'),
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
    Column('workflow_instance_id', VARCHAR(36), comment='WORKFLOW_INSTANCE_ID'),
    Column('activity_instance_id', VARCHAR(36), comment='ACTIVITY_INSTANCE_ID'),
    comment='表单Demo'
)


class SsoService(Base):
    __tablename__ = 'sso_service'
    __table_args__ = {'comment': '单点登录管理'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    system_name = Column(NVARCHAR(256), comment='系统名称')
    login_url = Column(NVARCHAR(256), comment='登录系统地址')
    logout_url = Column(NVARCHAR(256), comment='退出登录地址')
    token = Column(VARCHAR(256), comment='凭证密钥')
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
    i_enable = Column(NUMBER(asdecimal=False), comment='是否启用')


class TActivityTemplate(Base):
    __tablename__ = 't_activity_template'
    __table_args__ = {'comment': '活动模板表'}

    id = Column(VARCHAR(36), primary_key=True)
    index_code = Column(NUMBER(asdecimal=False), comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(VARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    flow_template_version_id = Column(VARCHAR(36), comment='流程模板版本表外键')
    name = Column(NVARCHAR(64), comment='活动名称')
    i_auto_transfer = Column(NUMBER(asdecimal=False), comment='转件时无需选人自动转走，1:是 0:否')
    i_archive_no_needed = Column(NUMBER(asdecimal=False), comment='未完成可归档 1-是  0-否')
    i_public_waiting_box = Column(NUMBER(asdecimal=False), comment='启用公共待办箱')
    i_limit_time = Column(NUMBER(asdecimal=False), comment='启用活动时限')
    time_limit = Column(NUMBER(asdecimal=False), comment='时限(单位是分，超过一天的分钟数，转换为天)')
    type = Column(NUMBER(asdecimal=False), comment='开始-10 结束-100 过程-20')
    i_work_day = Column(NUMBER(asdecimal=False), comment='是否工作日 1-是  0-否')
    activity_mark = Column(VARCHAR(64), comment='活动标识')
    mutex_logic = Column(NVARCHAR(1024), comment='后置活动前端转件互斥逻辑')
    mutex_logic_tip = Column(NVARCHAR(64), comment='不满足互斥条件的提示信息')


class TChildFlow(Base):
    __tablename__ = 't_child_flow'
    __table_args__ = {'comment': '子流程模板'}

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
    flow_template_id = Column(VARCHAR(36), comment='流程模板表外键')
    name = Column(NVARCHAR(32), comment='子流程显示名称')
    flow_template_version_id = Column(VARCHAR(36), comment='流程模板版本表外键\t')


class TDirectionTemplate(Base):
    __tablename__ = 't_direction_template'
    __table_args__ = {'comment': '流向模板表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    index_code = Column(NUMBER(asdecimal=False), comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(VARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    name = Column(NVARCHAR(64), comment='流向名')
    flow_template_version_id = Column(VARCHAR(36), comment='流程模板版本表外键')
    pre_node_name = Column(VARCHAR(64), comment='前置节点名称，可能是活动或网关或子流程')
    after_node_name = Column(VARCHAR(64), comment='后置节点名称，可能是活动或网关或子流程')
    i_auto_transfer = Column(NUMBER(asdecimal=False), comment='转件时无需选人自动转走，1:是 0:否')


class TFlowOpinion(Base):
    __tablename__ = 't_flow_opinion'
    __table_args__ = {'comment': '流程意见配置'}

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
    flow_template_version_id = Column(VARCHAR(36), comment='流程模板版本ID')
    opinion_name = Column(VARCHAR(64), comment='意见名称')
    opinion_user_text = Column(VARCHAR(64), comment='意见人文本')
    opinion_time_text = Column(VARCHAR(64), comment='意见时间文本')
    sign_type = Column(NUMBER(1, 0, False), comment='签名类型 1-数字签名 2-文本输入')
    activity_template_id = Column(VARCHAR(36), comment='活动模板ID')
    i_system_show = Column(NUMBER(asdecimal=False), comment='是否系统显示(1：是 0：否，非系统显示，需要业务端处理显示)')
    sort_mode = Column(NUMBER(asdecimal=False), comment='意见排序模式(1：以人员级别 0：以后台活动配置顺序)')
    i_hide_non_filled_comment = Column(NUMBER(asdecimal=False), comment='隐藏非本活动未填写意见(1：是 0：否)')
    i_show_my_opinion = Column(NUMBER(asdecimal=False), comment='单活动多意见只显示本人(1：是 0：否)')


class TFlowTemplateVDesign(Base):
    __tablename__ = 't_flow_template_v_design'
    __table_args__ = {'comment': '流程设计'}

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
    flow_template_v_design_id = Column(VARCHAR(36), comment='流程模板版本ID')
    design = Column(NCLOB, comment='设计器内容JSON格式')


class TFlowTemplateVersion(Base):
    __tablename__ = 't_flow_template_version'
    __table_args__ = {'comment': '流程模板版本表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    flow_template_id = Column(VARCHAR(36), comment='流程模板ID')
    flow_catalog_id = Column(VARCHAR(36), comment='流程目录ID')
    version_time = Column(DateTime, comment='版本时间')
    version_describe = Column(NVARCHAR(255), comment='版本描述')
    version_enable = Column(NUMBER(asdecimal=False), comment='版本是否启用')
    version_autoenable_time = Column(DateTime, comment='版本自动启用时间')
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
    code_template_id = Column(VARCHAR(36), comment='编码模板ID')
    inheritance_version_id = Column(VARCHAR(36), comment='继承版本ID')


class TFormRel(Base):
    __tablename__ = 't_form_rel'
    __table_args__ = {'comment': '表单关联表'}

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
    activity_template_id = Column(VARCHAR(36), comment='活动版本模板ID')


class TGatewayTemplate(Base):
    __tablename__ = 't_gateway_template'
    __table_args__ = {'comment': '网关模板表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    index_code = Column(NUMBER(asdecimal=False), comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(VARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    name = Column(NVARCHAR(64), comment='网关名')
    flow_template_version_id = Column(VARCHAR(36), comment='流程模板版本表外键')
    i_show_post_position = Column(NUMBER(asdecimal=False), comment='转件是否显示后置活动')
    transfer_judge = Column(NUMBER(asdecimal=False), comment='网关转出参与人判定 1-取所有参与人的并集 2-取所有参与人的交集 3-取最后一个前置活动指定的参与人 4-取第一个前置活动指定的参与人 5-指定某个活动/指定人的指定参与人\n')
