# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
# 	return "<p>Hello,world!<p>"

# app.run()

from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return request.do_the_login()
    else:
        return request.show_the_login_form()