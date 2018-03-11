from wsgiref.simple_server import make_server


class SimServer(object):
	def __init__(self):
		self.url_map = {}
	
	def __call__(self, environ, start_response):
		status = u'200 OK'
		response_headers = [('Content-type', 'text/plain')]
		start_response(status, response_headers)
		data = self.dispatch_request(environ)
		return [data.encode('utf-8'), ]
	
	def run(self, ip=None, host=None):
		if not ip:
			ip = ''
		if not host:
			host = 8080
		httpd = make_server(ip, host, self)
		httpd.serve_forever()
	
	def route(self, rule):  # Flask使用装饰器来完成url与处理函数的映射关系建立
		def decorator(f):  # 简单，侵入小，优雅
			self.url_map[rule.lstrip('/')] = f
			return f
		
		return decorator
	
	def dispatch_request(self, request):
		print(request)
		path = request.get('PATH_INFO', '').lstrip('/')
		print(path)
		return self.url_map[path]()  # 从url_map中找到对应的处理函数，并调用
