from flask import Flask,render_template

app = Flask(__name__)


@app.route('/',methods=['get',])
def hello_world():
    return render_template('index.html')

@app.route('/user/<name>',methods=['get','post'])
def user(name):
    return name


@app.route('/nihao')
def nihao():
    return


if __name__ == '__main__':
    app.run(FLASK_DEBUG=1)
