from flask import Flask,render_template

app = Flask(__name__)


@app.route('/',methods=['get',])
def hello_world():
    return render_template('index.html')

@app.route('/video/<num>')
def video(num):
    print(num)
    render_template('si.html')


if __name__ == '__main__':
    app.run()


