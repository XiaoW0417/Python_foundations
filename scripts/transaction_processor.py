from ast import parse
from itertools import groupby
import json
import asyncio
from collections import Counter
from pathlib import Path
from decimal import Decimal
from functools import wraps
import time
import random
import logging
import pickle
import numpy as np
import argparse

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logging.info("开始处理...")

# 加载数据
def load_data(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data

# 存储数据
def save_data(data):
    with open(save_path, "wb") as f:
        pickle.dump(data, f)

# 计时装饰器
def execution_timer(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        await func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"处理完成。耗时：{(end_time-start_time):.2f}s")
    return wrapper

# 定义交易类
class Transaction:
    '''
    初始化相关属性
    '''
    def __init__(self, init_ats: dict):
        self.user_id = init_ats.get("id")
        self.amount = init_ats.get("amt")
        self.status = init_ats.get("status")
        self.timestamp = init_ats.get("ts")
    
    def __repr__(self):
        return f"The class is with user-id: {self.user_id}"
    
    @classmethod
    def init_with_dict(cls, init_ats):
        return cls(init_ats)
    
    async def compute(self):
        try:
            random_sec = random.uniform(0.01, 0.1)
            await asyncio.sleep(random_sec)
            self.currency = round(float(Decimal("0.9") * Decimal(str(self.amount))), 0)
            return self.currency
        except Exception:
            logging.info("发现异常交易")

@execution_timer
async def process_tran(tran: dict):
    status_res.append(tran.get("status"))
    cur_tran = Transaction.init_with_dict(tran)
    result = await cur_tran.compute()
    amounts_list.append(result)
    tran.update({"currency": result})
    results.append(tran)

async def main():
    tasks = [process_tran(single_data) for single_data in loaded_data]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", nargs=1)
    parser.add_argument("--output", nargs=1)
    parser.add_argument("--threshold", nargs=1, type=int)
    args = parser.parse_args()
    print(args)

    amounts_list = []
    results = []
    status_res = []

    output_path = args.output[0]
    threshold = args.threshold[0]
    # input_path = "data/transaction.json"
    input_path = args.input[0]

    ROOT_PATH = Path(__file__).resolve().parent.parent
    data_path = ROOT_PATH / input_path
    save_path = ROOT_PATH / output_path

    data_path.parent.mkdir(parents=True, exist_ok=True)
    save_path.parent.mkdir(parents=True, exist_ok=True)
    loaded_data = load_data(data_path)


    asyncio.run(main())

    amts_np = np.array(amounts_list)
    qualified = np.where(amts_np>threshold)
    results.sort(key=lambda x: x["user"])
    gb_rows = groupby(results, key=lambda x: x["user"])
    save_data(results)

    print("\n\t--- 统计报告 ---")
    print(f"1.\t高频交易(>{threshold}数量): {len(qualified)} 笔")
    print("2.\t用户交易统计:")
    for name, user_infos in gb_rows:
        print(f"\t- {name} {len(list(user_infos))} 笔")
    print(f'3.\t状态分布: {Counter(status_res)}')
