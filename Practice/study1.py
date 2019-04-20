'''
a = 5
b = 2.5
c = 'happy'

print(a)
print(b)
print(c)
'''

'''
str1 = "let's go!"
print(str1)

a, b = input('请输入：').split(',')
print(a, b)

print('a的值为：',a)
print('a的值为： %s'%a)
'''

'''
# 元祖  不可变
s = (1, 2.5, 'happy')
print(s)
print(type(s))

# 列表  可变
m = [1, 2.5, 'happy']
print(m)
print(type(m))
print(m[2])

'''
'''
# 步长：隔几个逗号
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(x)
print(x[3:6:1])
print(x[6:9:1])
print(x[2:9:2])
print(x[1:8:2])

# 最后一个数的下标
print(x[-1])

# 省略代表到最后
print(x[3::])

# 列表中所有奇数
print(x[::2])

# 列表中所有偶数
print(x[1::2])

'''

'''
tup1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tup1[-3])
print(tup1[3:8:2])

s = list(range(1, 1000))
print(s)
print(s[::2])
print(s[1::2])

'''

# a = int(input('请输入：'))
# print(a)

# a = input('请输入：')
# b = int(a)
# print(b)

# reverse 反转
# a = [5, 2, 1, 4, 3]
# a.reverse()
# print(a)
#
# # sort 对原列表排序
# a.sort()
# print(a)

'''
sorted(a)
print(a)
print(sorted(a))

'''
'''
# 在某个元素下标插入n
a.insert(3, 7)
print(a)

# 在该列表末尾追加n
a.append(11)
print(a)

'''

'''
# 两个列表连接
b = [4, 5, 6, 1, 2]
a.extend(b)
print(a)

'''
'''
# 删除元素 m.pop(n) m是列表，n是下标
a.pop(0)
print(a)

# m.remove(n) m是列表，n是元素
a.remove(2)
print(a)

# m.count(n) 元素n在列表中出现的次数  m是列表，n是元素
print(a.count(2))

# len(s) 返回列表中元素的个数

# s.index(n) 元素n在列表中的下标  s是列表，n是元素
print(a.index(4))

print(max(a))
print(min(a))

# del s[n] 删除列表中元素 s是列表，n是下标
del a[0]
print(a)

# s.clear 清空列表

'''

'''
列表[11,13,5,7,0,56,23,34,72]
求该列表中最大值，最小值及列表中一共有几个元素
获取56在元素的位置
追加元素7
删除元素0
排序列表（由大到小）
将[66,67,68]与原列表组合

'''

'''
li = [11,13,5,7,0,56,23,34,72]
# 求该列表中最大值，最小值及列表中一共有几个元素
print(max(li))
print(min(li))
print(len(li))
# 获取56在元素的位置
print(li.index(56))
# 追加元素7
li.append(7)
print(li)
# 删除元素0
print(li.index(0))
li.pop(4)
print(li)
# 排序列表（由大到小）
li.sort()
li.reverse()
print(li)
# 将[66,67,68]与原列表组合
li2 = [66,67,68]
li.extend(li2)
print(li)

'''

# 集合
# s = [3, 1, 2, 5, 10]
# m = list(set(s))
# print(m)

# 添加 s.add(n) 向集合s添加元素n
# 删除 s.remove(n) 删除集合中元素n，如果元素不存在，报keyerror异常
# 删除 s.discard(n) 删除集合中元素n
# 清空 s.clear()  清空集合
# in 和 not in  用来检查是否在集合中

# 字典
# di = {'a':4,'b':'测试','c':0.3}
# di['m']=10
# print(di)
# print(list(di.items()))
# print(list(di.keys()))
# print(list(di.values()))

