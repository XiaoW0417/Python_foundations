# 基础库用法

## sys
```python
uv run main.py arg1 arg2 ...

import sys
args = ["main.py", "arg1", "arg2", "..."]
sys.argv = args
```

## round
注意是奇进偶舍，float和round都存在误差，如果需要高精度计算，使用decimal
2.5 -> 2
3.5 -> 4

```python
# 1. 默认保留到整数
print(round(3.14))    # 输出: 3
print(round(3.66))    # 输出: 4

# 2. 指定保留位数
print(round(3.14159, 2))  # 输出: 3.14
print(round(3.14159, 3))  # 输出: 3.142

# 3. 对整数部分进行四舍五入（ndigits 为负数）
print(round(1234.56, -1)) # 输出: 1230.0 (十位)
print(round(1234.56, -2)) # 输出: 1200.0 (百位)
```

## list
```python
1.列表直接赋值是引用
a = [1,2,3]
b = a
id(a) == id(b) True
2.常见函数
(1)append
(2)extend  扩展，把其他列表接到后面
(3)insert(i, x) 指定位置插入值
(4)remove(x) 删除找到的第一个为x的值
(5)pop
(6)clear 删除所有
(7)index 查找指定值第一次出现的下标
(8)count 计数
(9)sort, copy: 浅拷贝，直接对原数组进行排序  sorted()返回一个新列表
(10)reversed 反转列表顺序 不同于上面的函数，这里数据类型还需要list()给转回来
```

切分赋值是深拷贝
```python
a = [1, 2, 3]
b = [:1] 
id(a) == id(b) False
```

## prinit
end = ""取消换行

## dict
```python
创建方式：
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict(sape=4139, guido=4127, jack=4098)
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

print(users.items())
# 输出类似：dict_items([('Hans', 'active'), ('Éléonore', 'inactive'), ('景太郎', 'active')])

print(users.keys())
# 输出类似：dict_keys(['Hans', 'Éléonore', '景太郎'])

print(users.values())
# 输出类似：dict_values(['active', 'inactive', 'active'])

print(type(users.items()))
# <class 'dict_items'>

print(type(list(users.items())[0]))
# <class 'tuple'>

dict.get("xx") 未获取到则返回None
dict["xx"] 未获取到则报错

list(dict) 返回dict中的所有键


```
in 只在dict的key中进行查找

## pop 与 del
pop会返回值，del直接删
pop没找到指定值可设置默认返回值，不会报错；
del没找到会报错

## copy
### 浅拷贝
copy.copy(data) 只复制了最外层，内层的修改还是会作用于原函数
直接修改外层的内容，不影响原函数

### 深拷贝
copy.deepcopy(data) 完全复制

## 循环
enumerate：拿到下标以及值

## match
```python
match status:
    case 401 | 403 | 404:        # 也可以直接用变量来进行匹配
        return "Not allowed"
    case 400:
        return "Bad request"
    case 404:
        return "Not found"
    case 418:
        return "I'm a teapot"
    case _:
        return "Something's wrong with the internet"
```

## set
```python
1.创建
s = {1, 2, 3}
s = set()                      # 不能用{}来创建，{}代表空列表
set(list) 可用于去重

2.添加/删除
s.add(4)                       # 添加单个元素
s.update({5, 6})               # 添加多个（可传入任何可迭代对象）
s.remove(3)                    # 删除元素，不存在则 KeyError
s.discard(3)                   # 删除元素，不存在也不报错（推荐）
s.pop()                        # 随机删除并返回一个元素（set 无序）
s.clear()                      # 清空 → set()

3.集合运算
a = {1, 2, 3}
b = {3, 4, 5}

a | b          # 并集 → {1,2,3,4,5}      等价 a.union(b)
a & b          # 交集 → {3}              等价 a.intersection(b)
a - b          # 差集 → {1,2}            等价 a.difference(b)
a ^ b          # 对称差集 → {1,2,4,5}     等价 a.symmetric_difference(b)
```

## 函数参数
```python
def f(*args, **kwargs):
    pass
*args接收所有位置参数
**kwargs接收所有关键字参数
def f(a, b="b"):
    pass
a是必须的参数，因为没有默认值
b可以按位置或者关键字传入
如果参数中已经出现了关键字参数，后面的参数就只能是关键字参数，无法再使用位置参数
```

## lambda
```python
lambda x, y: x+y
sort(data, key = lambda x: (-x[0], x[1]))   按x[0]倒叙排，相同时再按x[1]排序
```
前半部分为参数，后半部分为表达式

## 函数注解
```python
def f(a: str, b: int) -> dict:
    '''This is an abstract
    
    This is a discribtion
    '''

    pass
```

## collections.deque
```python
from collections import deque
# 效率比list更高，更适合用来实现queue
queue = deque([1, 2, 3])
queue = deque(maxlen=n) # 可指定maxlen。达到maxlen之后就右进左出
queue.append(4)
queue.popleft()
```
## map filter
```python
map(func, iterate) 
传入 函数+可遍历对象 iterate 中每个值都传入func, 返回所有函数的计算值，可转为list
filer(func, iterate) 
传入 函数+可遍历对象 iterate 中每个值都传入func, 只保留函数结果为True的原始值，可转为list
```

## zip
```python
转置矩阵
matrix = [[1,2,3],
          [2,3,4],
          [5,6,7]]
*matrix = ([1,2,3],    *的作用是解包
          [2,3,4],
          [5,6,7])
zip(*matrix) = ([[1,2,5],
                 [2,3,6],
                 [3,4,7]])
```

## 比较运算符
and 和 or都是短路运算符，a and b and c，如果a真，b假，则不会对c求值

## 模块
```python
import a           a.f()
import a as aa     aa.f()
from a import f    f()
from a import *    f()
```
### 添加 init.py使该目录成为一个包
```text
相对导入必须是包与包之间的关系，即主脚本和工具脚本所在目录都需要有 __init__.py
同时，只要发生了该目录下的导入，即执行__init__.py
project_root/              # 通常不放 __init__.py
└── mypackage/             # ← 根包，必须有 __init__.py
    ├── __init__.py
    ├── main.py            # 主脚本
    ├── utils/             # 子包
    │   ├── __init__.py
    │   └── helper.py
    └── data/
        ├── __init__.py
        └── loader.py
```

## 格式化输出
```python
print(f"{a} and {b}")
print(f"{a:.3f}")      #下面的保留位数方法可以用在f格式化中
print("{:2} and {:2.2%}".format(a, b))
{:.3}  保留 3位有效数字
{:.3f} 保留 小数点后3位有效数字
{:.3%} 百分比化，保留小数点后3位有效数字
```

## 读写文件
```python
'''
在mode后面➕b则为二进制读/写，此时encoding失效，无法使用
读写JPEG 和 EXE等二进制文件时最好 +b
'''
from pathlib import Path        用该库来自动创建父级目录
file_path = Path("")
file_path.parent.mkdir(parenst=True, exist_ok=True)

with open("file_path", "w/r/a/r+", encoding="utf-8") as f:
    read_data = f.read(size) # size 为可选，最多读取size个字符/字节 
    f.readline()  # 读取一行          + 表示读写混合模式
    for line in f:
        print(line)  # 按行读，循环
    list(f); f.readlines() # 读取所有行，作为列表
    f.write("This is a str") #写入文件，返回值为字符数

```
## json
```python
json.dump(data, file, ensure_acii=False, indent=2) # 把可序列化数据(list, dict, str)写进file
json.load(file) 把文件还原为本来的格式，取决于dump时的格式

json.dumps(data, ensure_acii=False, indent=2) # 把数据格式化为安全的字符串
json.loads(file) # 字符串格式化为json，需要是json支持的格式，也取决于dumps之前的格式

```

## 异常处理
异常能够被捕获，同时其他代码会继续运行
```python
try:
    coding
except Exception as e:
    coding
finally:               #无论如何都会执行，放到最后
    coding
```

## 类
### namespace
```python
nonlocal a    #修改最近的外层变量a
a = 1
global a      #修只改最外层的全局a，但是中间仍然存在的函数空间的a不变
a = 1 

class Example:
    def __init__(self, name):     #初始化函数，可以没有。用来给类赋值一些属性
        self.name = name
    def func(self, pares)         #类方法，调用时接收函数
        print(pares)
a = Example("Alice")
a.name                -> "Alice"
a.func("example")     -> "example"
```

## 迭代器
```python
s = "abc"
it = iter(s)
next(it) -> a -> b -> c 执行3次
```

## 生成器
```python
rev_gen = (data[i] for i in range(len(data)-1, -1, -1))  # 类似于[a for a in list]
# 等价于
def reverse_gen(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]

rev_gen = reverse_gen(data)

# rev_gen是一个生成器，一次只拿一个条数据，不占用内存
for char in rev_gen:
    print(char)
```

## 字符串处理
```python
a = str.split(",")     # 默认以连续空格分割，返回list
a = "".join(list)      # list里面必须是str，以""中的内容来连接，返回str

a = str.strip()        # 删除两端空格、回车等。可指定删除元素
```