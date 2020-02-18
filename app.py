from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
        return "区域科技型企业画像系统"

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.run(debug=True,port=5000)