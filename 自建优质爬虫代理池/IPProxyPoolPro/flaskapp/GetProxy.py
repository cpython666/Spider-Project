from flask import Flask,jsonify
from IPProxyPoolPro import config

from IPProxyPoolPro.db.RedisHelper import RedisHelper
app = Flask(__name__,static_folder="static",template_folder="templates")

redisHelper = RedisHelper()

@app.route("/")
def hello():
    if redisHelper.count()>0:
        ls=redisHelper.getMax()
        return ls
    else:
        return '数据库暂时没有代理，爬虫板块加班中，稍等一下吧~~~'

@app.route("/all")
def all():
    if redisHelper.count()>0:
        return jsonify(redisHelper.all())

@app.route("/proxy/<int:num>")
def proxy(num):
    if redisHelper.count()>0:
        ls = redisHelper.getMax()
        if len(ls):
            return ls[:num]
        else:
            return ls

if __name__=='__main__':
    app.run(host='0.0.0.0', port=config['API_PORT'], debug=True)