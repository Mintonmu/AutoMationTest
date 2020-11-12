# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, NVARCHAR, Table, Text, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class DEPARTMENTCopy(Base):
    __tablename__ = 'DEPARTMENT_copy'
    __table_args__ = {'comment': '部门表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    name = Column(NVARCHAR(64), comment='部门名称')
    simple_name = Column(NVARCHAR(64), comment='部门简称')
    dept_code = Column(VARCHAR(64), comment='部门编码')
    address = Column(NVARCHAR(64), comment='地址')
    telephone = Column(VARCHAR(32), comment='电话')
    fax = Column(VARCHAR(32), comment='传真')
    pid = Column(VARCHAR(36), index=True, comment='上级部门ID')
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



class Branche(Base):
    __tablename__ = 'branche'
    __table_args__ = {'comment': '分支机构表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    name = Column(VARCHAR(255), comment='分支机构名称')
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


class Department(Base):
    __tablename__ = 'department'
    __table_args__ = {'comment': '部门表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    name = Column(NVARCHAR(64), comment='部门名称')
    simple_name = Column(NVARCHAR(64), comment='部门简称')
    dept_code = Column(VARCHAR(64), comment='部门编码')
    address = Column(NVARCHAR(64), comment='地址')
    telephone = Column(VARCHAR(32), comment='电话')
    fax = Column(VARCHAR(32), comment='传真')
    pid = Column(VARCHAR(36), index=True, comment='上级部门ID')
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


class DeptRelBranche(Base):
    __tablename__ = 'dept_rel_branche'
    __table_args__ = {'comment': '部门与分支机构关系表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    department_id = Column(VARCHAR(36), comment='部门ID')
    branche_id = Column(VARCHAR(36), comment='分支机构ID')
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


class DeptRelLeader(Base):
    __tablename__ = 'dept_rel_leader'
    __table_args__ = {'comment': '领导部门关联表（分管部门配置）'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    user_id = Column(VARCHAR(36), comment='人员id')
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


class DeptRelUser(Base):
    __tablename__ = 'dept_rel_user'
    __table_args__ = {'comment': '用户部门关系表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    user_id = Column(VARCHAR(36), comment='用户ID')
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


class District(Base):
    __tablename__ = 'district'
    __table_args__ = {'comment': '行政区划表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    city_code = Column(VARCHAR(4), index=True, comment='地市代码')
    city_name = Column(NVARCHAR(64), comment='地市名称')
    county_code = Column(VARCHAR(2), comment='区县代码')
    county_name = Column(NVARCHAR(64), comment='区县名称')
    town_code = Column(VARCHAR(3), comment='乡镇代码')
    town_name = Column(NVARCHAR(64), comment='乡镇名称')
    village_code = Column(VARCHAR(3), comment='村代码')
    village_name = Column(NVARCHAR(64), comment='村名称')
    group_code = Column(VARCHAR(2), comment='组代码')
    group_name = Column(NVARCHAR(64), comment='组名称')
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
    full_code = Column(VARCHAR(14), index=True, comment='完整代码')


t_gh_rel_user = Table(
    'gh_rel_user', metadata,
    Column('z_user_org_right_id', VARCHAR(255)),
    Column('z_user_org_right_name', VARCHAR(255)),
    Column('所属部门名称', VARCHAR(255)),
    Column('userid', VARCHAR(255)),
    Column('username', VARCHAR(255)),
    Column('password', VARCHAR(255)),
    Column('passwordsalt', VARCHAR(255)),
    Column('displayname', VARCHAR(255)),
    Column('shortname', VARCHAR(255)),
    Column('usertype', VARCHAR(255)),
    Column('createtime', VARCHAR(255)),
    Column('description', VARCHAR(255)),
    Column('isconfirmed', VARCHAR(255)),
    Column('confirmationtoken', VARCHAR(255)),
    Column('islockedout', VARCHAR(255)),
    Column('email', VARCHAR(255)),
    Column('nickname', VARCHAR(255)),
    Column('weight', VARCHAR(255)),
    Column('iconid', VARCHAR(255)),
    Column('zwpass', VARCHAR(255)),
    Column('sindex', VARCHAR(255)),
    Column('wechatid', VARCHAR(255))
)


class GroupBelongtoUser(Base):
    __tablename__ = 'group_belongto_user'
    __table_args__ = {'comment': '群组所属用户表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    belongto_user_id = Column(VARCHAR(36), comment='所属用户ID')
    group_id = Column(VARCHAR(36), comment='分组ID')
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
    i_creator = Column(NUMBER(asdecimal=False), comment='是否创建人（1：是 0：否）')
    group_authority = Column(NUMBER(asdecimal=False), comment='群组权限（1：可编辑 0：只读）')


class KeyValue(Base):
    __tablename__ = 'key_value'
    __table_args__ = {'comment': 'key-value字典表'}

    id = Column(VARCHAR(50), primary_key=True, comment='主键ID')
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


class Leader(Base):
    __tablename__ = 'leader'

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    user_id = Column(VARCHAR(36), comment='人员ID')
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


class LoginPage(Base):
    __tablename__ = 'login_page'

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    name = Column(NVARCHAR(64), comment='页面名称')
    redirecturl_app = Column(NVARCHAR(256), comment='移动端登录跳转地址')
    externalurl_app = Column(NVARCHAR(256), comment='移动端页面外部地址')
    redirecturl_web = Column(NVARCHAR(256), comment='WEB端登录跳转地址')
    externalurl_web = Column(NVARCHAR(256), comment='WEB端页面外部地址')
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
    i_enable = Column(NUMBER(asdecimal=False), comment='是否启用  1启用（默认） 2禁用')
    page_mark = Column(NVARCHAR(64), comment='页面标识')
    i_ca = Column(NUMBER(asdecimal=False), comment='是否CA登录')


class LoginPageHtml(Base):
    __tablename__ = 'login_page_html'
    __table_args__ = {'comment': '登录页HTML'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    web_html = Column(Text, comment='WEB端HTML')
    app_html = Column(Text, comment='APP端HTML')
    index_code = Column(NUMBER(asdecimal=False), comment='排序序号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(VARCHAR(36), comment='最后修改人\x13')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否合法')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')
    login_page_id = Column(VARCHAR(36), index=True, comment='登录页Id')


class ObjectPromisstion(Base):
    __tablename__ = 'object_promisstion'
    __table_args__ = {'comment': '对象权限'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    object_type = Column(NVARCHAR(64), comment='对象类型 如：角色/部门/职位')
    object_value = Column(VARCHAR(36), comment='对象值  如：管理员/财务部/部门经理 的ID')
    promisstion_type = Column(NVARCHAR(64), comment='权限类型（公司名.系统名.模块名）  例：ZJUGIS.WORKFLOW.TEMPLATE')
    promisstion_value = Column(VARCHAR(36), comment='权限值（ID）  如：流程模板ID(36位标识符)')
    p_promisstion_vaule = Column(VARCHAR(36), comment='父权限值（ID）如：流程模板ID(36位标识符)')
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


class OrgChangeLog(Base):
    __tablename__ = 'org_change_log'
    __table_args__ = {'comment': '组织架构操作日志（变更记录）'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    classify = Column(NUMBER(asdecimal=False), comment='变更类型 如：12：新增部门;1：人员新增;4：人员编辑;9：新增职位等')
    content = Column(NVARCHAR(256), comment='操作内容')
    op_date = Column(DateTime, comment='操作时间')
    user_name = Column(VARCHAR(64), comment='登录名')
    user_id = Column(VARCHAR(36), comment='操作人员ID')
    real_name = Column(NVARCHAR(64), comment='操作人员姓名')
    ip = Column(VARCHAR(16), comment='操作人登录IP地址')
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
    isok_num = Column(VARCHAR(10), comment='完成同步数量 （6/6）')


class Position(Base):
    __tablename__ = 'position'
    __table_args__ = {'comment': '职位表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    name = Column(NVARCHAR(64), comment='名称')
    p_department_id = Column(VARCHAR(36), comment='父级部门ID')
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
    code = Column(NVARCHAR(64), comment='编码')
    type = Column(NUMBER(asdecimal=False), comment='职位类型  0 普通职位 10负责人职位')


class Role(Base):
    __tablename__ = 'role'
    __table_args__ = {'comment': '角色表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    name = Column(NVARCHAR(64), comment='角色名')
    classify = Column(NVARCHAR(64), comment='角色类型')
    i_default = Column(NUMBER(asdecimal=False), comment='是否默认角色   0：否  1：是')
    index_code = Column(NUMBER(asdecimal=False), comment='排序序号')
    create_worker = Column(VARCHAR(36), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    latest_modify_worker = Column(VARCHAR(36), comment='最后修改人')
    latest_modify_time = Column(DateTime, comment='最后修改时间')
    isvalid = Column(NUMBER(asdecimal=False), comment='是否合法')
    bz = Column(NVARCHAR(255), comment='备注')
    bz1 = Column(NVARCHAR(255), comment='备注1')
    bz2 = Column(NVARCHAR(255), comment='备注2')
    bz3 = Column(NVARCHAR(255), comment='备注3')
    bz4 = Column(NVARCHAR(255), comment='备注4')


class RoleRelUser(Base):
    __tablename__ = 'role_rel_user'
    __table_args__ = {'comment': '用户角色关系表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    user_id = Column(VARCHAR(36), comment='用户ID')
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


class SsoService(Base):
    __tablename__ = 'sso_service'
    __table_args__ = {'comment': '单点登录管理'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    system_name = Column(NVARCHAR(64), comment='系统名称')
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


class SyncLog(Base):
    __tablename__ = 'sync_log'
    __table_args__ = {'comment': '组织架构同步日志表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    change_id = Column(VARCHAR(36), comment='变更日志ID')
    i_ok = Column(NUMBER(asdecimal=False), comment='是否同步成功 1成功  0失败')
    errorinfo = Column(NVARCHAR(500), comment='报错信息')
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


class SyncService(Base):
    __tablename__ = 'sync_service'
    __table_args__ = {'comment': '用户推送管理'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    website_name = Column(NVARCHAR(64), comment='站点名称')
    service_url = Column(VARCHAR(256), comment='服务地址')
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
    i_enable = Column(NUMBER(asdecimal=False), comment='是否启用 1启用（默认）  0禁用')


class ThirdParty(Base):
    __tablename__ = 'third_party'

    id = Column(VARCHAR(36), primary_key=True)
    third_party_name = Column(VARCHAR(255))
    index_code = Column(NUMBER(asdecimal=False))
    create_worker = Column(VARCHAR(36))
    create_time = Column(DateTime)
    latest_modify_worker = Column(VARCHAR(255))
    latest_modify_time = Column(DateTime)
    isvalid = Column(NUMBER(asdecimal=False))
    bz1 = Column(NVARCHAR(255))
    bz2 = Column(NVARCHAR(255))
    bz3 = Column(NVARCHAR(255))
    bz4 = Column(NVARCHAR(255))
    bz = Column(NVARCHAR(255))


class ThirdPartyLinkWorker(Base):
    __tablename__ = 'third_party_link_worker'
    __table_args__ = {'comment': '第三方系统关联用户'}

    id = Column(VARCHAR(36), primary_key=True, comment='关联id')
    third_party_id = Column(NVARCHAR(512), comment='第三方系统id')
    worker_id = Column(NVARCHAR(36), comment='人员id')
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
    third_party_name = Column(NVARCHAR(512), comment='第三方系统名称')


class UserBelongtoGroup(Base):
    __tablename__ = 'user_belongto_group'
    __table_args__ = {'comment': '群组下属用户表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    user_id = Column(VARCHAR(36), comment='人员ID')
    belongto_group_id = Column(VARCHAR(36), comment='所属群组ID')
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


t_user_import = Table(
    'user_import', metadata,
    Column('姓名', VARCHAR(255)),
    Column('登录名称', VARCHAR(255)),
    Column('密码', VARCHAR(255)),
    Column('姓名拼音', VARCHAR(255)),
    Column('性别', VARCHAR(255)),
    Column('电子邮箱', VARCHAR(255)),
    Column('电话', VARCHAR(255)),
    Column('手机', VARCHAR(255)),
    Column('身份证', VARCHAR(255)),
    Column('人员状态', VARCHAR(255))
)


class UserLink(Base):
    __tablename__ = 'user_link'
    __table_args__ = {'comment': '用户第三方对接'}

    user_id = Column(VARCHAR(36), primary_key=True, comment='用户ID')
    third_user_id = Column(NVARCHAR(64), index=True, comment='第三方用户ID')
    third_type = Column(NVARCHAR(36), index=True, comment='第三方类型 钉钉-dd 微信-wx 等等')


class UserRelDistrict(Base):
    __tablename__ = 'user_rel_district'
    __table_args__ = {'comment': '用户行政区关系表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    user_id = Column(VARCHAR(36), nullable=False, comment='用户ID')
    district_id = Column(VARCHAR(36), nullable=False, comment='行政区划ID')
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


class UserRelPosition(Base):
    __tablename__ = 'user_rel_position'
    __table_args__ = {'comment': '人员职位关联表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    user_id = Column(VARCHAR(36), comment='人员ID')
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


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'comment': '用户表'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键ID')
    login_name = Column(NVARCHAR(64), comment='登录名')
    real_name = Column(NVARCHAR(64), comment='真实姓名')
    pinyin_name = Column(VARCHAR(64), comment='姓名拼音')
    password = Column(VARCHAR(64), comment='密码')
    sex = Column(NUMBER(asdecimal=False), comment='性别  1：男  2：女')
    email = Column(VARCHAR(64), comment='电子邮件')
    telephone = Column(VARCHAR(32), comment='固定电话')
    mobilephone = Column(VARCHAR(32), comment='手机')
    id_card = Column(VARCHAR(32), comment='身份证')
    worker_state = Column(NUMBER(asdecimal=False), comment='人员状态   10：正常;   20：离职 ;  99：退休;     默认正常 ')
    worker_type = Column(NUMBER(asdecimal=False), comment='人员类型   10：普通用户 20：超级管理员 30：管理员')
    extend1 = Column(NVARCHAR(255), comment='扩展字段1')
    extend2 = Column(NVARCHAR(255), comment='扩展字段2')
    extend3 = Column(NVARCHAR(255), comment='扩展字段3')
    extend4 = Column(NVARCHAR(255), comment='扩展字段4')
    e_signature = Column(NVARCHAR(256), comment='电子签名  文件URL')
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
    is_leader = Column(NUMBER(asdecimal=False), comment='是否领导  （分管领导配置） 0否（默认） 1是')
    ca_key = Column(VARCHAR(64))
    worker_level = Column(NUMBER(asdecimal=False), comment='人员级别')


t_users0814 = Table(
    'users0814', metadata,
    Column('id', VARCHAR(36), nullable=False),
    Column('login_name', NVARCHAR(64)),
    Column('real_name', NVARCHAR(64)),
    Column('pinyin_name', VARCHAR(64)),
    Column('password', VARCHAR(64)),
    Column('sex', NUMBER(asdecimal=False)),
    Column('email', VARCHAR(64)),
    Column('telephone', VARCHAR(32)),
    Column('mobilephone', VARCHAR(32)),
    Column('id_card', VARCHAR(32)),
    Column('worker_state', NUMBER(asdecimal=False)),
    Column('worker_type', NUMBER(asdecimal=False)),
    Column('extend1', NVARCHAR(255)),
    Column('extend2', NVARCHAR(255)),
    Column('extend3', NVARCHAR(255)),
    Column('extend4', NVARCHAR(255)),
    Column('e_signature', NVARCHAR(256)),
    Column('index_code', NUMBER(asdecimal=False)),
    Column('create_worker', VARCHAR(36)),
    Column('create_time', DateTime),
    Column('latest_modify_worker', VARCHAR(36)),
    Column('latest_modify_time', DateTime),
    Column('isvalid', NUMBER(asdecimal=False)),
    Column('bz1', NVARCHAR(255)),
    Column('bz2', NVARCHAR(255)),
    Column('bz3', NVARCHAR(255)),
    Column('bz4', NVARCHAR(255)),
    Column('bz', NVARCHAR(255)),
    Column('is_leader', NUMBER(asdecimal=False)),
    Column('ca_key', VARCHAR(64)),
    Column('worker_level', NUMBER(asdecimal=False))
)


class UsersGroup(Base):
    __tablename__ = 'users_group'
    __table_args__ = {'comment': '群组'}

    id = Column(VARCHAR(36), primary_key=True, comment='主键')
    name = Column(NVARCHAR(64), comment='群组名称')
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
