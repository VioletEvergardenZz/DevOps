from flask import Flask

# 创建 Flask 应用实例  __name__ 参数表示当前模块的名称，当该模块被直接执行时，其值为 '__main__'
app = Flask(__name__)

# 将 URL 路由与视图函数绑定
@app.route('/')
# 视图函数，处理 URL 路由 / 的请求，并返回一个字符串
def hello_world():
    return 'xiaoxiao'

if __name__ == '__main__':
    app.run("0.0.0.0")