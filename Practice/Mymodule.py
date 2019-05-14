
def fun1():
    print('我是fun1函数')


def fun2():
    print('我是fun2函数')


# print('我是被调用的模块')

print('name值为：', __name__)
# 内置函数
if __name__ == '__main__':
    fun1()
    fun2()