# CODEPLOT-Docker-Jupyter


markdown 文件插入链接不能插入http 资源。


列取本地镜像：docker images
镜像构建：docker build -t demo:v1 ./   #./为当前存放Dokcerfile 的路径
运行镜像： docker run -i -t demo:v1
打包容器为镜像： docker commit 87d364e09a17 demo：v1
删除容器： docker rm 87d364e09a17 #87d364e09a17 容器id

