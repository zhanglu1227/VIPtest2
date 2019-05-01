# 4.20 作业

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
# x = list(set(li))
# print(x)

# 排序
li.sort()
# 去掉重复
li1 = []
for i in li:
    if i not in li1:
        li1.append(i)
print(li1)


# 4 求斐波那契数列 1 2 3 5 8 13 …
list2 = []
a = 0
b = 1
c = 1
while c < 100:

    # print(c, end=',')
    list2.append(c)
    a = b
    b = c
    c = a + b

print(list2)


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

