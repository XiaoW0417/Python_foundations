# 移步、协程笔记

## 回调函数
```python
def func1(a, b):
    return a+b

def func2(x):
    print(x)

def main(func1, *args, callback):   这种传入函数，再函数体内执行传入的函数的方式，称为回调函数
    result = func1(args)
    callback(result)
```

## 协程
回调函数的优化
```python
import asyncio

async def func1():
    print("start func1")
    await asyncio.sleep(1)
    print("func1 finished")

async def func2():
    print("start func2")
    await asyncio.sleep(3)
    print("func2 finished")

async def main():
    await asyncio.gather(func1(), func2()) # 某一个函数存在暂停的情况的时候，就会把控制权交出去，它执行完了得重新排队
asyncio.run(main())
```

