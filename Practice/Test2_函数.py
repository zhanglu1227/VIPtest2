# # 函数练习
#
# def study():
#     print('好好学习')
#
# a = study()
# print(a)
#
#
# def sum(sum1, sum2, sum4=10, *args, **kwargs):
#     sum3 = sum1 + sum2
#     print(args)
#     print(kwargs)
#     print(sum3)
#
# sum(10, 100, 13, 32, 200, 300)
#
#
# def func(a, b, c, *args, **kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(kwargs)
#
# func(11, 22, 33, 44, 55, task=66, done=77)
#
#
# # 递归函数
# # n!=1*2*3*...*n
# # 方法一
# def calnum(num):
#     i = 1
#     result = 1
#
#     while i <= num:
#         result *= i
#         i += 1
#
#     return result
#
# ret = calnum(9)
# print(ret)
#
# # 方法二
# def calnum(num):
#     if num >= 1:
#         result = num * calnum(num-1)
#
#     else:
#         result = 1
#
#     return result
#
# ret = calnum(9)
# print(ret)
#
# a = [1, 3, 5, 7]
# a.insert(3, a[0])
# # print(a)
# print(a[1:])

# ------------------------------------------------------------------------

# 无参无返回值
def calc(a, b):
    c = a+b
    return c

# print(calc())
a = int(input('请输入一个数：'))
b = int(input('请再输入一个数：'))
result = calc(a, b)
print(result)

# 可变参数
def calc(*args):
    print(*args)

    for i in args:
        print('传入的值为：',i)

calc(1, 3, 5)

# 关键字参数
def person(name, age, **kwargs):
    print(name, age, kwargs)

person('xiaoming', 20, no=123455666666, sex='女')

# 设计一个计算器，输入两个数，自动实现加减乘除，根据用户输入的计算符号计算结果

def jisuanqi(a,b,c):

    if b == '+':
        return a + c

    elif b == '-':
        return a - c

    elif b == '*':
        return a * c

    elif b == '/':
        return a / c

    else:
        print('输入错误')


a=int(input('请输入第一个数：'))
b=input('请输入运算符：')
c=int(input('请输入第二个数：'))
print(jisuanqi(a,b,c))




