# qiniuAPI

## 七牛配置
+ url: /config/
+ method: POST
+ post data:
    + QINIU_ACCESS_KEY
    + QINIU_SECRET_KEY
    + QINIU_BUCKET_NAME
    + QINIU_BUCKET_DOMAIN
+ return data:
    + 200 ok

## 七牛上传
+ url: /upload/
+ method: POST
+ post data:
    + fileobj 上传的文件对象
+ return data:
    + 200 ok

## Imgur 上传
+ 下载imguru:

```
wget http://downloads.rabien.com/imguru.tar.gz
```

+ 新建过渡文件夹:

```
cd /
mkdir down
```
