
# 模式：r：读; r+：读写；w：写（覆盖/新建）；w+：读写（覆盖/新建）；a：追加（存在的时候追加；没有的时候新建）


# -------------------------------------------------------------读取
# 打开文件open，两个常用参数：文件路径和打开模式
# 路径支持决定路径和相对路径
# f = open('/Users/cola/Desktop/testcode/VIPtest2/data', 'r')

# 读取文件全部内容，或读取定制长度字节的数据
# print(f.read())
# print(f.read(4))

# 读取整行
# print(f.readline())

# 读取所有行
# print(f.readlines())

# f.close()

# --------------------------------------------------写入
# f = open('/Users/cola/Desktop/testcode/VIPtest2/data', 'w+')
# f.write('hello python!')
# f.write('测试')
# f.seek(0) # 设置指针放在第一个位置
#
# print(f.readlines())
# f.close()

f = open('/Users/cola/Desktop/testcode/VIPtest2/data2', 'r')
li = []
f1 = f.read()
# f1 = f.readlines()

# for s in f1:
#     a = s.split()
#     # print(a)
#     for number in a:
#         if number.isdigit():
#             li.append(number)
#
# print(li)

# i = 0
# str1 = ''
# while i < len(f1):
#     if f1[i].isdigit():
#         str1 += f1[i]
#     i += 1
#
# print(str1)

# for n in f1:
#     str1 = n.strip()
#     str2 = str1.split(',')
#     # print(str2)
#     li.append(str2)
# print(li)


n = 1
for line in f1:
    n += 1
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















