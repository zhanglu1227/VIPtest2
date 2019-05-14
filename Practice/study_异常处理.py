
# 1-----try -except  --已知异常
# def calc(a, b):
#     try:
#         print(a / b)
#     except ZeroDivisionError:
#         print('除数不能为0')
#
# a = int(input(':'))
# b = int(input(':'))
# calc(a, b)

# 2-----try --except --未知异常 BaseException 和 Exception
# def calc(a, b):
#     try:
#         print(a / b)
#     except BaseException:
#         print('除数不能为0')
#
# a = int(input(':'))
# b = int(input(':'))
# calc(a, b)

# 3-----多重异常:挨个匹配except

# def calc(a, b):
#     try:
#         print(a / b)
#     except NameError:
#         print('该对象未声明')
#     except ZeroDivisionError:
#         print('除数不能为0')
#
# a = int(input(':'))
# b = int(input(':'))
# calc(a, b)

# 4-----最终处理：不管有没有异常，都执行finally

# def calc(a, b):
#     try:
#         print(a / b)
#     except NameError:
#         print('该对象未声明')
#     except ZeroDivisionError as msg:
#         print(msg)
#         # print('除数不能为0')
#     finally:
#         print('程序执行完毕')
#
# a = int(input(':'))
# b = int(input(':'))
# calc(a, b)

# 5---else  程序没有抛出异常，继续执行else语句
# def calc(a, b):
#     try:
#         print(a / b)
#     except NameError:
#         print('该对象未声明')
#     except TypeError as msg:
#         print(msg)
#         # print('除数不能为0')
#     else:
#         print('程序执行完毕')
#
# a = int(input(':'))
# b = int(input(':'))
# calc(a, b)

# 6---抛出异常  ---异常必须为exception的子类
# raise TypeError('类型错误！')

###
# def calc(a, b):
#     try:
#         print(a / b)
#     except NameError:
#         print('该对象未声明')
#     except TypeError:
#         print('类型错误')  # 输入的类型错误
#         # print('除数不能为0')
#     finally:
#         print('程序执行完毕')
#
# a = input(':')
# b = input(':')
# calc(a, b)