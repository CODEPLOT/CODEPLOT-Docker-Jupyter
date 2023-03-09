# CODEPLOT-Docker-Jupyter
Docker，也称为基础映像，就像一台新服务器，预装了分析所必须最小化的软件配置，所以它很轻，可以快速且廉价地运行。从技术上讲，它与虚拟机 (VM) 不同（它更小更轻），

当你制作一个 Docker“镜像”时，你是在一个虚拟“容器”中设置一个计算机系统，你可以复制它并在任何其他机器上运行——而不用担心它运行的是什么类型的系统。


在基础镜像上，比如Ubuntu，先登录镜像系统并安装Docker软件，然后整体制作镜像快照。方式如下：
### 一:基于DockerFile 构建镜像

1）找一台主机，安装Docker软件。


2）新建工作目录；创建 Dockerfile 文件，示例可以参考仓库其他镜像

3）构建镜像

docker build -t repo:tag .
命令参数：
  
repo：是存储 Docker 的存储库的名称（可以是现有存储库或将 Docker 推送到 Docker Hub 时创建的存储库的名称）。
  
tag:是有助于识别特定图像的关键字或版本号。
  
. 存放Dockerfile 路径
  
### 二:基于容器快照 构建镜像（不推荐；可以作为的一种的测试验证）
1）找一台主机，安装Docker软件。
  
2）启动CODEPLOT提供的基础镜像。再基础镜像执行安装任务
  
3）输入exit退出容器。
  
4）提交容器形成镜像快照：docker commit
  
docker commit <容器id> <repo>:<tag>
  
4）执行docker images可以查看到制作完成的Docker镜像
  
  
  ### 命令集
  列取本地镜像：docker images

镜像构建：docker build -t demo:v1 ./   #./为当前存放Dokcerfile 的路径

运行镜像： docker run -i -t demo:v1

打包容器为镜像： docker commit 87d364e09a17 demo：v1

删除容器： docker rm 87d364e09a17 #87d364e09a17 容器id
