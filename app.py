from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class Videos(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    video_name = db.Column(db.String(50),doc='名字',nullable=False)
    video_pic = db.Column(db.Text,doc='图片',nullable=False)
    video_url = db.Column(db.Text,doc='链接',nullable=False)
    video_description = db.Column(db.Text,doc='描述')

db.create_all()


@app.route('/')
def hello_world():
    info_1 = Videos(video_name='nihao',video_pic='http://pic.cn',video_url='http://url.cn',video_description='测试test')
    db.session.add(info_1)
    db.session.commit()
    return render_template('index.html')

@app.route('/video/<num>')
def video(num):
    print(num)
    return num


if __name__ == '__main__':
    app.run(Debug =True)


