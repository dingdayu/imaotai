#!/usr/bin/python3
import logging
import sys

import login
import process

DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式
                    stream=sys.stdout,
                    datefmt=DATE_FORMAT)

configs = login.config
if len(configs.sections()) == 0:
    logging.error("配置文件未找到配置")
    sys.exit(1)

for section in configs.sections():
    mobile = section
    token = configs.get(section, 'token')
    bark = configs.get(section, 'bark')

    try:
        process.getResult(mobile, token=token, bark=bark)
    except BaseException as e:
        print(e)
        logging.error(e)
