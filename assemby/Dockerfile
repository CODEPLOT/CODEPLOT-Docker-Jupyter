From  docker.io/jupyterhub/k8s-singleuser-sample:v0.2
RUN curl -sSL https://xuzhicheng.obs.cn-north-4.myhuaweicloud.com/software/SOAP -o /usr/bin//SOAP \
   && curl -sSL https://xuzhicheng.obs.cn-north-4.myhuaweicloud.com/software/MECAT2-master.tar.gz -o /opt/MECAT2-master.tar.gz \
   && curl -sSL https://xuzhicheng.obs.cn-north-4.myhuaweicloud.com/software/samtools-1.12.tar.bz2 -o /opt/samtools-1.12.tar.bz2\
   && curl -sSL https://xuzhicheng.obs.cn-north-4.myhuaweicloud.com/software/hifiasm-0.15.4.tar.gz -o /opt/hifiasm-0.15.4.tar.gz \
   && curl -sSL https://xuzhicheng.obs.cn-north-4.myhuaweicloud.com/software/minimap2-2.21.tar.gz -o /opt/minimap2-2.21.tar.gz \
   && curl -sSL https://xuzhicheng.obs.cn-north-4.myhuaweicloud.com/software/wtdbg2-2.5.tar.gz -o /opt/wtdbg2-2.5.tar.gz
RUN cd /opt && chmod 775 /usr/bin//SOAP \
   && apt-get update  \
   && apt-get upgrade -y \
   && apt-get install -y liblzma-dev libbz2-dev zlib1g-dev libncurses5-dev vim less \
   &&  tar -xvf minimap2-2.21.tar.gz \
   && cd minimap2-2.21 && make \
   && mv /opt/minimap2-2.21/minimap2 /usr/bin/. \
   && rm -fr /opt/minimap2-2.21/ \
   && cd /opt/ && tar -xvf wtdbg2-2.5.tar.gz \
   && cd wtdbg2-2.5 && make \
   && cd /opt/ &&  tar jxvf samtools-1.12.tar.bz2 \
   && cd samtools-1.12\
   && ./configure --prefix=/opt/samtools \  
   && make \
   && make install &&  rm -rf /opt/samtools-1.12\
   && cd /opt \
   &&  tar -xvf MECAT2-master.tar.gz \
   && tar -xvf hifiasm-0.15.4.tar.gz \
   && cd hifiasm-0.15.4 \
   && make && mv /opt/hifiasm-0.15.4/hifiasm /usr/bin/.\
   && rm -rf /opt/hifiasm-0.15.4/
ENV PATH /opt/samtools/bin/:/opt/MECAT2-20190314//Linux-amd64/bin:/opt/hifiasm-0.15.4/:$PATH
COPY Assembly /opt/Assembly

