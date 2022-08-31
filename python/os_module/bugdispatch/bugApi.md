# bugApi

```python
# -*- coding: utf-8 -*-
from flask import Flask, request
# 跨域访问
from flask_cors import CORS
from gevent import pywsgi
import json
from bugdispatch import  BugDispatch

app=Flask(__name__)
# 只接受get方法访问
@app.route("/bugdispatch_1.0", methods=["GET"])
def check(): 
    # 默认返回内容
    return_dict= {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data=request.args.to_dict()
    log_url = get_data.get('log_url')
    # 分支需要再考虑
    branch = get_data.get('branch')
    # 对参数进行操作
    return_dict['bug_author'] = main(log_url, branch)
    bug_author = main(log_url, branch)
    print(bug_author)
    if bug_author is None:
        return_dict['result'] = False
        return_dict['bug_author'] = 'yuanyi05'
    else:
        return_dict['result'] = True
        return_dict['bug_author'] = bug_author
    return json.dumps(return_dict, ensure_ascii=False)

def main(log_url, branch):
    log_url = log_url
    buger = BugDispatch('/home/work/QA_projects/bugdispatch_pro/code_repo_bak/androidtrunk')
    try:
        bug_author = buger.get_bug_author(log_url)
    except Exception as e:
        print(e)
        return '请传入日志文件连接'
    return bug_author

if __name__ == "__main__":
    server = pywsgi.WSGIServer(('0.0.0.0', 8080), app)
    CORS(app, supports_credentials=True)
    server.serve_forever()
    # app.run(host='0.0.0.0',port=8080,debug=False)

```

