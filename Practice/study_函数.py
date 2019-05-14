
# 定义函数calc-无参无返回值
# def calc(x, y):
#     # print(x, y)
#     c = x + y
#     return c
#     # print('结果为：',c)
#     # print('结果为：%d' %c)
#
# # 调用
# # print(calc())
#
# a = int(input('请输入一个数：'))
# b = int(input('请输入第二个数：'))
# result = calc(a, b)
# print(result)

# 默认参数用法
# def add_end(L = None):
#     if L is None:
#         L = []
#     L.append(('End'))
#     return L
#
# print(add_end())
# print(add_end())

# 可变参数
# def calc(*numbers):
#     print(*numbers)
#     print(numbers)
#     sum = 0
#     for n in numbers:
#         sum += n
#
#     return sum
#
# print(calc(1, 2))

# def calc(*args):
#     print(*args)
#     print(args, type(args))
#
#     for i in args:
#         print('传入的值分别为：',i)
#
# # 带星号打印出来是整形数，不带星号打印出来是元祖
# # 可变参数传参形式1-常用
# m = [1, 2, 3]
# n = (3, 4, 5)
# # 通过引用的方式传入必须带*
# calc(*m)
# calc(*n)
#
# # 可变参数传参形式2
# # calc(1, 2, 3)

# 关键字参数
# 可变参数及关键字参数都可以不传参数，关键字参数可传入任意个
# def person(name, age, **kwargs):
#     print('name', name, 'age', age, kwargs)
#
# person('xiaoming', 25, sex='male', color='blue')
# person('xiaoming', 21)
# person('xiaoming', 21, sex='1')
# # person('xiaoming', 21, 'male')

# 设计一个计算器，输入两个数，自动实现加减乘除
def counter(x, y):
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)

    for i in x, y:
        print('输入的数分别为：',i)
n = [4, 5]
counter(*n)

# 进阶：根据用户输入的计算符号计算结果
def counter1():
    a = int(input('输入第一个数：'))
    b = int(input('输入第二个数：'))
    c = input('输入运算符：')

    if c == '+':
        result = a + b
    elif c == '-':
        result = a - b
    elif c == '*':
        result = a * b
    elif c == '/':
        result = a / b
    else:
        print('输入错误')

    print(result)

counter1()
