import os
from flask import Flask, Response
from flask import render_template
from utils.code import Code

app = Flask(__name__)


@app.route('/')
def Register():
	return render_template('verify.html')


@app.route('/codes/')
def code():
	infor = Code().creat_code()
	image_path = infor["image_path"]
	code = infor['code']
	
	print(image_path)
	with open(image_path, 'rb') as f:
		image_content = f.read()
	os.remove(image_path)
	return Response(image_content, mimetype='jpeg')


if __name__ == '__main__':
	app.run(debug=True)
