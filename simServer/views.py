from simServer.serverHadler import SimServer

# 创建一个app
app = SimServer()


@app.route('/index')
def index():
	return 'hello world'


@app.route('/login')
def login():
	return 'please login'


if __name__ == "__main__":
	app.run()

if __name__ == "__main__":
	app.run()
