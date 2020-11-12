# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, MetaData, NVARCHAR, Table, VARCHAR
from sqlalchemy.dialects.oracle import LONG, NUMBER

metadata = MetaData()


t_message_info = Table(
    'message_info', metadata,
    Column('id', VARCHAR(36), comment='主键ID'),
    Column('message_id', VARCHAR(128), comment='消息编号'),
    Column('message_body', VARCHAR(4000), comment='消息主题内容'),
    Column('create_time', DateTime, comment='创建时间'),
    Column('type', NUMBER(asdecimal=False), comment='消息类型'),
    Column('status', NUMBER(asdecimal=False), comment='消息状态'),
    Column('excute_time', NUMBER(asdecimal=False), comment='执行时间'),
    Column('system_code', VARCHAR(52), comment='系统标识代码'),
    Column('target_url', VARCHAR(256), comment='请求目标URL'),
    Column('callback_url', VARCHAR(256), comment='回调地址URL'),
    Column('ret_value', VARCHAR(2000), comment='请求返回值'),
    Column('request_ip', VARCHAR(24), comment='请求IP'),
    Column('third_process_res', NUMBER(asdecimal=False), comment='三方系统处理响应结果'),
    Column('isvalid', NUMBER(asdecimal=False), comment='ISVALID'),
    Column('create_worker', VARCHAR(36), comment='创建人'),
    Column('latest_modify_time', DateTime, comment='最后更新时间'),
    Column('latest_modify_worker', VARCHAR(36), comment='最后更新人'),
    Column('bz1', NVARCHAR(255), comment='BZ1'),
    Column('bz2', NVARCHAR(255), comment='BZ1')
)


t_schedule_job = Table(
    'schedule_job', metadata,
    Column('id', VARCHAR(36), comment='主键'),
    Column('job_name', VARCHAR(256), comment='任务名称'),
    Column('sys_name', VARCHAR(256), comment='系统名称'),
    Column('url', VARCHAR(512), comment='请求路径URL'),
    Column('params', VARCHAR(512), comment='请求参数'),
    Column('cron', VARCHAR(36), comment='转换相应的cron表达式'),
    Column('status', NUMBER(asdecimal=False), comment='状态 1启动 0暂停'),
    Column('start_time', DateTime, comment='开始执行时间'),
    Column('i_execute_now', NUMBER(asdecimal=False), comment='是否立即执行 1是 0否'),
    Column('loop_day', NUMBER(asdecimal=False), comment='循环执行时间 单位：秒'),
    Column('i_loop', NUMBER(asdecimal=False), comment='是否循环执行  1否 0是'),
    Column('remind', VARCHAR(512), comment='任务描述'),
    Column('create_time', DateTime, comment='创建时间'),
    Column('latest_modify_time', DateTime, comment='最后修改时间\t'),
    Column('index_code', NUMBER(asdecimal=False), comment='排序编号\t'),
    Column('isvalid', NUMBER(asdecimal=False), comment='是否启用\t'),
    Column('bz1', NVARCHAR(255), comment='备注1'),
    Column('bz2', NVARCHAR(255), comment='备注2'),
    Column('bz3', NVARCHAR(255), comment='备注3'),
    Column('bz4', NVARCHAR(255), comment='备注4'),
    Column('create_worker', NVARCHAR(36)),
    Column('latest_modify_worker', NVARCHAR(36)),
    Column('loop_hour', Integer, comment='轮询的小时数'),
    Column('loop_min', Integer, comment='轮询的分钟数'),
    Column('loop_sec', Integer, comment='轮询的秒数')
)


t_schedule_job_log = Table(
    'schedule_job_log', metadata,
    Column('id', VARCHAR(36), comment='主键ID'),
    Column('job_id', VARCHAR(36), comment='任务ID'),
    Column('complate_time', DateTime, comment='完成时间'),
    Column('success', NUMBER(asdecimal=False), comment='成功标识 1成功 0失败'),
    Column('result', VARCHAR(512), comment='响应内容'),
    Column('create_time', DateTime, comment='创建时间'),
    Column('create_worker', VARCHAR(36), comment='创建人'),
    Column('latest_modify_time', DateTime, comment='最后修改时间'),
    Column('latest_modify_worker', VARCHAR(36), comment='最后修改人'),
    Column('isvalid', NUMBER(asdecimal=False), comment='是否启用'),
    Column('index_code', NUMBER(asdecimal=False), comment='排序编号'),
    Column('bz1', NVARCHAR(255), comment='备注1'),
    Column('bz2', NVARCHAR(255), comment='备注2'),
    Column('bz3', NVARCHAR(255), comment='备注3'),
    Column('bz4', NVARCHAR(255), comment='备注4'),
    Column('start_time', DateTime, comment='任务开始时间'),
    Column('execute_time', LONG, comment='执行时间（毫秒）')
)
