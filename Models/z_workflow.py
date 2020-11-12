# coding: utf-8
from sqlalchemy import Column, DateTime, Index, Integer, NVARCHAR, Table, Text, VARCHAR
from sqlalchemy.dialects.oracle import NCLOB, NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TACTIVITYTEMPLATECopy1(Base):
    __tablename__ = 'T_ACTIVITY_TEMPLATE_copy1'
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


class ActivityRelOpinion(Base):
    __tablename__ = 'activity_rel_opinion'
    __table_args__ = {'comment': '活动与意见模板关系表'}

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
    activity_template_id = Column(VARCHAR(36), comment='活动模板ID')
    opinion_template_id = Column(VARCHAR(36), comment='意见模板ID')
    flow_template_version_id = Column(VARCHAR(36), comment='流程模板版本ID')


class IActiInsRelForm(Base):
    __tablename__ = 'i_acti_ins_rel_form'
    __table_args__ = {'comment': '活动实例表单关联表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    index_code = Column(Integer, comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(Integer, comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    flow_instance_id = Column(VARCHAR(36), comment='流程实例id')
    activity_instance_id = Column(VARCHAR(36), index=True, comment='活动实例id')
    form_id = Column(VARCHAR(36), comment='表单id')
    form_name = Column(NVARCHAR(255), comment='表单名称')
    form_url = Column(NVARCHAR(255), comment='表单地址')
    form_title = Column(NVARCHAR(256), comment='表单标题')
    form_mobile_url = Column(NVARCHAR(255), comment='表单地址（移动端）')


class IActivityInsParticipant(Base):
    __tablename__ = 'i_activity_ins_participant'
    __table_args__ = (
        Index('idx_aip_authority_finish_time', 'handle_authority', 'finish_time', 'activity_instance_id'),
        {'comment': '活动参与人实例'}
    )

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
    activity_instance_id = Column(VARCHAR(36), index=True, comment='活动实例ID')
    activity_template_id = Column(VARCHAR(36), comment='活动模板ID')
    user_id = Column(VARCHAR(36), index=True, comment='参与人ID')
    receive_time = Column(DateTime, comment='接件时间')
    finish_time = Column(DateTime, comment='完成时间')
    i_end = Column(NUMBER(1, 0, False), comment='是否归档')
    lead_participant_id = Column(VARCHAR(36), comment='前置参与人ID')
    wait_opinion_temp_id = Column(VARCHAR(36), comment='立等可取意见模板ID')
    handle_authority = Column(NUMBER(1, 0, False), comment='办理权限（0：办理  1：隐藏  2：查看）')


class IActivityInstance(Base):
    __tablename__ = 'i_activity_instance'
    __table_args__ = (
        Index('ai_flow_id_index', 'flow_instance_id', 'id'),
        {'comment': '活动实例'}
    )

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
    flow_instance_id = Column(VARCHAR(36), comment='流程实例ID')
    activity_template_id = Column(VARCHAR(36), comment='活动模板ID')
    start_time = Column(DateTime, comment='活动开始时间')
    end_time = Column(DateTime, comment='活动结束时间（实际完成时间）')
    should_finish_time = Column(DateTime, comment='活动应该完成时间，没有时限则存null')
    status = Column(NUMBER(asdecimal=False), index=True, comment='1-正常 20-已挂起  90-已完成 40-退件')
    i_end = Column(NUMBER(1, 0, False), comment='是否归档')
    i_public = Column(NUMBER(asdecimal=False), comment='是否在公共待办箱 1-是 0-否')
    name = Column(NVARCHAR(64), comment='活动名称')
    external_activity_id = Column(VARCHAR(36), comment='外部活动实例ID')
    i_external = Column(NUMBER(1, 0, False), comment='是否是外部活动 1是 0否')
    external_flow_instance_id = Column(VARCHAR(36), comment='外部流程实例ID')
    time_limit = Column(Integer, comment='时限(单位：分)')
    i_work_day = Column(Integer, comment='是否工作日 1-是  0-否')


class IAttentionInstance(Base):
    __tablename__ = 'i_attention_instance'
    __table_args__ = (
        Index('attention_uid_fid', 'attention_user_id', 'flow_instance_id'),
        {'comment': '关注实例'}
    )

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
    attention_user_id = Column(VARCHAR(36), comment='关注人ID')
    flow_instance_id = Column(VARCHAR(36), comment='流程实例ID')
    attention_time = Column(DateTime, comment='关注时间')
    i_readed = Column(NUMBER(1, 0, False), comment='是否已读 1|0')


class ICarboncopyInstance(Base):
    __tablename__ = 'i_carboncopy_instance'
    __table_args__ = {'comment': '抄送实例'}

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
    carboncopy_user_id = Column(VARCHAR(36), comment='抄送人')
    flow_instance_id = Column(VARCHAR(36), comment='流程实例ID')
    carboncopy_time = Column(DateTime, comment='抄送时间')
    receive_user_id = Column(VARCHAR(36), index=True, comment='接收人')
    i_readed = Column(NUMBER(1, 0, False), comment='接收人已读状态 1|0')


t_i_delete_flow_temp = Table(
    'i_delete_flow_temp', metadata,
    Column('flow_id', VARCHAR(36))
)


class IDirectionInstance(Base):
    __tablename__ = 'i_direction_instance'
    __table_args__ = {'comment': '转移流程实例'}

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
    pre_type = Column(NUMBER(asdecimal=False), comment='前置类型 1-活动 2-网关')
    record_id = Column(VARCHAR(36), comment='记录ID，一次转件到多个活动，此ID为一致')
    pre_id = Column(VARCHAR(36), comment='前置ID')
    after_id = Column(VARCHAR(36), comment='后置ID')
    after_type = Column(NUMBER(asdecimal=False), comment='后置类型 1-活动 2-网关')
    flow_instance_id = Column(VARCHAR(36), comment='流程实例ID')


class IEventRecord(Base):
    __tablename__ = 'i_event_record'
    __table_args__ = {'comment': '事件执行记录'}

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
    i_flow_instance_id = Column(VARCHAR(36), comment='流程实例ID')
    trigger_position = Column(NUMBER(asdecimal=False), comment='事件触发位置编号，从事件表带入或自行选择')
    i_end = Column(NUMBER(1, 0, False), comment='是否归档')
    i_finished = Column(NUMBER(1, 0, False), comment='是否执行完成')
    condition_event_id = Column(VARCHAR(36), comment='条件事件ID')


class IFlowDatum(Base):
    __tablename__ = 'i_flow_data'
    __table_args__ = {'comment': '流程数据'}

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
    object_type = Column(NUMBER(asdecimal=False), comment='对象类型 1-流程；2-活动；3-网关')
    object_id = Column(VARCHAR(36), comment='对象ID')
    data = Column(Text, comment='数据')
    i_end = Column(NUMBER(1, 0, False), comment='是否归档')


class IFlowInstance(Base):
    __tablename__ = 'i_flow_instance'
    __table_args__ = (
        Index('idex_flowinstance_id_status', 'status', 'i_test', 'id'),
        {'comment': '流程实例'}
    )

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
    code_template_id = Column(VARCHAR(36), comment='编码模板ID')
    name = Column(VARCHAR(256), comment='流程名称')
    code = Column(VARCHAR(256), comment='业务编码号')
    start_time = Column(DateTime, comment='流程启动时间')
    end_time = Column(DateTime, comment='流程归档时间')
    parent_flow_ins_id = Column(VARCHAR(36), index=True, comment='父流程实例ID')
    i_end = Column(NUMBER(1, 0, False), comment='是否归档')
    status = Column(NUMBER(asdecimal=False), comment='流程状态 1-正常 160-已作废')
    parent_activity_ins_id = Column(VARCHAR(36), comment='父流程活动实例ID')
    describtion = Column(VARCHAR(1024), comment='流程描述')
    i_test = Column(NUMBER(1, 0, False), comment='是否测试案件 1-是 0-否，默认为0')
    i_external = Column(NUMBER(1, 0, False), comment='是否外部流程：1是 0否')
    external_flow_id = Column(VARCHAR(36), comment='外部流程ID')
    handle_source = Column(NVARCHAR(64), comment='办件来源')
    to_system_id = Column(NVARCHAR(36), comment='所属系统ID')
    should_finish_time = Column(DateTime, comment='流程应完成时间')
    time_limit = Column(Integer, comment='时限(单位是分)')
    i_work_day = Column(Integer, comment='是否工作日(1-是  0-否)')


class IFlowMaterial(Base):
    __tablename__ = 'i_flow_materials'
    __table_args__ = {'comment': '收件材料实例'}

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
    flow_instance_id = Column(VARCHAR(36), index=True, comment='流程实例ID')
    flow_materials_id = Column(VARCHAR(36), comment='材料模板ID')
    i_end = Column(NUMBER(1, 0, False), comment='是否归档')
    exp_field_value = Column(VARCHAR(256), comment='扩展字段用户选择值[{"字段id":"value"},{"字段id":"value"}]')
    name = Column(NVARCHAR(256), comment='材料名称')
    must_rcv_acti_cfg = Column(VARCHAR(2000), comment='必收活动ID activity_id1,activity_id2,activity_Id3')
    can_lack_acti_cfg = Column(VARCHAR(2000), comment='容缺活动ID activity_id1,activity_id2,activity_Id3')
    readonly_acti_cfg = Column(VARCHAR(2000), comment='只读活动')
    exp_field_cfg = Column(VARCHAR(2000), comment="扩展字段设置 {字段id:{defaut:value;i_show:1/0;i_user:1/0;dom_type:'checkbox/select';}}")
    discriminator = Column(NUMBER(asdecimal=False), comment='0/null:正常收件材料  1:面向流程扩展字段 ')
    flow_materials_catalog_id = Column(VARCHAR(36), comment='材料目录实例ID')
    full_path = Column(NVARCHAR(256), comment='材料完成路径')
    bz = Column(NVARCHAR(255), comment='材料描述')
    show_activity_cfg = Column(Text, comment='显示活动ID activity_id1,activity_id2,activity_Id3')
    view_can_up_cfg = Column(VARCHAR(2000))
    file_upload_format = Column(VARCHAR(512), comment='可上传文件格式，默认全部，格式不区分大小写 如：jpg,png,bmp')


class IFlowMaterialsCatalog(Base):
    __tablename__ = 'i_flow_materials_catalog'
    __table_args__ = {'comment': '目录实例'}

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
    flow_instance_id = Column(VARCHAR(36), comment='流程实例ID')
    flow_materials_id = Column(VARCHAR(36), comment='材料目录模板ID')
    i_end = Column(NUMBER(1, 0, False), comment='是否归档')
    name = Column(VARCHAR(64), comment='目录名称')
    parent_id = Column(VARCHAR(36), comment='父级主键')
    full_path = Column(VARCHAR(256), comment='完成路径')


class IFlowMaterialsFile(Base):
    __tablename__ = 'i_flow_materials_file'
    __table_args__ = {'comment': '收件材料文件表'}

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
    flow_materials_id = Column(VARCHAR(36), index=True, comment='收件材料实例表外键')
    name = Column(VARCHAR(1024), comment='文件名')
    suffix = Column(VARCHAR(16), comment='后缀')
    file_url = Column(VARCHAR(2000), comment='文件地址')
    file_id = Column(VARCHAR(36), comment='文件管理系统ID')
    i_end = Column(NUMBER(asdecimal=False), comment='是否归档')


class IFlowOpinion(Base):
    __tablename__ = 'i_flow_opinion'
    __table_args__ = {'comment': '流程意见实例'}

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
    flow_instance_id = Column(VARCHAR(36), index=True, comment='流程实例ID')
    activity_instance_id = Column(VARCHAR(36), comment='流程活动ID')
    participant_id = Column(VARCHAR(36), comment='参与人ID')
    opinion_content = Column(NVARCHAR(2000), comment='意见内容')
    opinion_time = Column(DateTime, comment='意见时间')
    sign = Column(VARCHAR(1024), comment='签名内容 可输入URL或者 签名文本')
    flow_opinion_id = Column(VARCHAR(36), comment='意见模板ID')


class IFlowRecord(Base):
    __tablename__ = 'i_flow_record'
    __table_args__ = {'comment': '流程整体日志'}

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
    ope_type = Column(NUMBER(asdecimal=False), comment='操作类型 10-转件 20-接件 30-追回 40-退件 50-挂起 60-恢复挂起 \n70-作废 80-恢复作废 90-彻底删除 100-督办 \n110取消督办 120-关注 130-取消关注 140-抄送 150-委托')
    ope_id = Column(VARCHAR(36), comment='操作ID ')
    flow_instance_id = Column(VARCHAR(36), comment='流程实例ID')


class IGatewayInsParticipant(Base):
    __tablename__ = 'i_gateway_ins_participant'
    __table_args__ = {'comment': '网关参与人缓存实例'}

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
    gateway_instance_id = Column(VARCHAR(36), comment='网关实例ID')
    direction_instance_id = Column(VARCHAR(36), comment='流向实例ID')
    activity_ins_participant = Column(VARCHAR(36), comment='参与人ID')
    direction_after_acti_ins_id = Column(VARCHAR(36), comment='流向后置活动实例ID')
    gateway_template_id = Column(VARCHAR(36), comment='网关模板ID')
    direction_template_id = Column(VARCHAR(36), comment='流向模板ID')
    direction_after_acti_temp_id = Column(VARCHAR(36), comment='流向后置活动模板ID')
    i_end = Column(NUMBER(1, 0, False), comment='是否归档')


class IGatewayInstance(Base):
    __tablename__ = 'i_gateway_instance'
    __table_args__ = {'comment': '网关实例'}

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
    name = Column(VARCHAR(64), comment='网关名称')
    gateway_template_id = Column(VARCHAR(36), comment='网关模板ID')
    status = Column(NUMBER(1, 0, False), comment='执行状态 1-已执行 0-未执行')
    i_end = Column(NUMBER(1, 0, False), comment='是否归档')


class IHangup(Base):
    __tablename__ = 'i_hangup'
    __table_args__ = {'comment': '流程实例'}

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
    hangup_apply_user_id = Column(VARCHAR(36), comment='申请挂起人')
    flow_instance_id = Column(VARCHAR(36), comment='流程实例ID')
    hangup_time = Column(DateTime, comment='挂起时间')
    hangup_apply_time = Column(DateTime, comment='申请挂起时间')
    hangup_reason = Column(NVARCHAR(1024), comment='挂起理由')
    i_hanguped = Column(NUMBER(3, 0, False), comment='是否已挂起 1|0')
    un_hangup_reason = Column(NVARCHAR(1024), comment='解挂理由')
    cancel_user_id = Column(VARCHAR(36), comment='取消挂起人')
    cancel_time = Column(DateTime, comment='取消挂起时间')
    hangup_activity_instance_id = Column(VARCHAR(36), comment='挂起活动实例ID')


class INullyApply(Base):
    __tablename__ = 'i_nully_apply'
    __table_args__ = (
        Index('idx_nully_fid_nullied', 'void_flow_instance_id', 'i_nullied'),
        {'comment': '作废申请表'}
    )

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
    nully_apply_user_id = Column(VARCHAR(36), comment='申请作废人')
    flow_instance_id = Column(VARCHAR(36), comment='作废流程实例ID')
    nully_time = Column(DateTime, comment='作废时间')
    nully_apply_time = Column(DateTime, comment='申请作废时间')
    nully_reason = Column(NVARCHAR(1024), comment='申请理由')
    i_nullied = Column(NUMBER(3, 0, False), comment='0|10|20|30  0未作废 10已作废 20已取消 30已恢复 40彻底作废')
    cancel_user_id = Column(VARCHAR(36), comment='取消作废人')
    cancel_time = Column(DateTime, comment='取消作废时间')
    void_flow_instance_id = Column(VARCHAR(36), index=True, comment='被作废的流程实例ID')
    recover_reason = Column(NVARCHAR(1024), comment='恢复原因')


class IRelFormRelReport(Base):
    __tablename__ = 'i_rel_form_rel_report'
    __table_args__ = {'comment': '活动实例表单报表关联表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    index_code = Column(Integer, comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(Integer, comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    acti_form_rel_id = Column(VARCHAR(36), comment='活动实例表单关联表id')
    report_id = Column(VARCHAR(36), comment='报表id')


t_i_rel_form_rel_report_20200806 = Table(
    'i_rel_form_rel_report_20200806', metadata,
    Column('id', VARCHAR(36)),
    Column('index_code', Integer),
    Column('create_worker', VARCHAR(36)),
    Column('create_time', DateTime),
    Column('latest_modify_worker', NVARCHAR(36)),
    Column('latest_modify_time', DateTime),
    Column('isvalid', Integer),
    Column('bz1', NVARCHAR(255)),
    Column('bz2', NVARCHAR(255)),
    Column('bz3', NVARCHAR(255)),
    Column('bz4', NVARCHAR(255)),
    Column('acti_form_rel_id', VARCHAR(36)),
    Column('report_id', VARCHAR(36))
)


t_i_rel_form_rel_report_copy = Table(
    'i_rel_form_rel_report_copy', metadata,
    Column('id', VARCHAR(36)),
    Column('index_code', Integer),
    Column('create_worker', VARCHAR(36)),
    Column('create_time', DateTime),
    Column('latest_modify_worker', NVARCHAR(36)),
    Column('latest_modify_time', DateTime),
    Column('isvalid', Integer),
    Column('bz1', NVARCHAR(255)),
    Column('bz2', NVARCHAR(255)),
    Column('bz3', NVARCHAR(255)),
    Column('bz4', NVARCHAR(255)),
    Column('acti_form_rel_id', VARCHAR(36)),
    Column('report_id', VARCHAR(36))
)


class ISendBackRecord(Base):
    __tablename__ = 'i_send_back_record'
    __table_args__ = {'comment': '退件日志表'}

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
    back_worker_id = Column(VARCHAR(36), comment='退件人ID')
    b_back_activity_id = Column(VARCHAR(36), comment='被退件活动ID')
    b_back_acti_tem_id = Column(VARCHAR(36), comment='被退件活动模板ID')
    b_back_activity_name = Column(VARCHAR(128), comment='被退件活动名称')
    back_to_activity_id = Column(VARCHAR(36), comment='退至活动ID（新创）')
    back_to_acti_tem_id = Column(VARCHAR(36), comment='退至活动模板ID（新创）')
    back_to_activity_name = Column(VARCHAR(128), comment='退至活动名称（新创）')
    back_reason = Column(VARCHAR(512), comment='退件原因')
    back_to_his_activity_id = Column(VARCHAR(36), comment='退至活动ID（历史）')


class ISuperviseInstance(Base):
    __tablename__ = 'i_supervise_instance'
    __table_args__ = {'comment': '督办实例'}

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
    supervise_user_id = Column(VARCHAR(36), comment='督办人')
    supervise_time = Column(DateTime, comment='督办时间')
    supervise_apply_time = Column(DateTime, comment='申请督办时间')
    supervise_reason = Column(NVARCHAR(2000), comment='申请理由')
    i_supervise = Column(NUMBER(3, 0, False), comment='10未督办 20已督办 30取消督办')
    cancel_user_id = Column(VARCHAR(36), comment='取消督办人')
    cancel_time = Column(DateTime, comment='取消督办时间')
    recover_reason = Column(NVARCHAR(2000), comment='取消督办原因')
    sprv_flow_instance_id = Column(VARCHAR(36), comment='被督办流程实例ID')
    flow_instance_id = Column(VARCHAR(36), comment='督办流程实例ID')


t_import_rel_activity = Table(
    'import_rel_activity', metadata,
    Column('t_flow_template_version_id', VARCHAR(512), comment='万维流程模板版本ID'),
    Column('t_activity_template_id', VARCHAR(512), comment='万维活动模板ID'),
    Column('t_activity_template_name', VARCHAR(512), comment='万维活动名称'),
    Column('gh_template_id', VARCHAR(512), comment='规划流程模板ID'),
    Column('gh_flow_name', VARCHAR(512), comment='规划流程名称'),
    Column('gh_activity_name', VARCHAR(512), comment='规划活动名称'),
    Column('t_flow_template_name', VARCHAR(512), comment='万维流程模板名称'),
    Column('gh_template_name', VARCHAR(512), comment='规划流程模板名称'),
    Column('gh_activity_id', VARCHAR(512), comment='规划活动模板ID'),
    Column('a_count', NUMBER(5, 0, False), comment='个数'),
    Column('delete_flag', NUMBER(1, 0, False), comment='删除标识 1-是'),
    Column('id', VARCHAR(36), comment='唯一标识符')
)


t_import_rel_template = Table(
    'import_rel_template', metadata,
    Column('gh_template_id', VARCHAR(100), comment='规划模板ID'),
    Column('t_flow_template_version_id', VARCHAR(100), comment='万维流程版本ID'),
    Column('t_flow_template_name', VARCHAR(500), comment='万维流程模板名称'),
    Column('gh_flow_name', VARCHAR(500), comment='规划流程名称'),
    Column('t_flow_template_version_remark', VARCHAR(500), comment='万维流程版本备注'),
    Column('gh_template_name', VARCHAR(500), comment='规划模板名称')
)


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
    system_mark = Column(NVARCHAR(255), comment='系统标识')


class PersonalKeyValue(Base):
    __tablename__ = 'personal_key_value'
    __table_args__ = {'comment': '个人相关设置'}

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
    key = Column(NVARCHAR(64), comment='键')
    value = Column(Text, comment='值')
    user_id = Column(VARCHAR(36), comment='用户ID')


class TActivityTemplate(Base):
    __tablename__ = 't_activity_template'
    __table_args__ = {'comment': '活动模板表'}

    id = Column(VARCHAR(36), primary_key=True)
    index_code = Column(Integer, comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(VARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(Integer, comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    flow_template_version_id = Column(VARCHAR(36), comment='流程模板版本表外键')
    name = Column(NVARCHAR(64), comment='活动名称')
    i_auto_transfer = Column(Integer, comment='转件时无需选人自动转走，1:是 0:否')
    i_archive_no_needed = Column(Integer, comment='未完成可归档 1-是  0-否')
    i_public_waiting_box = Column(Integer, comment='启用公共待办箱')
    i_limit_time = Column(Integer, comment='启用活动时限')
    time_limit = Column(Integer, comment='时限(单位是分，超过一天的分钟数，转换为天)')
    type = Column(Integer, comment='开始-10 结束-100 过程-20')
    i_work_day = Column(Integer, comment='是否工作日 1-是  0-否')
    activity_mark = Column(VARCHAR(64), comment='活动标识')
    mutex_logic = Column(NVARCHAR(1024), comment='后置活动前端转件互斥逻辑')
    mutex_logic_tip = Column(NVARCHAR(64), comment='不满足互斥条件的提示信息')
    message_notice_method = Column(NVARCHAR(128), comment='消息通知方式')


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


class TConditionEvent(Base):
    __tablename__ = 't_condition_event'
    __table_args__ = {'comment': '条件事件管理表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    name = Column(NVARCHAR(64), comment='事件条件名称')
    system_id = Column(VARCHAR(36), comment='所属系统ID')
    execution_type = Column(Integer, comment='事件类型（1：Restful服务 2：Sql语句）')
    restful_url = Column(NVARCHAR(256), comment='Restful服务地址')
    sql_statement = Column(NVARCHAR(2000), comment='SQL语句')
    i_asynchronous = Column(Integer, comment='是否异步（1：是 0：否）')
    event_position = Column(Integer, comment='事件位置，参考原型设计页面编号4')
    index_code = Column(Integer, comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(VARCHAR(36), comment='最后更新人')
    latest_modify_time = Column(DateTime, comment='最后更新时间')
    isvalid = Column(Integer, comment='是否合法')
    bz1 = Column(NVARCHAR(255), comment='BZ1')
    bz2 = Column(NVARCHAR(255), comment='BZ2')
    bz3 = Column(NVARCHAR(255), comment='BZ3')
    bz4 = Column(NVARCHAR(255), comment='BZ4')
    params = Column(Text, comment='参数 JSON格式')


t_t_condition_event_rel = Table(
    't_condition_event_rel', metadata,
    Column('id', VARCHAR(36), nullable=False, comment='主键'),
    Column('index_code', Integer, comment='排序编号'),
    Column('create_worker', VARCHAR(36), comment='创建人'),
    Column('create_time', DateTime, comment='创建时间'),
    Column('latest_modify_worker', VARCHAR(36), comment='最后修改人'),
    Column('latest_modify_time', DateTime, comment='最后修改时间'),
    Column('isvalid', Integer, comment='是否启用'),
    Column('bz1', NVARCHAR(255), comment='备注1'),
    Column('bz2', NVARCHAR(255), comment='备注2'),
    Column('bz3', NVARCHAR(255), comment='备注3'),
    Column('bz4', NVARCHAR(255), comment='备注4'),
    Column('condition_event_id', VARCHAR(36), comment='事件模板ID'),
    Column('trigger_position', Integer, comment='事件触发位置编号，从事件表带入或自行选择'),
    Column('object_id', VARCHAR(36), comment='对象ID'),
    Column('logic_rel', VARCHAR(2), comment='条件逻辑关系 &&-与运算、||-或运算、^-异或运算、！-非运算'),
    Column('object_type', NUMBER(1, 0, False), comment='对象类型 1-流程；2-活动； 3-流向'),
    comment='流程模板关联事件表'
)


class TDirectionTemplate(Base):
    __tablename__ = 't_direction_template'
    __table_args__ = {'comment': '流向模板表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    index_code = Column(Integer, comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(VARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(Integer, comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    name = Column(NVARCHAR(64), comment='流向名')
    flow_template_version_id = Column(VARCHAR(36), comment='流程模板版本表外键')
    pre_node_name = Column(VARCHAR(128), comment='前置节点名称，可能是活动或网关或子流程')
    after_node_name = Column(VARCHAR(128), comment='后置节点名称，可能是活动或网关或子流程')
    i_auto_transfer = Column(Integer, comment='转件时无需选人自动转走，1:是 0:否')
    transfer_order = Column(Integer, comment='转件排序')


class TFlowCatalog(Base):
    __tablename__ = 't_flow_catalog'
    __table_args__ = {'comment': '流程目录表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    parent_id = Column(VARCHAR(36), comment='父级主键')
    name = Column(NVARCHAR(32), comment='流程目录名')
    describe = Column(NVARCHAR(255), comment='描述')
    index_code = Column(Integer, comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(Integer, comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    icon_url = Column(NVARCHAR(512), comment='流程目录图标URL')
    color = Column(NVARCHAR(32), comment='目录色彩')


class TFlowMaterial(Base):
    __tablename__ = 't_flow_materials'
    __table_args__ = {'comment': '流程收件材料配置'}

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
    flow_materials_catalog_id = Column(VARCHAR(36), comment='流程收件材料目录ID')
    name = Column(NVARCHAR(256), comment='材料名称')
    bz = Column(NVARCHAR(512), comment='材料描述')
    exp_field_cfg = Column(VARCHAR(2000), comment="扩展字段设置 {字段id:{defaut:value;i_show:1/0;i_user:1/0;dom_type:'checkbox/select';}}")
    must_rcv_acti_cfg = Column(VARCHAR(2000), comment='必收活动ID activity_id1,activity_id2,activity_Id3')
    can_lack_acti_cfg = Column(VARCHAR(2000), comment='容缺活动ID activity_id1,activity_id2,activity_Id3')
    discriminator = Column(NUMBER(asdecimal=False), comment='0/null:正常收件材料  1:面向流程扩展字段 ')
    readonly_acti_cfg = Column(VARCHAR(2000), comment='只读活动')
    i_uncreate_materials = Column(NUMBER(1, 0, False), comment='流程启动是否不创建收件材料 1--不创建 0--创建')
    show_activity_cfg = Column(Text, comment='显示活动ID activity_id1,activity_id2,activity_Id3')
    view_can_up_cfg = Column(VARCHAR(2000))
    file_upload_format = Column(NVARCHAR(512), comment='可上传文件格式，默认全部，格式不区分大小写 如：jpg,png,bmp')


class TFlowMaterialsCatalog(Base):
    __tablename__ = 't_flow_materials_catalog'
    __table_args__ = {'comment': '流程收件材料目录'}

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
    name = Column(VARCHAR(64), comment='目录名称')
    parent_id = Column(VARCHAR(36), comment='父级主键')


class TFlowOpPersonal(Base):
    __tablename__ = 't_flow_op_personal'
    __table_args__ = {'comment': '个人意见设置'}

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
    user_id = Column(VARCHAR(36), comment='用户ID')
    content = Column(NVARCHAR(1024), comment='意见内容')
    activity_template_id = Column(NVARCHAR(36), comment='活动模板ID')
    i_dedicated_opinion = Column(NUMBER(1, 0, False), comment='是否当前活动模板专用意见')
    i_sys = Column(NUMBER(1, 0, False), comment='是否系统意见')


class TFlowOpTemplate(Base):
    __tablename__ = 't_flow_op_template'
    __table_args__ = {'comment': '流程意见模板'}

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
    html_content = Column(VARCHAR(2000), comment='HTML内容')
    i_enable = Column(NUMBER(1, 0, False), comment='是否启用')
    opinion_use = Column(NUMBER(1, 0, False), comment='意见模板用途（0：PC端 1：移动端）')


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
    opinion_name = Column(NVARCHAR(64), comment='意见名称')
    opinion_user_text = Column(NVARCHAR(64), comment='意见人文本')
    opinion_time_text = Column(NVARCHAR(64), comment='意见时间文本')
    sign_type = Column(NUMBER(1, 0, False), comment='签名类型 1-数字签名 2-文本输入')
    activity_template_id = Column(VARCHAR(36), comment='活动模板ID')
    i_system_show = Column(Integer, comment='是否系统显示(1：是 0：否，非系统显示，需要业务端处理显示)')
    sort_mode = Column(Integer, comment='意见排序模式(1：以人员级别 0：以后台活动配置顺序)')
    i_hide_non_filled_comment = Column(Integer, comment='隐藏非本活动未填写意见(1：是 0：否)')
    i_show_my_opinion = Column(Integer, comment='单活动多意见只显示本人(1：是 0：否)')
    i_enable = Column(Integer, comment='是否启用(1：是 0：否)')


class TFlowTemplate(Base):
    __tablename__ = 't_flow_template'
    __table_args__ = {'comment': '流程模板表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    flow_catalog_id = Column(VARCHAR(36), comment='流程目录ID')
    name = Column(NVARCHAR(256), comment='流程模板名')
    describe = Column(NVARCHAR(512), comment='描述')
    index_code = Column(Integer, comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(Integer, comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    flow_template_type = Column(Integer, comment='1-正常流程  2-挂起（系统流程） 3-作废（系统流程） 4-督办（系统流程）')
    i_external = Column(Integer, comment='1:外部流程 0非外部流程')
    to_system_id = Column(NVARCHAR(32), comment='所属系统ID')
    flow_mark = Column(NVARCHAR(36), comment='流程标识')
    i_limit_time = Column(Integer, comment='启用流程时限')
    time_limit = Column(Integer, comment='时限(单位是分)')
    i_work_day = Column(Integer, comment='是否工作日(1-是  0-否)')


t_t_flow_template_history = Table(
    't_flow_template_history', metadata,
    Column('id', VARCHAR(36), nullable=False),
    Column('flow_catalog_id', VARCHAR(36)),
    Column('name', NVARCHAR(256)),
    Column('describe', NVARCHAR(512)),
    Column('index_code', Integer),
    Column('create_worker', VARCHAR(36)),
    Column('create_time', DateTime),
    Column('latest_modify_worker', NVARCHAR(36)),
    Column('latest_modify_time', DateTime),
    Column('isvalid', Integer),
    Column('bz1', NVARCHAR(255)),
    Column('bz2', NVARCHAR(255)),
    Column('bz3', NVARCHAR(255)),
    Column('bz4', NVARCHAR(255)),
    Column('flow_template_type', Integer),
    Column('i_external', Integer)
)


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
    version_enable = Column(Integer, comment='版本是否启用')
    version_autoenable_time = Column(DateTime, comment='版本自动启用时间')
    index_code = Column(Integer, comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(Integer, comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    code_template_id = Column(VARCHAR(36), comment='编码模板ID')
    inheritance_version_id = Column(VARCHAR(36), comment='继承版本ID')


class TFlowWaitForOpinion(Base):
    __tablename__ = 't_flow_wait_for_opinion'
    __table_args__ = {'comment': '立等可取意见配置'}

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
    activity_template_id = Column(VARCHAR(36), comment='活动模板ID')
    opinion_name = Column(VARCHAR(64), comment='意见名称')
    opinion_user_text = Column(VARCHAR(64), comment='意见人文本')
    opinion_time_text = Column(VARCHAR(64), comment='意见时间文本')
    sys_op_content = Column(NVARCHAR(256), comment='系统意见内容')
    participant_id = Column(VARCHAR(36), comment='参与人ID')
    department_id = Column(VARCHAR(36), comment='部门ID')
    opinion_mark = Column(VARCHAR(36), comment='意见标识')


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


class TFunctionBtnRel(Base):
    __tablename__ = 't_function_btn_rel'
    __table_args__ = {'comment': '功能按钮关联表'}

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
    i_show = Column(NUMBER(asdecimal=False), comment='是否显示')
    object_type = Column(NUMBER(asdecimal=False), comment='对象类型 1-流程；2-活动')
    object_id = Column(VARCHAR(36), comment='对象ID')
    btn_type = Column(NUMBER(asdecimal=False), comment='功能按钮类型 160-作废；190-关注；210-抄送；240-挂起；260-督办')


class TGatewayTemplate(Base):
    __tablename__ = 't_gateway_template'
    __table_args__ = {'comment': '网关模板表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    index_code = Column(Integer, comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(VARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(Integer, comment='是否启用')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    name = Column(NVARCHAR(64), comment='网关名')
    flow_template_version_id = Column(VARCHAR(36), comment='流程模板版本表外键')
    i_show_post_position = Column(NUMBER(asdecimal=False), comment='转件是否显示后置活动')
    transfer_judge = Column(NUMBER(asdecimal=False), comment='网关转出参与人判定 1-取所有参与人的并集 2-取所有参与人的交集 3-取最后一个前置活动指定的参与人 4-取第一个前置活动指定的参与人 5-指定某个活动/指定人的指定参与人\n')


class TMaterialsExpCfg(Base):
    __tablename__ = 't_materials_exp_cfg'
    __table_args__ = {'comment': '收件材料字段扩展'}

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
    name = Column(VARCHAR(64), comment='字段名称')


class TMaterialsExpCfgOption(Base):
    __tablename__ = 't_materials_exp_cfg_option'
    __table_args__ = {'comment': '收件材料字段扩展选项'}

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
    materials_exp_cfg_id = Column(VARCHAR(36), comment='父表主键ID')
    name = Column(VARCHAR(64), comment='显示名称')
    value = Column(NUMBER(asdecimal=False), comment='数据库存储值')


class TParticipantFilter(Base):
    __tablename__ = 't_participant_filter'
    __table_args__ = {'comment': '参与人过滤管理表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    flow_participant_group_id = Column(VARCHAR(36), comment='参与人组ID')
    participant_type_first = Column(Integer, comment='可参与人员类型指定首级')
    participant_type_secondary = Column(NVARCHAR(128), comment='可参与人员类型指定次级')
    i_default_display = Column(Integer, comment='可参与人员是否默认显示（1：是 0：否）')
    filter_type = Column(Integer, comment='过滤类型（1：交集 0：并集）')
    i_enable = Column(Integer, comment='是否启用（1：是 0：否）')
    remark = Column(NVARCHAR(255), comment='备注')
    index_code = Column(Integer, comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(VARCHAR(36), comment='最后更新人')
    latest_modify_time = Column(DateTime, comment='最后更新时间')
    isvalid = Column(Integer, comment='是否合法')
    bz1 = Column(NVARCHAR(255), comment='BZ1')
    bz2 = Column(NVARCHAR(255), comment='BZ2')
    bz3 = Column(NVARCHAR(255), comment='BZ3')
    bz4 = Column(NVARCHAR(255), comment='BZ4')
    param_json = Column(NVARCHAR(1000), comment='自定义参与人参数JSON')


class TParticipantGroup(Base):
    __tablename__ = 't_participant_group'
    __table_args__ = {'comment': '参与人组管理表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    parent_id = Column(VARCHAR(36), comment='父级ID')
    name = Column(NVARCHAR(64), comment='参与人组名称')
    remark = Column(NVARCHAR(255), comment='备注')
    index_code = Column(Integer, comment='排序编号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(VARCHAR(36), comment='最后更新人')
    latest_modify_time = Column(DateTime, comment='最后更新时间')
    isvalid = Column(Integer, comment='是否合法')
    bz1 = Column(NVARCHAR(255), comment='BZ1')
    bz2 = Column(NVARCHAR(255), comment='BZ2')
    bz3 = Column(NVARCHAR(255), comment='BZ3')
    bz4 = Column(NVARCHAR(255), comment='BZ4')


class TParticipantGroupRel(Base):
    __tablename__ = 't_participant_group_rel'
    __table_args__ = {'comment': '参与人组关联'}

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
    participant_group_id = Column(NVARCHAR(36), comment='参与人组ID')
    trigger_position = Column(NUMBER(asdecimal=False), comment='参与人组位置，看原型2.1显示过滤等下面数字')
    object_type = Column(NUMBER(1, 0, False), comment='对象类型 1-流程版本；2-活动； 3-流向，再确定哪个位置即可')
    object_id = Column(VARCHAR(36), comment='对象ID')


class TReturnConfig(Base):
    __tablename__ = 't_return_config'
    __table_args__ = {'comment': '退件配置'}

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
    activity_template_id = Column(VARCHAR(36), comment='活动模板ID')
    i_return_current_branch = Column(NUMBER(1, 0, False), comment='是否只退回当前分支')


class TSameLevelTransferConfig(Base):
    __tablename__ = 't_same_level_transfer_config'
    __table_args__ = {'comment': '同级转件配置'}

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
    activity_template_id = Column(VARCHAR(36), comment='活动模板ID')
    i_requried_opinion = Column(NUMBER(1, 0, False), comment='是否必填意见')


t_v_get_actv_name = Table(
    'v_get_actv_name', metadata,
    Column('flow_template_version_id', VARCHAR(36)),
    Column('id', VARCHAR(36), nullable=False),
    Column('name', NVARCHAR(64)),
    Column('gh_template_id', VARCHAR(512)),
    Column('gh_activity_id', VARCHAR(512)),
    Column('rn', NUMBER(asdecimal=False))
)


t_v_t_rel = Table(
    'v_t_rel', metadata,
    Column('id', VARCHAR(36), nullable=False),
    Column('gh_flowid', NVARCHAR(255)),
    Column('version_describe', NVARCHAR(255)),
    Column('name', NVARCHAR(256))
)


t_v_t_rel_lsq = Table(
    'v_t_rel_lsq', metadata,
    Column('id', VARCHAR(36), nullable=False),
    Column('gh_flowid', NVARCHAR(255)),
    Column('version_describe', NVARCHAR(255)),
    Column('name', NVARCHAR(256))
)


t_v_update_import_rel_activity = Table(
    'v_update_import_rel_activity', metadata,
    Column('id', VARCHAR(36), nullable=False),
    Column('name', NVARCHAR(64))
)
