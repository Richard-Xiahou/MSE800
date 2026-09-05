import time
def log(func):
    def wrapper():
        print ("Current Time: %s" % time.now())
        func()
    return wrapper

@log
def save():
    print("Saving")

@log
def delete():
    print("Deleting")

@log
def update():
    print("Updating...")

# 如果save,delete,update 每次保存数据，都打印当前时间。
# Decorator 能够解决这种重复
# update() 其实等同于 update = log(update)
# 多个装饰器如
# @A
# @B
# def f():
#     pass
# 等同于
# f = B(A(f))
# 顺序其实是从下到上 f() -> B(f()) -> A(B(f()))