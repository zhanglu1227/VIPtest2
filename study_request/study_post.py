
import requests

# 发送post请求
urlstr = 'https://www.wanandroid.com/user/login'

data = {'username':'zhanglu77','password':'qweqwe123'}

# 发送请求
r = requests.post(url=urlstr, data=data)

if r.status_code == 200:
    print('登录成功')

else:
    print('登录失败')

# 获取结果
print(r.text)
print(type(r.json()))
print(r.json()['data']['username'])
print(r.status_code)





