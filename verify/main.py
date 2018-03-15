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
	image_file = infor["image_file"]
	code = infor['code']
	image_content = image_file.getvalue()
	image_file.close()
	return Response(image_content, mimetype='jpeg')


if __name__ == '__main__':
	app.run(debug=True)
