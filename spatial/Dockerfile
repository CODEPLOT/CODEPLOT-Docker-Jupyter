From  docker.io/jupyterhub/k8s-singleuser-sample:v0.2
RUN apt-get update -qq \
    && apt install -y less vim  
RUN apt-get update -qq\
    && apt install -y --no-install-recommends software-properties-common dirmngr gnupg default-jre default-jdk\
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9\
    && add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran40/'\
    && add-apt-repository 'deb http://us.archive.ubuntu.com/ubuntu/ bionic main restricted'\
    && apt-get install -yq --no-install-recommends apt-transport-https libicu60\
    && apt-get install -yq r-base \
    && apt-get clean
ENV JUPYTER_ALLOW_INSECURE_WRITES=False
RUN  R -e 'source("https://xuzhicheng.obs.cn-north-4.myhuaweicloud.com/seurat.R")' 
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
RUN  python3 -m pip install scanpy -i https://pypi.tuna.tsinghua.edu.cn/simple 
RUN python3 -m pip install scgen  -i https://pypi.tuna.tsinghua.edu.cn/simple \
  && python3 -m pip install stereopy -i https://pypi.tuna.tsinghua.edu.cn/simple 
RUN R -e 'install.packages("harmony")'\
  && R -e 'install.packages("rliger")' \
  && R -e 'devtools::install_github("dmcable/spacexr", build_vignettes = FALSE)'\
  && R -e 'library(devtools);install_github("https://github.com/MarcElosua/SPOTlight",upgrade ="never")' 
RUN cd /opt \
  && git clone https://github.com/almaan/stereoscope \
  && cd stereoscope\
  && ./setup.py install 
RUN cd /opt \
  && git clone https://github.com/MarioniLab/MNN2017/

COPY example /opt/example/data
