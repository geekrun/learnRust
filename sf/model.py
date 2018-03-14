import functools


class Field(object):
	def __init__(self, column_type, max_length, **kwargs):
		'''
		1，删除了参数name，field参数全部为定义字段类型相关参数，和众多有名的orm相同
		2，使用反射，方便字段的扩展，如本例使用deafault就是反射的应用
		3，如果想要做到好的解耦，可以先用反射给属性赋值，
			然后在做检查，本文就不做更进一步处理
		'''
		self.column_type = column_type  # 字段类型
		self.max_length = max_length  # 字段长度
		self.default = None
		if kwargs:
			for k, v in kwargs.items():
				if hasattr(self, k):
					setattr(self, k, v)
	
	def __str__(self):
		return '<%s>' % (self.__class__.__name__)


class StringField(Field):
	def __init__(self, max_length, **kwargs):
		super().__init__(column_type='varchar({})'.format(max_length), max_length=max_length, **kwargs)


class IntegerField(Field):
	def __init__(self, **kwargs):
		super().__init__(column_type='bigint', max_length=8)


class ModelMetaclass(type):
	def __new__(cls, name, bases, attrs):
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)
		mappings = dict()
		for k, v in attrs.items():
			# print('k={},v={}'.format(k,v))
			if isinstance(v, Field):
				mappings[k] = v
		for k in mappings.keys():
			attrs.pop(k)
		attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
		attrs['__table__'] = attrs.get('Meta').table or name  # 假设表名和类名一致
		return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
	def __init__(self, **kw):
		super(Model, self).__init__(**kw)
	
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)
	
	def __setattr__(self, key, value):
		self[key] = value
	
	def save(self):
		fields = []
		params = []
		for k, v in self.__mappings__.items():
			fields.append(k)
			params.append(getattr(self, k, v.default))
		sql = 'insert into {} ({}) values ({})'.format(self.__table__, self.join(fields), self.join(params))
		print('SQL: %s' % sql)
	
	# 自己写了一个join函数，廖雪峰老师使用自带join，无法处理数字等非字符串类型
	def join(self, attrs, pattern=','):
		return functools.reduce(lambda x, y: '{}{}{}'.format(x, pattern, y), attrs)


class User(Model):
	# 使用Meta，能自定义表的相关信息
	class Meta:
		# 自定义表名
		table = 'users'
	
	# 定义类的属性到列的映射：
	id = IntegerField()
	name = StringField(max_length=50)
	email = StringField(max_length=50, default='root@123.com')
	password = StringField(max_length=50)


if __name__ == "__main__":
	# 创建一个实例：
	u = User(id=234, name='jane', password='pwd')
	# 保存到数据库：
	u.save()
	# 打印结果;SQL: insert into users (id,name,email,password) values (234,jane,root@123.com,pwd)
