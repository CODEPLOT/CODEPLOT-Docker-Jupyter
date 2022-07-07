From  docker.io/jupyterhub/k8s-singleuser-sample:v0.2
RUN apt-get update -qq \
    && apt install -y less vim python2.7 python2.7-dev libncurses5-dev
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py\
   && python2.7 get-pip.py\
   && python2.7 -m pip install ipykernel\
   && python2.7 -m ipykernel install --name python2
RUN python2.7  -m pip install --upgrade pip \
 #&& python2 -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple -i https://pypi.tuna.tsinghua.edu.cn/simple\
 #&& python2 -m pip install --upgrade pip -i  http://mirrors.aliyun.com/pypi/simple --trusted-host=mirrors.aliyun.com-i https://pypi.tuna.tsinghua.edu.cn/simple\
 #&& python2 -m pip config set global.index-ur https://mirrors.aliyun.com/pypi/simple-i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python2.7 -m pip install pathlib \
 && python2.7 -m pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python2.7 -m pip install py4j -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python2.7 -m pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python2.7 -m pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python2.7 -m pip install bokeh -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python2.7 -m pip install pyfasta -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python2.7 -m pip install markdown -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python2.7 -m pip install pdoc3 -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python2.7 -m pip install fastinterval -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python2.7 -m pip install matplotlib-venn -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python2.7 -m pip install h5py -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python2.7 -m pip install html5lib -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python2.7 -m pip install keras -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python2.7 -m pip install Cython -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python2.7 -m pip install pyvcf -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python2.7 -m pip install theano -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python2.7 -m pip install readline 

