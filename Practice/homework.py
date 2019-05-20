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
f2 = open('/Users/cola/Desktop/testcode/VIPtest2/data3', 'r+')
f2.write(str(bubble_sort(li)))
f2.close()

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

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def xiaoming(self):
        print('%s体重是%s公斤'%(self.name, self.weight))  # 小明体重75.0公斤

    def run(self, runnig):
        print('%s爱%s'%(self.name, runnig))        # 小明爱跑步
        print('每次%s会减肥0.5公斤'%runnig)          # 2）每次跑步会减肥0.5公斤
        self.weight -= 0.5

    def eat(self, food):
        print('%s爱吃%s'%(self.name, food))      # 小明爱吃东西
        print("每次吃%s体重增加1公斤" %food)        # 3）每次吃东西体重会增加1公斤
        self.weight += 1

        # 4）小美的体重是45.0公斤

    def xiaomei(self):
        print('%s体重是%s公斤'%(self.name, self.weight))


b = Person('小明',75.0)
b.xiaoming()
b.run('跑步')
b.eat('东西')
c = Person('小美',45.0)
c.xiaomei()




'''
4 摆放家具
1）.房子有户型，总面积和家具名称列表
新房子没有任何的家具
2）.家具有名字和占地面积，其中
   床：占4平米
   衣柜：占2平面
   餐桌：占1.5平米
3）.将以上三件家具添加到房子中
4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
'''

class Home():

    def __init__(self, name, area):
        self.area = area
        self.name = name

    def __str__(self):
        return '[%s]占地%.2f' %(self.name,self.area)

class House():

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ('户型:%s\n总面积:%.2f[剩余:%.2f]\n家具:%s'
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        # 1.判断家具的面积
        if item.area > self.free_area:
                print('%s的面积太大，无法添加' % item.name)

        # 2.将家具的名称添加到列表中
        self.item_list.append(item.name)
        # 3.计算剩余面积
        self.free_area -= item.area

# 1.创建家具对象
bed = Home('床', 4)
yg = Home('衣柜', 2)
table = Home('餐桌', 1.5)

# 2.创建房子对象
my_house = House('两室一厅', 100)
# 3.添加家具
my_house.add_item(bed)
my_house.add_item(yg)
my_house.add_item(table)
print(my_house)
# 运行结果：
# 户型:两室一厅
# 总面积:100.00[剩余:92.50]
# 家具:['bed', 'yg', 'table']


'''
5.士兵开枪
需求：
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量
'''

# class Soldier:
#     def __init__(self, name):
#         self.name = name
#
#     def gun(self, qiang):
#         print('士兵%s有一把%s'%(self.name, qiang))
#
# c = Soldier('瑞恩')
# c.gun('AK47')



class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def __str__(self):
        return '%s士兵的枪为%s' % (self.name, self.gun)

    def fire(self):
        if self.gun == None:
            print('士兵还没有枪')
        else:
            self.gun.shoot()


class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def __str__(self):
        return '%s的子弹有%s颗' % (self.model, self.bullet_count)

    def shoot(self):
        if self.bullet_count < 1:
            print('没有子弹了，请补充子弹再射击')
        else:
            self.bullet_count -= 1
            return self.bullet_count

    def add_bullet(self, count):
        if self.bullet_count >= 50:
            print('子弹已经装满，不可再加')
        else:
            self.bullet_count += count


ryan = Soldier('瑞恩')

AK47 = Gun('AK47')
AK47.shoot()    #此时没有子弹不能射击
AK47.add_bullet(50) #加50发子弹
AK47.shoot()

print(AK47)



ryan.gun = AK47
ryan.fire()
print(ryan)
print(AK47)












