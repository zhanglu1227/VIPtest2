'''
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

'''

# ---------------------------------------------------------------

# 5.11作业
'''
# 1、取出文件中的数字并排序
f = open('/Users/cola/Desktop/testcode/VIPtest2/data2', 'r+')
f1 = f.read()
li = []

# n = 1
for line in f1:
    # n += 1
    line = line.replace('', '')
    # line = line.replace('\n', '')
    if line.isdigit():
        li.append(line)

    else:
        continue


# print(li)

def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li
print(bubble_sort(li))
# f.close()

# f = open('/Users/cola/Desktop/testcode/VIPtest2/data2', 'a+')
# for x in f.readlines():
#     if bubble_sort(li) not in x:
#         f.write(str(bubble_sort(li)))
#     else:
#         break
f.write(str(bubble_sort(li)))
f.close()
'''

# 2、打印小猫爱吃鱼，小猫要喝水
class Cat:
    def __init__(self, name):  # 实例属性，初始化
        self.name = name

    def eat(self, food):
        print('%s爱吃%s'%(self.name,food))  # 自定义方法，属性

    def drink(self, water):
        print('%s要喝%s'%(self.name,water)) # 自定义方法，属性

a = Cat('小猫')  # 实例化
a.eat('鱼')   # 调用类中方法
a.drink('水')  # 调用类中方法

# 3、小明爱跑步，爱吃东西
class Person:

    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

    def run(self, running):
        print('%s爱%s'%(self.name1,running))

    def eat(self, food):
        print('爱吃%s'%food)

    # 1）小明体重75.0公斤
    def weight(self, weight1, weight2):
        print('%s体重%s公斤'%(self.name1,weight1))
        # print('每次%s会减肥%公斤'%(running, weight3))

        # 4）小美的体重是45.0公斤
        print('%s体重%s公斤'%(self.name2,weight2))

    # 2）每次跑步会减肥0.5公斤

    # 3）每次吃东西体重会增加1公斤


b = Person('小明','小美')
b.run('跑步')
b.eat('东西')
b.weight('75.0', '45.0')

# 4 摆放家具
# 1）.房子有户型，总面积和家具名称列表
# 新房子没有任何的家具
class Home:

    def __init__(self, model, area):
        self.area = area
        self.model = model
        self.furniture = []

# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
class Bed:

    def __init__(self, area, name = '床'):
        self.name = name
        self.area = area

    def __str__(self):
        msg = '床占地面积为：' + str(self.area)
        return msg


# 3）.将以上三件家具添加到房子中

# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表










