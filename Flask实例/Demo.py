from flask import Flask

app = Flask(__name__)


@app.route('/shcreditunion/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run(host='192.168.1.126',port=8000,debug=True)
