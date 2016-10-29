# coding: utf-8

from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key is here'
app.config['QINIU_ACCESS_KEY'] = "7mVlJlbLcnr1m-FbsvOtFlT8aC-6rGBWkdUH0BD6"
app.config['QINIU_SECRET_KEY'] = "LpuwHp2mECopFk0oPpGbLyjU_tK5ggdwygr0F87r"
app.config['QINIU_BUCKET_NAME'] = "neo1218"
app.config['QINIU_BUCKET_DOMAIN'] = "7xj431.com1.z0.glb.clouddn.com"

from . import views
