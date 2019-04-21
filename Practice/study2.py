# a = int(input('请输入一个数字：'))
#
# if a > 0:
#     a += 10
#
# elif a == 0:
#     a += 20
#
# else:
#     a += 30
#
# print(a)

# b = float(input('请输入一个数字：'))
#
# if b>=90 and b<=100:
#     print('等级为A')
#
# elif b<90 and b >=60:
#     print('等级为B')
#
# else:
#     print('等级为E')

# 定义循环变量
# n = 5
# # 循环条件
# while n > 0:
#     # 循环体
#     a = int(input('请输入一个数字：'))
#
#     if a > 0:
#         a += 10
#
#     elif a == 0:
#         a += 20
#
#     else:
#         a += 30
#
#     print(a)
#
#     # 循环变量发生变化
#     n = n-1

# 计算1+2+...100
# n = 1
# sum = 0
# while n <= 100:
#     sum = sum + n
#     n += 1
# print(sum)

# for i in [1, 2, 1, 4]:
#     print(i, 'ok')

# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)

# 作业
# 1 求10阶乘
n = 1
m = 1
while n < 11:
    m = m * n
    n += 1
print(m)

# 2 求100以内能被3整除的数，并将作为列表输出
list1 = []
for i in range(1, 101):

    if i % 3 == 0:
        list1.append(i)

print(list1)

# 3 列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
li = [1, 2, 3, 4, 3, 4, 2, 5, 5, 8, 9, 7]
x = list(set(li))
print(x)

# 4 求斐波那契数列 1 2 3 5 8 13 …

a = 0
b = 1
c = 1
while c < 100:
    print(c, end=',')

    a = b
    b = c
    c = a + b

# 5 求10000以内的质数（质数：只能被1和它本身整除）
li3 = []
x1 = 2
for x1 in range(2, 10000):
    x2 = 2
    for x2 in range(2, x1):
        if x1 % x2 == 0:
            break
    else:
        li3.append(x1)
print(li3)
