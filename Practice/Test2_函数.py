# 函数练习

def study():
    print('好好学习')

a = study()
print(a)


def sum(sum1, sum2, sum4=10, *args, **kwargs):
    sum3 = sum1 + sum2
    print(args)
    print(kwargs)
    print(sum3)

sum(10, 100, 13, 32, 200, 300)


def func(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

func(11, 22, 33, 44, 55, task=66, done=77)


# 递归函数
# n!=1*2*3*...*n
# 方法一
def calnum(num):
    i = 1
    result = 1

    while i <= num:
        result *= i
        i += 1

    return result

ret = calnum(9)
print(ret)

# 方法二
def calnum(num):
    if num >= 1:
        result = num * calnum(num-1)

    else:
        result = 1

    return result

ret = calnum(9)
print(ret)
