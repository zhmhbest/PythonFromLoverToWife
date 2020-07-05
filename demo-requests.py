# pip install requests
import requests
import json

# requests.get
# requests.post
# requests.request

result = requests.request(
    method='POST',  # GET | POST

    # 百度翻译接口
    url='https://fanyi.baidu.com/sug',
    # timeout=2               # 超时等待2s
    # allow_redirects=True,   # 允许重定向
    # verify=True,            # 验证签名
    # proxies=None,           # 代理IP

    # GET  -> params
    params=None,

    # POST -> data
    data={
        'kw': "God"
    },

    headers=None,   # Dict
    cookies=None,   # Dict or CookieJar
    files=None,     # Dict of filename->fileobject
)

print("HTTP Status =", result.status_code)
print("Encoding =", result.encoding)
# result.headers : Response Headers

# 【Header】
print(type(result.headers), result.headers)

# 【Cookie】
print(type(result.cookies), result.cookies)

# 【Content】
# result.text    : Content in unicode
# result.content : Content in bytes
res_text = json.loads(result.text)['data']
print(res_text)
