# 标准库、常用库

## os

## argparse
```python
import argparse

parser = argparse.ArgumentParser(
    prog = "program"                # 可自定义，在-h时会显示，无特殊含义
    description="This is a test"    # 同上
)

parser.add_argument("--filenames", nargs="*")              # 添加参数，- / -- 表示是可选，无则表示必须，nargs指定数量
parser.add_argument("-l", "--lines", type=int, default=10) # 同时可指定类型，默认值
args = parser.parse_args()                                 # 取出args

print(args)
```

## random
```python
random.choice(['a', 'b'])     # 随机选择可迭代对象
random.sample(range(100), 10) # 无重复采样
random.random()               # 随机 [0.0-1.0) 采样
random.uniform(5.0, 20.0)     # 指定范围浮点数采样
random.randint(0, 10)         # 指定范围整数采样
```

## decimal
```python
from decimal import *
round(Decimal("1.34") * Decimal("23.1"), 2)    # 十进制浮点数运算，都是先由str转过来的，精度更高
```

## collections
```python
from collections import defaultdict
d = defaultdict[list]
d['a'].append(1) # 相比dict的有点在于不需要初始化，指定为list之后对于空键可以直接进行列表操作

# 控制字典中的元素，并且保持插入的顺序      但是内存是普通字典的两倍，注意
from collections import OrderedDict
d = OrderedDict()
for key in d:
    print(key, d[key])

from collections import Counter
data = ['Alice', 'Alice', 'Mike']
count_data = Counter(data)                # 返回的是一个dict结构的数据，对应出现次数，Counter({'Alice': 2, 'Mike': 1})
most_com = count_data.most_common(1)      # 返回出现最多的1个 [('Alice', 2)]

# 优雅的展平可迭代对象
from collection.abc import Iterable
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)   # 相当于再次for，递归的话就加上from
        else:
            yield x
```

## itertools
```python
from itertools import groupby

rows.sort(key=lambda x:x['date'])                # 需要先将rows进行排序，因为groupby只将连续的相同key分为一组
gb_rows = groupby(rows, key=lambda x:x['date'])  # gb_rows的结构类似 [key1: [data1, data2], key2: [data3, data4]]
                                                 # 也可以用defaultdict[list] 来存，用date实现查找。groupby的优势在于它是一个迭代器，省内存
for date, row in gb_rows:
    print(f"date:{date}")
    for i in row:
        print(f"{i}")
```

## Numpy
```python
import numpy as np         
x = np.array([1, 2, 3])
y = np.array([3, 4, 5])     # 不可增长
z = np.array([         
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
z[1:3, 1:3]              # 支持多维索引切片，list不支持

# numpy数组的标量运算时每个元素进行计算，但是纯list是拼接、复制列表
x += 1 / x += y / x *= y

numpy.zeros(shape=(x, y), dtype=float) / .ones() # 以0初始化指定形状的numpy数组

numpy.where(x<10, x, 10)    # where(codition, codition成立的取值, 不成立的取值) 用于剔除异常值、条件赋值
numpy.where(x>0)            # 返回的是index，二维就是 行下标[] 列下标[] 可以用rows, cols = idx来接收，zip组合更好看懂

x @ y / np.dot(x, y) / np.matmul(x, y) # 对array进行矩阵乘法，也可以用np.matrix直接*，但是array更灵活
```

## pickle 序列化存储py对象
```python
import pickle
pickle.dump / .dumps
pincle.load / .loads # 用法与json相同
```

## time
```python
import time
now_time = time.localtime()
time_stamp = time.time()                               # 从1970-01-01 00:00:00 UTC 开始的秒数, float
converted_time = time.localtime(time_stamp)            # 把浮点数转为对应的日期struct
f_time = time.strftime("%Y %m %d %H %M %S", now_time)  # 取出struct里面的时间, 用之前，如果是float，记得先用time.localtime转为struct
```

## logging
```python
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
```
