import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)5s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('practice.log', encoding='utf-8'),   # 输出到log文件
        logging.StreamHandler()                                  # 输出到终端
    ]
)

logging.info("This is an info")
logging.warning("This is warning")
logging.error("This is an error")