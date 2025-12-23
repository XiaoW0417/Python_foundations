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