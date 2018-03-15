import pymysql
from datetime import datetime


class MyPyMysql(object):
	def __init__(self, user, passwd, db, host='localhost', port=3306, use_unicode=True):
		self.host = host
		self.port = port
		self.user = user
		self.passwd = passwd
		self.db = db
		self.connect = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd,
		                               use_unicode=True)
		self.cursor = self.connect.cursor()
	
	def insert(self, table_name, kwargs):
		sql = 'insert into {} ({}) VALUES  {};'.format(table_name, ','.join(list(kwargs.keys())),
		                                               tuple(kwargs.values()))
		self.query(sql)
		'''
		success excute insert into student (id,name,age,birthData) VALUES  (12, 'dalex', 20, '2018-03-15 14:32:35.271451');
		success excute insert into student (id,name,age,birthData) VALUES  (23, 'balex', 20, '2018-03-15 14:32:35.271451');
		'''
		print('success excute {}'.format(sql))
	
	def query(self, sql):
		self.cursor.execute(sql)
		self.connect.commit()
	
	def close(self):
		self.cursor.close()
		self.connect.close()


if __name__ == "__main__":
	me = MyPyMysql('root', 'root', 'blog')
	'''
	1、由日期格式转化为字符串格式的函数为: datetime.datetime.strftime()
	2、由字符串格式转化为日期格式的函数为: datetime.datetime.strptime()
	from datetime import datetime
	print(datetime.now().strftime('%Y-%m-%d'))
	print(datetime.strptime('2018-03-15 15:32:24', '%Y-%m-%d %H:%M:%S'))
	输出结果为：
	2018-03-15
	2018-03-15 15:32:24
	'''
	birthData = str(datetime.now())
	me.insert('student', {'id': 12, 'name': 'dalex', 'age': 20, 'birthData': birthData})
	me.insert('student', {'id': 23, 'name': 'balex', 'age': 20, 'birthData': birthData})
	me.close()
