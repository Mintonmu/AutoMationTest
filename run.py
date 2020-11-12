import pytest

import argparse
from config.globalVars import G
from utils.logs import LogConfig
def get_args():
    """命令行参数解析"""
    parser = argparse.ArgumentParser(description=u'可选择参数：')
    parser.add_argument('-e', '--marker', choices=['z_user_org_right', 'z_workflow', 'z_web_container', 'z_file_management',
                                                   'z_auto_deploy', 'spring_demo', 'z_bussiness_commom', 'z_message_queue'],
                        help=u'marker表示需要测试的平台')
    args = parser.parse_args()
    G.module = args.marker

def main():
    """运行pytest命令启动测试"""
    pytest.main(['TestCase/', '-v', "-m %s" % G.module, '--html=%s/%s.html' % (G.report_path, G.module),'--self-contained-html', ])


if __name__ == '__main__':
    get_args()  # 命令行参数解析
    LogConfig(G.log_path)
    main()  # 运行pytest测试集
