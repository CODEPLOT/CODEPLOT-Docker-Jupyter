From  docker.io/jupyterhub/k8s-singleuser-sample:v0.2
RUN apt-get update -qq \
    && apt install -y less vim  
RUN python3 -m pip -V \
 #&& python3 -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple -i https://pypi.tuna.tsinghua.edu.cn/simple\
 #&& python3 -m pip install --upgrade pip -i  http://mirrors.aliyun.com/pypi/simple --trusted-host=mirrors.aliyun.com-i https://pypi.tuna.tsinghua.edu.cn/simple\
 #&& python3 -m pip config set global.index-ur https://mirrors.aliyun.com/pypi/simple-i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install py4j -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install pandas-profiling -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install statsmodels -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install ggplot -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install bokeh -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install pyfasta -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install pdoc3 -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install biopython -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install fastinterval -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install matplotlib-venn -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install h5py -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install html5lib -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install pytz -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install pyvcf -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install theano -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install mkl -i https://pypi.tuna.tsinghua.edu.cn/simple\
 && python3 -m pip install readline \
 && rm -rf /root/.cache/pip/wheels/*
COPY Chamaeleo-master.zip /opt/Chamaeleo-master.zip
RUN cd /opt \
   && unzip Chamaeleo-master.zip \
   && mv Chamaeleo-master Chamaeleo \
   &&  rm Chamaeleo-master.zip \
   && python3 -m pip install terminaltables \
   && apt install -y less vim
ENV PYTHONPATH /opt/:$PYTHONPATH

