import os
import sys
from logFile.logger import getLog

log = getLog("DEBUG")


def mk_dir(path):
    # 去除首位空格
    path = path.strip()
    path = path.rstrip("\\")
    path = path.rstrip("/")

    # 判断路径是否存在
    is_exists = os.path.exists(path)

    if not is_exists:
        try:
            os.makedirs(path)
        except Exception as e:
            log.error("目录创建失败：%s" % e)
    else:
        # 如果目录存在则不创建，并提示目录已存在
        log.debug("目录已存在：%s" % str(path))
        pass


def setPath(path, operation="add"):
    log.warning("仅windows系统可使用%s函数 " % sys._getframe().f_code.co_name)
    assert "win" in sys.platform.lower()
    if path:
        if operation == "add":
            os.environ["Path"] += path
        else:
            os.environ["Path"] -= path

        return True
