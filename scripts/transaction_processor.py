from itertools import groupby
from collections import Counter
from pathlib import Path
from decimal import Decimal
from functools import wraps

import json
import asyncio
import time
import random
import logging
import pickle
import numpy as np
import argparse

# 加载数据
def load_data(path: Path) -> list:
    with open(path, "r", encoding='utf-8') as f:
        data = json.load(f)
        return data

# 存储数据
def save_data(data, path: Path) -> None:
    with open(path, "wb") as f:
        pickle.dump(data, f)

# 计时装饰器
def execution_timer(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"处理完成。耗时：{(end_time-start_time):.2f}s")
        return result
    return wrapper

class Transaction:
    '''
    定义交易类，初始化相关属性
    '''
    def __init__(self, init_ats: dict):
        self.user_id = init_ats.get("id")
        self.amount = init_ats.get("amt")
        self.status = init_ats.get("status")
        self.timestamp = init_ats.get("ts")
    
    def __repr__(self):
        return f"The class is with user-id: {self.user_id}"
    
    @classmethod
    def init_with_dict(cls, init_ats: dict):
        return cls(init_ats)
    
    async def compute(self) -> float | None:
        try:
            random_sec = random.uniform(0.01, 0.1)
            await asyncio.sleep(random_sec)
            currency = round(float(Decimal("0.9") * Decimal(str(self.amount))), 0)
            self.currency = currency
            return currency
        except Exception as e:
            logging.info(f"发现异常交易: user={self.user_id}, error: {e}")
            return None

@execution_timer
async def process_tran(tran: dict) -> tuple[dict | None, float | None, str]:
    """处理单条数据"""
    status = tran.get('status', 'unknown')

    cur_tran = Transaction.init_with_dict(tran)
    currency = await cur_tran.compute()

    if currency:
        tran['currency'] = currency
        return (tran, currency, status)
    else:
        return (None, None, status)

async def async_process_all(data: list[dict]) -> tuple[list[dict], list[float], list[str]]:
    """处理所有交易"""
    tasks = [process_tran(item)for item in data]
    results_tuples = await asyncio.gather(*tasks)
    processed_records: list[dict] = []
    amounts: list[float] = []
    statuses: list[str] = []

    for record, amount, status in results_tuples:
        statuses.append(status)
        if record:
            amounts.append(amount)
            processed_records.append(record)
    return processed_records, amounts, statuses

def run(args):
    output_path = args.output[0]
    threshold = args.threshold[0]
    input_path = args.input[0]

    ROOT_PATH = Path(__file__).resolve().parent.parent
    data_path = ROOT_PATH / input_path
    save_path = ROOT_PATH / output_path

    data_path.parent.mkdir(parents=True, exist_ok=True)
    save_path.parent.mkdir(parents=True, exist_ok=True)
    loaded_data = load_data(data_path)

    processed_records, amounts, statuses = asyncio.run(async_process_all(loaded_data))

    amts_np = np.array(amounts)
    qualified_indices = np.where(amts_np>threshold)[0]
    qualified_count = len(qualified_indices)

    processed_records.sort(key=lambda x: x.get("user", ""))

    gb_rows = groupby(processed_records, key=lambda x: x.get("user", "unknown"))

    save_data(processed_records, save_path)

    print("\n\t--- 统计报告 ---")
    print(f"1.\t高频交易(>{threshold}数量): {qualified_count} 笔")
    print("2.\t用户交易统计:")
    for name, group in gb_rows:
        group_list = list(group)
        print(f"\t- {name} {len((group_list))} 笔")
    print(f'3.\t状态分布: {Counter(statuses)}')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
    logging.info("开始处理...")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", nargs=1, default="data/transaction.json")
    parser.add_argument("--output", nargs=1, default="data/processed_data.pth")
    parser.add_argument("--threshold", nargs=1, type=int, default=100)
    args = parser.parse_args()
    
    run(args)