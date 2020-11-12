# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, LargeBinary, NVARCHAR, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Feedback(Base):
    __tablename__ = 'feedback'
    __table_args__ = {'comment': '意见表'}

    id = Column(NVARCHAR(36), primary_key=True, comment='意见表ID')
    belong_system = Column(NVARCHAR(32), comment='所属系统')
    type = Column(NVARCHAR(32), comment='问题类别')
    url = Column(NVARCHAR(2000), comment='页面地址')
    title = Column(NVARCHAR(1024), comment='反馈标题')
    content = Column(NVARCHAR(2000), comment='反馈内容')
    feedback_worker_ip = Column(NVARCHAR(16), comment='反馈人ip地址')
    feedback_worker_id = Column(NVARCHAR(36), comment='反馈人ID')
    feedback_login_name = Column(NVARCHAR(64), comment='反馈人用户名')
    feedback_worker_name = Column(NVARCHAR(64), comment='反馈人姓名')
    feedback_time = Column(DateTime, comment='反馈时间')
    ideal = Column(Integer, comment='已处理标识 ')
    deal_person = Column(NVARCHAR(32), comment='责任人')
    deal_time = Column(DateTime, comment='处理时间')
    opinion = Column(NVARCHAR(2000), comment='处理意见 ')
    create_worker = Column(NVARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(Integer, comment='是否合法')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    num = Column(NVARCHAR(64), comment='意见编号')
    propose = Column(NVARCHAR(2000), comment='改进型建议')
    flowstate = Column(Integer, comment='流程状态')
    complete_time = Column(DateTime, comment='流程办结时间')
    instance_id = Column(NVARCHAR(36), comment='流程实例ID')
    solution = Column(NVARCHAR(64), comment='解决方案')


class FeedbackPic(Base):
    __tablename__ = 'feedback_pic'
    __table_args__ = {'comment': '意见反馈图片表表'}

    id = Column(NVARCHAR(36), primary_key=True, comment='意见反馈图片表ID')
    feedback_id = Column(NVARCHAR(36), comment='反馈ID')
    title = Column(NVARCHAR(32), comment='图片标题')
    stream = Column(LargeBinary, comment='图片流')
    type = Column(NVARCHAR(16), comment='类型')
    create_worker = Column(NVARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(Integer, comment='是否合法')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')


class GovernmentCloudCalendar(Base):
    __tablename__ = 'government_cloud_calendar'
    __table_args__ = {'comment': '政务云日程表'}

    id = Column(VARCHAR(36), primary_key=True, comment='日程ID')
    calendar_name = Column(NVARCHAR(1024), comment='日程名称')
    calendar_content = Column(NVARCHAR(1024), comment='日程内容')
    calendar_time = Column(DateTime, comment='日程发生时间')
    index_code = Column(Integer, comment='排序编号')
    create_worker = Column(NVARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(NVARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(Integer, comment='是否合法')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')


class IndexLayout(Base):
    __tablename__ = 'index_layout'
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
    width_pect = Column(NUMBER(4, 0, False), comment='宽度占比')
    theme_id = Column(VARCHAR(36), comment='所属主题，这里存的是菜单ID')


class IndexModule(Base):
    __tablename__ = 'index_module'
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
    index_layout_id = Column(VARCHAR(36), comment='所属布局ID')
    name = Column(NVARCHAR(64), comment='模块名称')
    type = Column(NUMBER(1, 0, False), comment='模块类型 1-色块 2-小部件')
    background_color = Column(NVARCHAR(16), comment='背景色')
    background_image = Column(NVARCHAR(128), comment='背景图URL')
    menu_id = Column(VARCHAR(36), comment='菜单ID')
    width_pec = Column(NUMBER(4, 0, False), comment='宽度百分比')
    height_pec = Column(NUMBER(4, 0, False), comment='高度百分比')


t_index_screen_module = Table(
    'index_screen_module', metadata,
    Column('id', VARCHAR(36), nullable=False, comment='主键ID'),
    Column('name', NVARCHAR(64), comment='模块名称'),
    Column('menu_id', VARCHAR(36), comment='菜单ID'),
    Column('background_color', NVARCHAR(12), comment='模块背景色'),
    Column('position', NUMBER(asdecimal=False), comment='模块位置'),
    Column('i_enable', NUMBER(asdecimal=False), comment='是否启用'),
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
    Column('screen_id', VARCHAR(36), comment='屏幕ID'),
    comment='首页屏幕模块管理表'
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
    menu_mark = Column(NVARCHAR(255), comment='菜单标识')
    app_id = Column(NVARCHAR(255), comment='APP标识')


class LayoutRelDepartment(Base):
    __tablename__ = 'layout_rel_department'
    __table_args__ = {'comment': '布局-部门关联表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    layout_id = Column(VARCHAR(36), comment='布局模板id')
    department_id = Column(VARCHAR(36), comment='部门ID')
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


class LayoutRelPosition(Base):
    __tablename__ = 'layout_rel_position'
    __table_args__ = {'comment': '布局-部门职位关联表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    layout_id = Column(VARCHAR(36), comment='布局ID')
    position_id = Column(VARCHAR(36), comment='职位ID')
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


class LayoutRelRole(Base):
    __tablename__ = 'layout_rel_role'
    __table_args__ = {'comment': '布局-角色关联表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    layout_id = Column(VARCHAR(36), comment='布局模板ID')
    role_id = Column(VARCHAR(36), comment='角色ID')
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


class LayoutTemplate(Base):
    __tablename__ = 'layout_template'
    __table_args__ = {'comment': '首页布局模板管理'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    name = Column(NVARCHAR(64), comment='模板名称')
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


class Menu(Base):
    __tablename__ = 'menu'
    __table_args__ = {'comment': '菜单管理'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    name = Column(NVARCHAR(64), comment='菜单名称')
    open_type = Column(NUMBER(asdecimal=False), comment='打开方式 10,容器自带头部标签  20,弹出并全屏显示 30,弹出新窗口')
    web_url = Column(NVARCHAR(2000), comment='菜单URL(PC端)')
    corner_font_url = Column(NVARCHAR(2000), comment='角标文字URL')
    icon_font_url = Column(NVARCHAR(2000), comment='菜单图标URL')
    app_url = Column(NVARCHAR(2000), comment='手机端URL')
    click_service = Column(NVARCHAR(2000), comment='菜单点击执行服务')
    pid = Column(VARCHAR(36), comment='父菜单ID')
    controller_action_url = Column(NVARCHAR(2000), comment='菜单Controller_Action地址')
    system_identity = Column(NVARCHAR(64), comment='系统标识')
    bz = Column(NVARCHAR(256), comment='备注')
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
    position = Column(NVARCHAR(64), comment='菜单位置')
    whether_fast_mode = Column(NUMBER(asdecimal=False), comment='是否是快捷菜单')
    base_menu_id = Column(VARCHAR(36), comment='源头id')
    preposition_js = Column(Text, comment='前置js')
    func_type = Column(VARCHAR(40), nullable=False, server_default=text("'PresetJS' "), comment='前置JS类型')
    func_value = Column(VARCHAR(40))


class SoftDownload(Base):
    __tablename__ = 'soft_download'
    __table_args__ = {'comment': '软件下载管理'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    name = Column(NVARCHAR(128), comment='软件名称')
    app_size = Column(NUMBER(asdecimal=False), comment='软件大小(MB)')
    icon_url = Column(NVARCHAR(2000), comment='软件图标地址')
    app_url = Column(NVARCHAR(2000), comment='软件下载地址')
    verson_no = Column(VARCHAR(32), comment='版本号')
    update_date = Column(DateTime, comment='更新日期')
    support_sys = Column(NVARCHAR(64), comment='支持系统')
    bz = Column(NVARCHAR(2000), comment='功能简介')
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


class UpdateLog(Base):
    __tablename__ = 'update_logs'
    __table_args__ = {'comment': '更新日志'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    up_date = Column(DateTime, comment='更新时间')
    content = Column(NVARCHAR(2000), comment='更新内容')
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


class WidgetsConfig(Base):
    __tablename__ = 'widgets_config'
    __table_args__ = {'comment': '小部件配置'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    template_id = Column(VARCHAR(36), comment='模板ID')
    name = Column(VARCHAR(64), comment='名称')
    height = Column(NUMBER(asdecimal=False), comment='高度')
    height_unit = Column(NUMBER(asdecimal=False), comment='高度单位 10:px 20:%')
    width = Column(NUMBER(asdecimal=False), comment='宽度  单位默认%')
    url = Column(NVARCHAR(256), comment='url')
    is_custom = Column(NUMBER(asdecimal=False), comment='是否自定义 0:否（默认） 1,是')
    is_scroll = Column(NUMBER(asdecimal=False), comment='是否开启滚动条  0:否（默认） 1,是')
    is_showheader = Column(NUMBER(asdecimal=False), comment='是否显示头部  0:否（默认） 1,是')
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


class WidgetsCustom(Base):
    __tablename__ = 'widgets_custom'
    __table_args__ = {'comment': '小部件-自定义'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    widgets_config_id = Column(VARCHAR(36), comment='小部件ID')
    ftl_content = Column(Text, comment='ftl模板文件内容')
    css_contetn = Column(Text, comment='css样式文件内容')
    js_content = Column(Text, comment='js脚本文件内容')
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


class Win10IndexScreen(Base):
    __tablename__ = 'win10_index_screen'
    __table_args__ = {'comment': '首页屏幕管理表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    name = Column(NVARCHAR(64), comment='屏幕名称')
    background_image = Column(NVARCHAR(128), comment='屏幕背景图')
    background_color = Column(NVARCHAR(12), comment='屏幕背景色')
    i_enable = Column(NUMBER(asdecimal=False), comment='是否启用')
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


class Win10IndexScreenModule(Base):
    __tablename__ = 'win10_index_screen_module'
    __table_args__ = {'comment': '首页屏幕模块管理表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    name = Column(NVARCHAR(64), comment='模块名称')
    menu_id = Column(VARCHAR(36), comment='菜单ID')
    background_color = Column(NVARCHAR(12), comment='模块背景色')
    position = Column(NUMBER(asdecimal=False), comment='模块位置')
    i_enable = Column(NUMBER(asdecimal=False), comment='是否启用')
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
    screen_id = Column(VARCHAR(36), comment='屏幕ID')
