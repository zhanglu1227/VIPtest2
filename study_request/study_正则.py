import re

# print(re.match('com','comWWW.runoob.com'))   # 在起始位置匹配

# result = re.match('com','comWWW.runoob.com')   # 不在起始位置匹配
#
#
# result = re.search('www','www.baidu.com.www')
# print(result)
# print(result.group(0))


pattern = re.compile(r'\D')
result = pattern.findall('safd1safsafgdsfg')
print(result)