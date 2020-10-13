import logging.handlers, os


def log_conf():
    """初始化日志配置"""
    # 日志器位置
    logPath = "./Log"
    # 日志器
    logger = logging.getLogger()
    # 日志器级别
    logger.setLevel(logging.INFO)
    # 处理器 -控制台
    sh = logging.StreamHandler()
    # 处理器 -文件
    trsh = logging.handlers.TimedRotatingFileHandler(filename=logPath + os.sep + "mini.log",
                                                     when="midnight", interval=1,
                                                     backupCount=7, encoding="UTF-8")
    # 格式化字符串
    f = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(f)

    # 把格式化器添加到处理器中
    sh.setFormatter(formatter)
    trsh.setFormatter(formatter)

    # 把处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(trsh)


# 请求通用接口地址
base_url = "http://e.cn/api/v1"

# 微信code
code = "093tXk0w3wSh7V2slM2w39HU0u1tXk0s"

# 请求头
headers = {
    "Content-Type": "application/json",
    "token": "c2d4680a195fac447f5fdc2f1130fb3f"
}
