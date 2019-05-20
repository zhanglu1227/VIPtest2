# 1---导入包

import requests
'''
# 发送Get请求

urlstr = 'https://www.wanandroid.com/article/query'

# https://www.wanandroid.com/article/query?k=Android

# 携带参数
param = {'k': 'Android'}
# 2---发送请求
r = requests.get(url=urlstr, params=param)

# 3---获取结果
print(r.text)
print(r.status_code)
print(r.headers)
'''

# headers

urlstr = 'https://www.wanandroid.com/blog/show/2'

header = {'User-Agent':'Mozilla/6.0'}
cookie = {}

r = requests.get(url=urlstr, headers=header, cookies=cookie)

print(r.text)
print(r.headers)
print(r.cookies)

