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
RUN R -e 'source("https://xuzhicheng.obs.cn-north-4.myhuaweicloud.com/baser.R")' 

