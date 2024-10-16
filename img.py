from flask import Flask
from flask import render_template

app = Flask(__name__)

"""
读取本地图片，并返回图片流给前端显示
"""


def return_img_stream(img_local_path):
    """
    工具函数：
    :param img_local_path:文件单张图片的本地绝对路径
    :return: 图片流
    """
    import base64
    img_stream = ''
    with open(img_local_path, 'r') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream)
    return_img_stream()


@app.route('/')
def hello_world():
    img_path = 'D:/Dorian/styletransfer/images/style.jpg'
    img_stream = return_img_stream(img_path)
    return render_template('index.html',
                           img_stream=img_stream)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
