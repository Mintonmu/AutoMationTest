# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, LargeBinary, NVARCHAR, Table, Text, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AvailableNum(Base):
    __tablename__ = 'available_num'

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    num = Column(Integer, comment='流水号')
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
    flow_num_id = Column(VARCHAR(36), comment='编码管理（编码详细）表ID')


class CodeTemplate(Base):
    __tablename__ = 'code_template'
    __table_args__ = {'comment': '业务通用模块-编码管理（编码模板）'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    to_system_id = Column(NVARCHAR(64), comment='所属系统ID')
    template_name = Column(NVARCHAR(64), comment='模板名称')
    template_body = Column(NVARCHAR(1024), comment='模板主体内容')
    bz = Column(NVARCHAR(255), comment='备注')
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


class Dictionary(Base):
    __tablename__ = 'dictionary'
    __table_args__ = {'comment': '业务通用模块-字典管理'}

    id = Column(VARCHAR(36), primary_key=True, comment='ID')
    to_system_id = Column(NVARCHAR(64), comment='所属系统ID，数据来自MIS表管理')
    classify = Column(NVARCHAR(64), comment='字典类型')
    code = Column(NVARCHAR(64), comment='字典编码')
    name = Column(NVARCHAR(64), comment='字典名称')
    shortername = Column(NVARCHAR(64), comment='简称')
    pid = Column(VARCHAR(36), comment='父字典项ID')
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
    bz = Column(NVARCHAR(255), comment='备注')
    i_enable = Column(NUMBER(asdecimal=False), comment='是否启用')


class FakeFlow(Base):
    __tablename__ = 'fake_flow'
    __table_args__ = {'comment': '虚拟流程表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    index_code = Column(NUMBER(asdecimal=False), comment='排序序号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否合法')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    fakeflow_name = Column(NVARCHAR(64), comment='虚拟流程名称')
    fakeflow_mark = Column(NVARCHAR(64), comment='虚拟流程标识')
    bz = Column(NVARCHAR(255), comment='说明')
    serverlayer_ids = Column(NVARCHAR(255), comment='专题图服务ID集合(,隔开)')
    serverlayer_names = Column(NVARCHAR(255), comment='专题图服务名称集合(,隔开)')


class FlowNum(Base):
    __tablename__ = 'flow_num'
    __table_args__ = {'comment': '业务通用模块-编码管理（编码详细）'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    start_num = Column(NUMBER(asdecimal=False), comment='流水号的开始值，如00001')
    max_num = Column(NUMBER(asdecimal=False), comment='已生成的最大号')
    classify = Column(NVARCHAR(128), comment='编码的类型，如验证测量编号，不同的编码类型流水号都是从设定的初始值开始(1)')
    fill_word = Column(VARCHAR(10), comment='流水号填充的值，如00001中的数字1长度不足5位，在左侧填充4个0')
    figures = Column(NUMBER(asdecimal=False), comment='流水号的长度，如00001，长度为5')
    i_fill = Column(NUMBER(asdecimal=False), comment='是否填充，1,是 生成的流水号包括fillWord的值\n0,否 生成的流水号不包括')
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


class InwebsiteMessage(Base):
    __tablename__ = 'inwebsite_message'
    __table_args__ = {'comment': '站内信'}

    id = Column(VARCHAR(36), primary_key=True)
    send_user_id = Column(VARCHAR(36), comment='发送人ID')
    send_user_name = Column(NVARCHAR(64), comment='发送人姓名')
    content = Column(NVARCHAR(2000), comment='信息内容')
    send_time = Column(DateTime, comment='发送时间')
    pc_url = Column(NVARCHAR(256), comment='PC端URL')
    app_url = Column(NVARCHAR(256), comment='移动端URL')
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
    open_type = Column(NUMBER(1, 0, False), comment='打开页面方式 1--内部 2--新窗体')


class InwebsiteMessageSendRecord(Base):
    __tablename__ = 'inwebsite_message_send_record'
    __table_args__ = {'comment': '站内信发送记录'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    inwebsite_message_id = Column(VARCHAR(36), comment='站内信ID')
    receive_user_id = Column(VARCHAR(36), comment='接收人ID')
    receive_user_name = Column(NVARCHAR(64), comment='接收人姓名')
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
    i_read = Column(NUMBER(asdecimal=False), comment='是否已读')


class KeyValue(Base):
    __tablename__ = 'key_value'

    id = Column(VARCHAR(50), primary_key=True, comment='主键ID')
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
    key = Column(NVARCHAR(64), comment='键')
    value = Column(Text, comment='值')


class MailAttach(Base):
    __tablename__ = 'mail_attach'
    __table_args__ = {'comment': '邮件附件'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    mail_send_id = Column(VARCHAR(36), comment='MAIL_SEND表ID')
    file_name = Column(NVARCHAR(64), comment='文件名称')
    file_size = Column(NUMBER(asdecimal=False), comment='文件大小')
    file_url = Column(NVARCHAR(128), comment='文件路径')
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


class MailSend(Base):
    __tablename__ = 'mail_send'
    __table_args__ = {'comment': '邮件收件箱'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    send_user_id = Column(VARCHAR(36), comment='发送人ID')
    send_user_name = Column(NVARCHAR(64), comment='发送人姓名')
    send_time = Column(DateTime, comment='发送时间')
    i_attachment = Column(NUMBER(asdecimal=False), comment='是否包含附件')
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
    i_delayed = Column(NUMBER(asdecimal=False), comment='是否定时发送')
    brief_content = Column(NVARCHAR(2000), comment='简略内容  主题：内容...')
    i_delete = Column(NUMBER(asdecimal=False), comment='是否删除')
    i_draft = Column(NUMBER(asdecimal=False), comment='是否草稿')
    oid = Column(VARCHAR(36), comment='原邮件ID')
    mail_user_tag_id = Column(VARCHAR(36), comment='标签ID')
    classify = Column(NUMBER(asdecimal=False), comment='邮件分类   10,回复 20,转发')
    subject = Column(NVARCHAR(1024), comment='主题')
    i_urgent = Column(NUMBER(asdecimal=False), comment='是否紧急')
    i_need_receipt = Column(NUMBER(asdecimal=False), comment='是否需要回执')
    i_star = Column(NUMBER(asdecimal=False), comment='是否星标邮件')
    i_send_message = Column(NUMBER(asdecimal=False), comment='是否发送短信')


class MailSendContent(Base):
    __tablename__ = 'mail_send_content'
    __table_args__ = {'comment': '邮件内容'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    mail_send_id = Column(VARCHAR(36), comment='邮件ID')
    content = Column(Text, comment='邮件信息')
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


class MailSendReciveUser(Base):
    __tablename__ = 'mail_send_recive_user'
    __table_args__ = {'comment': '邮件发送'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    mail_send_id = Column(VARCHAR(36), comment='邮件ID')
    receive_user_id = Column(VARCHAR(36), comment='接收人ID')
    receive_user_name = Column(NVARCHAR(64), comment='接收人姓名')
    i_cc = Column(NUMBER(asdecimal=False), comment='是否抄送')
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
    i_read = Column(NUMBER(asdecimal=False), comment='是否已读')
    mail_user_tag_id = Column(VARCHAR(36), comment='标签')
    i_delete = Column(NUMBER(asdecimal=False), comment='是否删除')
    i_star = Column(NUMBER(asdecimal=False), comment='是否星标邮件')
    read_time = Column(DateTime, comment='查阅邮件时间')


class MailUserTag(Base):
    __tablename__ = 'mail_user_tag'
    __table_args__ = {'comment': '邮件标签表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    color = Column(NVARCHAR(8), comment='便签颜色')
    name = Column(NVARCHAR(64), comment='标签名')
    to_user_id = Column(VARCHAR(36), comment='所属人ID')
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


t_map_field_manage = Table(
    'map_field_manage', metadata,
    Column('id', NVARCHAR(36), nullable=False, comment='主键'),
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
    Column('field_name', NVARCHAR(64), comment='字段名称'),
    Column('field_alias', NVARCHAR(64), comment='字段别名'),
    Column('is_show_iquery', NUMBER(asdecimal=False), comment='是否显示I查询（0否1是）'),
    Column('is_support_attribute_query', NUMBER(asdecimal=False), comment='是否支持属性查询'),
    Column('is_show_query_list', NUMBER(asdecimal=False), comment='是否在查询列表中显示'),
    Column('is_enable', NUMBER(asdecimal=False), comment='是否启用'),
    Column('map_search_layer_id', NVARCHAR(36), comment='图层查询ID'),
    comment='图层字段配置管理'
)


class MapIField(Base):
    __tablename__ = 'map_i_field'
    __table_args__ = {'comment': '图层I查询字段配置'}

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
    field_name = Column(NVARCHAR(64), comment='字段名称')
    field_alias = Column(NVARCHAR(64), comment='字段别名')
    format_script = Column(NVARCHAR(256), comment='格式化脚本')
    map_i_search_layer_id = Column(VARCHAR(36), comment='I查询图层外键')


class MapISearchLayer(Base):
    __tablename__ = 'map_i_search_layer'
    __table_args__ = {'comment': 'I查询图层管理'}

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
    name = Column(NVARCHAR(64), comment='图层名称')
    alias = Column(NVARCHAR(64), comment='图层别名')
    flag_name = Column(NVARCHAR(64), comment='标识名称')
    connecter = Column(NVARCHAR(512), comment='连接参数')
    search_param = Column(NVARCHAR(512), comment='查询参数')
    min_scale = Column(NUMBER(asdecimal=False), comment='标注显示最小比例\t')
    max_scale = Column(NUMBER(asdecimal=False), comment='标注显示最大比例\t')
    querytype = Column(NUMBER(asdecimal=False), comment='查询方式(1:通过SDE连接参数查询,2:通过GIS服务地址查询)')
    gisserver_url = Column(NVARCHAR(255), comment='用于要素查询的GIS服务地址')


class MapRelFakeflow(Base):
    __tablename__ = 'map_rel_fakeflow'
    __table_args__ = {'comment': '地图配合和虚拟流程关联表'}

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
    fakeflow_template_id = Column(VARCHAR(64), comment='虚拟流程表主键ID')
    map_store_id = Column(VARCHAR(64), comment='图形仓库ID')


class MapRelFlow(Base):
    __tablename__ = 'map_rel_flow'
    __table_args__ = {'comment': '图层仓库关联流程'}

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
    flow_template_id = Column(VARCHAR(36), comment='流程模板ID')
    map_store_id = Column(VARCHAR(36), comment='图形仓库ID')


class MapStore(Base):
    __tablename__ = 'map_store'

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    index_code = Column(NUMBER(asdecimal=False), comment='排序序号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否合法')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    name = Column(NVARCHAR(64), comment='图形名称')
    connecter = Column(NVARCHAR(128), comment='连接字符串')
    location_layer = Column(VARCHAR(36), comment='定位图层(MAP_I_SEARCH_LAYER表ID)')
    location_field = Column(NVARCHAR(64), comment='定位字段')
    left_top_x = Column(NUMBER(asdecimal=False), comment='左上X')
    left_top_y = Column(NUMBER(asdecimal=False), comment='左上Y')
    right_bottom_x = Column(NUMBER(asdecimal=False), comment='右下X')
    right_bottom_y = Column(NUMBER(asdecimal=False), comment='右下Y')
    serch_tip = Column(NVARCHAR(128), comment='搜索提示内容')
    is_enable = Column(NUMBER(asdecimal=False), comment='是否启用')
    location_layer_name = Column(NVARCHAR(64), comment='定位图层名称')


class MapStoreServer(Base):
    __tablename__ = 'map_store_server'
    __table_args__ = {'comment': '图层仓库服务配置'}

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
    map_store_service_catalog = Column(VARCHAR(36), comment='目录ID，外键')
    name = Column(NVARCHAR(64), comment='图层名称')
    alias = Column(NVARCHAR(64), comment='图层别名')
    service_type = Column(NUMBER(1, 0, False), comment='服务类型 1-tiled 2-dynamic 3-吉奥wmts')
    node_type = Column(NUMBER(1, 0, False), comment='节点类型 1-mapService 2-geoMetryServer')
    clarity_ratio = Column(NUMBER(asdecimal=False), comment='透明度')
    url = Column(NVARCHAR(1024), comment='服务地址')
    i_image = Column(NUMBER(1, 0, False), comment='是否默认影像')
    i_vector = Column(NUMBER(1, 0, False), comment='默认矢量')
    ja_wmts_layer_id = Column(NVARCHAR(64), comment='图层ID(加载吉奥WMTS专用)')
    ja_wmts_style_id = Column(NVARCHAR(64), comment='样式ID(加载吉奥WMTS专用)\t')
    ja_wmts_cell_set = Column(NVARCHAR(512), comment='切片矩阵设置（加载吉奥WMTS专用）\t')
    i_visible = Column(NUMBER(1, 0, False), comment='是否可见')
    i_feature_query = Column(NUMBER(1, 0, False), comment='是否支持地块属性检索查询')
    i_identify_query = Column(NUMBER(1, 0, False), comment='是否支持i查询')


class MapStoreServiceCatalog(Base):
    __tablename__ = 'map_store_service_catalog'
    __table_args__ = {'comment': '图层仓库服务目录'}

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
    name = Column(NVARCHAR(64), comment='目录名称')
    i_edit = Column(NUMBER(1, 0, False), comment='是否可操作')
    parent_id = Column(VARCHAR(36), comment='父级ID')


class MessageAbutmentConfig(Base):
    __tablename__ = 'message_abutment_config'
    __table_args__ = {'comment': '消息模板对接配置'}

    id = Column(VARCHAR(32), primary_key=True, comment='主键ID')
    name = Column(NVARCHAR(64), comment='IM名称')
    send_url = Column(NVARCHAR(256), comment='发送URL')
    noread_url = Column(NVARCHAR(256), comment='获取未读消息URL')
    is_builtin = Column(NUMBER(asdecimal=False), comment='是否内置')
    is_enable = Column(NUMBER(asdecimal=False), comment='是否启用')
    bz = Column(NVARCHAR(255), comment='描述')
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
    detail_param_config = Column(NVARCHAR(255), comment='详细参数配置')
    config_mark = Column(NVARCHAR(64), comment='对接配置标识')


class MessageSendRecdUClassify(Base):
    __tablename__ = 'message_send_recd_u_classify'
    __table_args__ = {'comment': '消息发送类型表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    message_send_record_id = Column(VARCHAR(36), comment='消息调用记录表ID')
    abutment_config_id = Column(VARCHAR(36), comment='消息对接配置ID')
    abutment_config_name = Column(NVARCHAR(64), comment='消息对接配置名称')
    i_ok = Column(NUMBER(asdecimal=False), comment='是否发送成功')
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
    error_info = Column(NVARCHAR(1024), comment='发送失败原因')


t_message_send_recd_user = Table(
    'message_send_recd_user', metadata,
    Column('id', VARCHAR(36), comment='主键ID'),
    Column('index_code', NUMBER(asdecimal=False), comment='排序序号'),
    Column('create_worker', VARCHAR(36), comment='创建人'),
    Column('create_time', DateTime, comment='创建时间'),
    Column('latest_modify_worker', VARCHAR(36), comment='最后修改人'),
    Column('latest_modify_time', DateTime, comment='最后修改时间'),
    Column('isvalid', NUMBER(asdecimal=False), comment='是否合法'),
    Column('bz1', NVARCHAR(255), comment='备注1'),
    Column('bz2', NVARCHAR(255), comment='备注2'),
    Column('bz3', NVARCHAR(255), comment='备注3'),
    Column('bz4', NVARCHAR(255), comment='备注4'),
    Column('receive_user_name', NVARCHAR(64), comment='接收人姓名'),
    Column('receive_user_id', VARCHAR(36), comment='接收人ID'),
    Column('message_send_record_id', VARCHAR(36), comment='消息发送记录表ID'),
    comment='消息接收人表'
)


class MessageSendRecord(Base):
    __tablename__ = 'message_send_record'
    __table_args__ = {'comment': '消息调用记录表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    send_user_id = Column(NVARCHAR(36), comment='发送人ID')
    message_body = Column(Text, comment='消息内容')
    send_time = Column(DateTime, comment='发送时间')
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
    send_user_name = Column(NVARCHAR(64), comment='发送人姓名')
    send_type = Column(NVARCHAR(64), comment='发送类型')


class MessageTemplate(Base):
    __tablename__ = 'message_template'
    __table_args__ = {'comment': '业务通用模块-消息模板'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    to_system = Column(NVARCHAR(64), comment='所属系统')
    template_name = Column(NVARCHAR(64), comment='模板名称')
    template_body = Column(NVARCHAR(1024), comment='模板主体')
    bz = Column(NVARCHAR(255), comment='备注')
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
    is_enable = Column(NUMBER(asdecimal=False), comment='是否启用')


class NewsAttachment(Base):
    __tablename__ = 'news_attachment'
    __table_args__ = {'comment': '新闻附件表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    news_id = Column(VARCHAR(36), comment='新闻纪录ID')
    file_name = Column(NVARCHAR(50), comment='附件名称')
    file_format = Column(VARCHAR(10), comment='附件格式(带.)')
    file_size = Column(NUMBER(asdecimal=False), comment='附件大小')
    file_type = Column(Integer, comment='附件类型(1：新闻图片 2：新闻附件 3：新闻内容附件)')
    isvalid = Column(Integer, comment='是否合法')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(VARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')


class NewsAttachmentContent(Base):
    __tablename__ = 'news_attachment_content'
    __table_args__ = {'comment': '新闻附件内容表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    news_attachment_id = Column(VARCHAR(36), comment='新闻附件ID')
    file_buffer = Column(LargeBinary, comment='附件内容')
    isvalid = Column(Integer, comment='是否合法')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(VARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')


class NewsClas(Base):
    __tablename__ = 'news_class'
    __table_args__ = {'comment': '新闻分类表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    parent_id = Column(VARCHAR(36), comment='父分类ID')
    class_name = Column(NVARCHAR(100), comment='分类名称')
    is_need_audit = Column(Integer, comment='是否需要审核(0：不审核 1：审核,)')
    publish_right = Column(Integer, comment='发布权限(10：公开,20：指定部门或者人员)')
    index_code = Column(Integer, comment='排序号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(VARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    read_right = Column(Integer, comment='阅读权限(10：公开,20：指定部门或者人员)')
    isvalid = Column(Integer, comment='是否合法')
    admin_right = Column(Integer, comment='管理权限(10：公开,20：指定部门或者人员)')
    class_mark = Column(NVARCHAR(255), unique=True, comment='分类标识')


class NewsClassAuthority(Base):
    __tablename__ = 'news_class_authority'
    __table_args__ = {'comment': '新闻分类权限表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    class_id = Column(VARCHAR(36), index=True, comment='分类ID')
    target_id = Column(VARCHAR(36), comment='目标ID(人员ID或部门ID)')
    target_type = Column(Integer, comment='目标类型(10：部门,20：人员)')
    right_type = Column(Integer, comment='权限类型(10：阅读,20：发布,30：管理)')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(VARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否合法')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    target_name = Column(NVARCHAR(50), comment='目标名称(人员名称或部门名称)')


t_news_read_log = Table(
    'news_read_log', metadata,
    Column('id', VARCHAR(36), nullable=False, comment='主键ID'),
    Column('news_id', VARCHAR(36), comment='新闻纪录ID'),
    Column('read_time', DateTime, comment='阅读日期'),
    Column('read_worker_name', NVARCHAR(50), comment='阅读人员姓名'),
    Column('read_dept_id', VARCHAR(72), comment='阅读人所在部门ID'),
    Column('read_dept_name', NVARCHAR(100), comment='阅读人所在部门名称'),
    Column('isvalid', Integer, comment='是否合法'),
    Column('create_worker', VARCHAR(36), comment='创建人'),
    Column('create_time', DateTime, comment='创建时间'),
    Column('latest_modify_worker', VARCHAR(36), comment='最后修改人'),
    Column('latest_modify_time', DateTime, comment='最后修改时间'),
    Column('bz1', NVARCHAR(255), comment='备注1'),
    Column('bz2', NVARCHAR(255), comment='备注2'),
    Column('bz3', NVARCHAR(255), comment='备注3'),
    Column('bz4', NVARCHAR(255), comment='备注4'),
    comment='新闻阅读日志表'
)


class NewsRecord(Base):
    __tablename__ = 'news_record'
    __table_args__ = {'comment': '新闻记录表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    title = Column(NVARCHAR(200), comment='新闻标题')
    subtitle = Column(NVARCHAR(100), comment='新闻副标题')
    keyword = Column(NVARCHAR(100), comment='新闻关键字')
    class_id = Column(VARCHAR(36), comment='分类ID')
    class_name = Column(NVARCHAR(64), comment='分类名称')
    is_stick = Column(Integer, comment='是否置顶(0：不置顶,1：置顶)')
    stick_time_unit = Column(VARCHAR(10), comment='置顶时间单位(分钟：MM,小时：HH,工作日（天）：WDAY,自然日（天）：NDAY)')
    stick_time_value = Column(NUMBER(asdecimal=False), comment='置顶时间数值')
    stick_end_time = Column(DateTime, comment='置顶结束日期')
    is_download_attach = Column(Integer, comment='是否直接下载附件(0：否,1：是)')
    is_need_audit = Column(Integer, comment='是否需要审核(0：否,1：是)')
    record_state = Column(Integer, comment='新闻记录状态(0：草稿,1：待审核,2：已发布,3：未通过)')
    is_allow_publish = Column(Integer, comment='是否允许发布(0：否,1：是)')
    is_scroll_picture = Column(Integer, comment='是否滚动图片(0：否,1：是)')
    is_show = Column(Integer, comment='是否显示新闻(0：否,1：是)')
    read_count = Column(Integer, comment='阅读量')
    create_worker_id = Column(VARCHAR(36), comment='发布人ID')
    create_worker_name = Column(NVARCHAR(50), comment='发布人姓名')
    create_dept_id = Column(VARCHAR(255), comment='发布人所在部门ID')
    create_dept_name = Column(NVARCHAR(255), comment='发布人所在部门名称')
    publish_date = Column(DateTime, comment='发布日期')
    latest_modify_worker_id = Column(VARCHAR(36), comment='修改人ID')
    create_time = Column(DateTime, comment='创建日期')
    latest_modify_time = Column(DateTime, comment='修改日期')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否合法')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    instance_id = Column(VARCHAR(36), comment='流程实例ID')


class NewsRecordContent(Base):
    __tablename__ = 'news_record_content'
    __table_args__ = {'comment': '新闻纪录内容表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    news_id = Column(VARCHAR(36), comment='新闻纪录ID')
    news_content = Column(Text, comment='新闻内容')
    isvalid = Column(Integer, comment='是否合法')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(VARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')


t_obsolete_num_recycling = Table(
    'obsolete_num_recycling', metadata,
    Column('id', VARCHAR(36), nullable=False, comment='主键ID'),
    Column('code_template_id', VARCHAR(36), comment='编码模板ID'),
    Column('code_number', NVARCHAR(64), comment='编号'),
    Column('index_code', NUMBER(asdecimal=False), comment='排序序号'),
    Column('create_worker', VARCHAR(36), comment='创建人'),
    Column('create_time', DateTime, comment='创建时间'),
    Column('latest_modify_worker', VARCHAR(36), comment='最后修改人'),
    Column('latest_modify_time', DateTime, comment='最后修改时间'),
    Column('isvalid', NUMBER(asdecimal=False), comment='是否合法'),
    Column('bz1', NVARCHAR(255), comment='备注1'),
    Column('bz2', NVARCHAR(255), comment='备注2'),
    Column('bz3', NVARCHAR(255), comment='备注3'),
    Column('bz4', NVARCHAR(255), comment='备注4'),
    Column('classify', NVARCHAR(128), comment='编码的类型'),
    comment='作废编号回收再利用表'
)


class Report(Base):
    __tablename__ = 'report'
    __table_args__ = {'comment': '报表设计'}

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
    name = Column(VARCHAR(128), comment='报表名称')
    bz = Column(VARCHAR(1024), comment='备注')
    report_catalog_id = Column(VARCHAR(36), comment='目录ID')
    datasource_url = Column(NVARCHAR(255), comment='数据源URL')
    report_mark = Column(VARCHAR(64), comment='报表标识')


class ReportCatalog(Base):
    __tablename__ = 'report_catalog'
    __table_args__ = {'comment': '图层仓库管理'}

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
    parent_id = Column(VARCHAR(36), comment='父级ID')
    name = Column(VARCHAR(64), comment='目录名称')


class ReportContent(Base):
    __tablename__ = 'report_content'
    __table_args__ = {'comment': '报表设计内容'}

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
    content = Column(LargeBinary, comment='内容')
    report_id = Column(VARCHAR(36), comment='报表外键ID')


class ReportDataConnection(Base):
    __tablename__ = 'report_data_connection'
    __table_args__ = {'comment': '报表数据源'}

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
    name = Column(NVARCHAR(64), comment='连接名称')
    connection_driver = Column(NVARCHAR(512), comment='数据库实例')
    connection_url = Column(NVARCHAR(512), comment='数据库URL')
    connection_username = Column(NVARCHAR(512), comment='数据库用户名')
    connection_password = Column(NVARCHAR(512), comment='数据库密码')
    connection_identity = Column(NVARCHAR(512), comment='登陆身份')


class ReportDatasource(Base):
    __tablename__ = 'report_datasource'
    __table_args__ = {'comment': '报表数据源'}

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
    sql = Column(LargeBinary, comment='SQL语句')
    report_id = Column(VARCHAR(36), comment='关联报表ID')
    name = Column(NVARCHAR(64), comment='数据源名称')
    report_data_connection_id = Column(VARCHAR(36), comment='数据库连接外键ID,为空则为该系统连接')


class SmsRecord(Base):
    __tablename__ = 'sms_record'
    __table_args__ = {'comment': '短信发送'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    send_user_id = Column(VARCHAR(36), comment='发送人员ID')
    send_user_name = Column(NVARCHAR(64), comment='发送人员姓名')
    message_body = Column(NVARCHAR(512), comment='消息内容')
    send_time = Column(DateTime, comment='发送时间')
    send_state = Column(NUMBER(asdecimal=False), comment='发送状态  10,发送失败 20,发送成功 30,定时发送   ')
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


t_sms_record_user = Table(
    'sms_record_user', metadata,
    Column('id', VARCHAR(36), comment='主键ID'),
    Column('sms_record_id', VARCHAR(36), comment='SMS_RECORD表ID'),
    Column('receive_user_id', VARCHAR(36), comment='接收人ID'),
    Column('receive_user_name', NVARCHAR(64), comment='接收人姓名'),
    Column('index_code', NUMBER(asdecimal=False), comment='排序序号'),
    Column('create_worker', VARCHAR(36), comment='创建人'),
    Column('create_time', DateTime, comment='创建时间'),
    Column('latest_modify_worker', VARCHAR(36), comment='最后修改人'),
    Column('latest_modify_time', DateTime, comment='最后修改时间'),
    Column('isvalid', NUMBER(asdecimal=False), comment='是否合法'),
    Column('bz1', NVARCHAR(255), comment='备注1'),
    Column('bz2', NVARCHAR(255), comment='备注2'),
    Column('bz3', NVARCHAR(255), comment='备注3'),
    Column('bz4', NVARCHAR(255), comment='备注4'),
    Column('receive_user_phone', NVARCHAR(16), comment='接收人手机号'),
    Column('i_ok', NUMBER(asdecimal=False), comment='是否成功'),
    Column('error_info', NVARCHAR(1024), comment='失败原因')
)


class Workday(Base):
    __tablename__ = 'workday'
    __table_args__ = {'comment': '业务通用模块-工作日'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    to_filiale = Column(NVARCHAR(64), comment='分公司')
    day_date = Column(DateTime, comment='日期')
    is_workday = Column(NUMBER(asdecimal=False), comment='是否工作日')
    holiday_remark = Column(NVARCHAR(64), comment='节假日备注')
    am_starttime = Column(DateTime, comment='上午上班时间')
    am_finishtime = Column(DateTime, comment='上午下班时间')
    pm_starttime = Column(DateTime, comment='下午上班时间')
    pm_finishtime = Column(DateTime, comment='下午下班时间')
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
