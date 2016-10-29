# coding: utf-8
from . import app
from flask import render_template, request, jsonify
from flask_zero import Qiniu

qiniu = Qiniu(app)

@app.route('/config/', methods=['POST'])
def config():
    """
    七牛配置
    """
    if request.method == 'POST':
        QINIU_ACCESS_KEY = request.get_json().get('QINIU_ACCESS_KEY')
        QINIU_SECRET_KEY = request.get_json().get('QINIU_SECRET_KEY')
        QINIU_BUCKET_NAME = request.get_json().get('QINIU_BUCKET_NAME')
        QINIU_BUCKET_DOMAIN = request.get_json().get('QINIU_BUCKET_DOMAINi')
        app.config['QINIU_ACCESS_KEY'] = QINIU_ACCESS_KEY
        app.config['QINIU_SECRET_KEY'] = QINIU_SECRET_KEY
        app.config['QINIU_BUCKET_NAME'] = QINIU_BUCKET_NAME
        app.config['QINIU_BUCKET_DOMAIN'] = QINIU_BUCKET_DOMAIN
        return jsonify({'config': 'ok'}), 200


@app.route('/upload/', methods=['POST', 'GET'])
def upload():
    """
    上传文件到七牛
    """
    if request.method == 'POST':
        # 配置项
        fileobj = request.files['files']  # fileobj待定
        # if file and allowed_file(file.filename, form.filename.data):
        # 七牛文件上传
        qiniu.save(fileobj) # 保存文件到七牛
        return jsonify({}), 200
    else:
        return jsonify({'msg': 'please post the data'}), 405
