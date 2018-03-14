import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from parsel import Selector
from copyheaders import headers_raw_to_dict
import json
import time
from hashlib import sha1
import hmac
from  http import cookiejar

s = requests.session()
s.headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

post_headers_raw = b'''
accept:application/json, text/plain, */*
Accept-Encoding:gzip, deflate, br
Accept-Language:zh-CN,zh;q=0.9,zh-TW;q=0.8
authorization:oauth c3cef7c66a1843f8b3a9e6a1e3160e20
Connection:keep-alive
DNT:1
Host:www.zhihu.com
Origin:https://www.zhihu.com
Referer:https://www.zhihu.com/signup?next=%2F
User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36
'''


def get_signal(time_stamp):
	"""
	传入一个时间戳
	:param time_stamp:
	:return: signature
	"""
	a = hmac.new("d1b964811afb40118a12068ff74a12f4".encode('utf-8'), digestmod=sha1)  # HMAC key
	a.update("password".encode('utf-8'))  # grant_type固定字符串
	a.update("c3cef7c66a1843f8b3a9e6a1e3160e20".encode('utf-8'))  # clienId
	a.update("com.zhihu.web".encode('utf-8'))  # 固定字符串
	a.update(time_stamp.encode('utf-8'))  # timeStamp
	return a.hexdigest()


def get_headers():
	'从网页源代码内解析出 uuid与Xsrftoken'
	z1 = s.get('https://www.zhihu.com/')
	sel = Selector(z1.text)
	jsdata = sel.css('div#data::attr(data-state)').extract_first()
	xudid = json.loads(jsdata)['token']['xUDID']
	# xsrf = json.loads(jsdata)['token']['xsrf']
	headers = headers_raw_to_dict(post_headers_raw)
	headers['X-UDID'] = xudid
	# headers['X-Xsrftoken'] = xsrf
	return headers


def get_data(username, password, captcha=''):
	client_id = 'c3cef7c66a1843f8b3a9e6a1e3160e20'
	timestamp = int(time.time()) * 1000
	signature = get_signal(str(timestamp))
	data = {
		'client_id': client_id, 'grant_type': 'password',
		'timestamp': str(timestamp), 'source': 'com.zhihu.web',
		'signature': signature, 'username': username,
		'password': password, 'captcha': captcha,
		'lang': 'en', 'ref_source': 'homepage', 'utm_source': ''
	}
	return data


# 检查验证码
def check_capthca(headers, cn=True):
	'检查是否需要验证码,无论需不需要，必须要发一个请求'
	if cn:
		url = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=cn'
	else:
		url = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=en'
	# headers.pop('X-Xsrftoken')
	z = s.get(url, headers=headers)
	print(z.json())
	return z.json()


def zhihu_login(username, password):
	url = 'https://www.zhihu.com/api/v3/oauth/sign_in'
	headers = get_headers()
	check_capthca(headers)
	data = get_data(username, password)
	encoder = MultipartEncoder(data, boundary='----WebKitFormBoundarycGPN1xiTi2hCSKKZ')
	headers['Content-Type'] = encoder.content_type
	z2 = s.post(url, headers=headers, data=encoder.to_string(), )
	print(z2.json())


def is_login():
	# 通过个人中心页面返回状态码来判断是否为登录状态
	inbox_url = "https://www.zhihu.com/question/56250357/answer/148534773"
	response = s.get(inbox_url, headers=get_headers(), allow_redirects=False)
	if response.status_code != 200:
		return False
	else:
		return True


if __name__ == '__main__':
	username = 'liuxuejun1994@gmail.com'
	password = '19940712l'
	zhihu_login(username, password)
	content = s.request(url='https://www.zhihu.com/', method='get')
	with open('test.html', 'wb') as f:
		f.write(content.content)
