# # 整数（int），浮点数(float），字符串(str)
# a = 9
# b = 3.33
# c = '测试'
# print(a)
# print(b)
# print(c)
#
# a, b = input('请输入：').split(',')
# print(a, b)
#
# print('a的值为：', a)
# print('a的值为：%s' % a)
#
# # 元祖
# tu1 = (3, 5, 'asd', 90)
# print(type(tu1))
# print(tu1)
# print(tu1[0])
#
# # 列表
# li1 = [4, 2, 0, 'ssss']
# print(li1)
# print(type(li1))
# print(li1[3])
#
# # 切片
# li3 = [3, 8, 2, 9, 0, 5, 6, 1, 13, 45]
# print(li3[2:5])
# print(li3[3:7:2])
# print(li3[-1])
# print(li3[::-1])
# # 列表中所有奇数
# # 列表中所有偶数
#
# # 练习：定义一个1-9的元组，1、输出倒数第3个元素；2、输出值468
# tu2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(tu2[-3])
# print(tu2[3::2])
#
# # 如何定义1-999的元组
# tu3 = tuple(range(1, 1000))
# print(tu3)
# # 取所有奇数
# print(tu3[::2])
# # 取所有偶数
# print(tu3[1::2])
#
# # s.reverse() 逆序 改变原来的值
# li4 = [4, 5, 6, 2, 1, 0, 8, 11]
# li4.reverse()
# print(li4)
#
# # s.sort() 排序存在 改变原来的值
# li4.sort()
# print(li4)
#
# # sorted(s) 排序 不改变原来的值
# print(sorted(li4))
#
# # s.insert(n,m) 插入 在(s[n]前面)插入该值m
# li4.insert(2, 7)
# print(li4)
#
# # s.append(n) 追加 在该列表末尾追加n
# li4.append(18)
# print(li4)
#
# # m.extend(n) 连接两个列表
# li5 = [2, 3]
# li6 = [3, 5, 'zzz']
# li5.extend(li6)
# print(li5)
#
# # m.pop(n) 删除指定元素 n为下标
# li4.pop(2)
# print(li4)
#
# # m.remove(n) 删除指定元素第一次出现的值  n为元素
# li7 = [2, 3, 4, 5, 6, 2, 1, 1, 1, 8]
# li7.remove(1)
# print(li7)
#
# # m.count(n) 返回该值在列表中出现的次数 n为元素
# print(li7.count(1))
#
# # max(s) 返回列表中元素最大值
# print(max(li7))
#
# # min(s) 返回列表中元素最小值
# print(min(li7))
#
# # del s[n] 删除  n为下标
# del li7[0]
# print(li7)
# # del(li7[0])   # 也可以这样写
# # print(li7)
#
# # s.index(n)  获取元素的下标，n为元素
# print(li7.index(6))
#
# # s.clear() 清空列表
# li8 = [4, 5, 7]
# li8.clear()
# print(li8)
#
# # in 和 not in  用来检查是否在列表中
# li9 = [3, 5, 6, 2, 0, 9]
# print(0 in li9)
# print(3 not in li9)
#
# '''
# 练习：列表[11,13,5,7,0,56,23,34,72]，
# 求该列表中的最大值，最小值及列表中一共有几个元素
# 获取56元素在列表的位置
# 追加元素7
# 删除元素0
# 排序列表（由大到小）
# 将列表[66,67,68]与原列表组合
# '''
# li10 = [11, 13, 5, 7, 0, 56, 23, 34, 72]
# print(max(li10))
# print(min(li10))
# print(len(li10))
# li10.append(7)
# print(li10)
# print(li10.index(0))
# del li10[4]
# print(li10)
# li10.sort()
# li10.reverse()
# print(li10)
# li11 = [66, 67, 68]
# li10.append(li11)
# print(li10)
#
# # 集合 无序的且不重复  不能通过下标引用
# set1 = {3, 4, 5}
# # s.add(n) 添加  n为元素
# set1.add(9)
# print(set1)
# # s.remove(n) 删除  删除元素n
# set1.remove(4)
# print(set1)
# # s.discard(n) 删除
# set1.discard(5)
# print(set1)
# # s.clear()  清空集合
# set1.clear()
# print(set1)
# # in 和 not in  用来检查是否在集合中
# set2 = {5, 3, 9, 2}
# print(0 in set2)
# print(3 not in set2)
#
# # 字典  字典内的元素没有顺序，不能够通过下标引用
# dic1 = {'a': 15, 'b': 0, 'c': 'xxx'}
# # 通过键来引用
# print(dic1['a'])
# print(dic1)
# # 赋值
# dic1['d'] = '你好'
# print(dic1)
# # s.keys() 取出所有的键
# print(dic1.keys())
# # s.values() 取出所有的值
# print(dic1.values())
# # s.items() 取出所有的键值对，作为一个列表内的元素
# dic1.items()
# print(list(dic1))
# # del s[‘key’]  删除
# del dic1['b']
# print(dic1)
# # s.clear(） 清空字典
# dic1.clear()
# print(dic1)
#
# # if判断
# a1 = 0
# if a1 > 0:
#     a1 += 1
# print(a1)
#
# a2 = int(input('请输入：'))
# if a2 > 0:
#     a2 += 1
# else:
#     a2 -= 1
# print(a2)
#
# a3 = int(input('请输入：'))
# if a3 > 0:
#     a3 += 1
# elif a3 == 0:
#     a3 -= 1
# elif a3 < 0:
#     a3 += 3
# print(a3)
#
# # 输入一个数，判断该数的等级：90-100：等价为A……60以下：等级为E
# b1 = int(input('请输入：'))
# if b1 >= 90 and b1 <= 100:
#     print('等级为a')
# elif b1 < 90 and b1 >= 80:
#     print('等级为b')
# elif b1 < 80 and b1 >= 70:
#     print('等级为c')
# elif b1 < 70 and b1 >= 60:
#     print('等级为d')
# elif b1 < 60 and b1 > 0:
#     print('等级为e')
# else:
#     print('输入错误')
#
# # while循环
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#
# # 计算1+2+3+4……+100的和
# n = 1
# sum = 0
# while n <= 100:
#     sum = sum + n
#     n += 1
# print(sum)
#
# # for循环
# for i in [1, 2, 3, 4, 6, 7, 8, 0]:
#     print(i)
#
# for i in range(1, 10):
#     if i == 3:
#         break
#     else:
#         print(i)
#
# for i in range(1, 99):
#     if i > 66:
#         continue
#     else:
#         print(i)


