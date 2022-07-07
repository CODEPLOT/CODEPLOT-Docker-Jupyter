install.packages("BiocManager")
install.packages('https://mirrors.bfsu.edu.cn/CRAN/src/contrib/mgcv_1.8-34.tar.gz')
install.packages('https://mirrors.bfsu.edu.cn/CRAN/src/contrib/spatial_7.3-13.tar.gz')
install.packages('https://mirrors.bfsu.edu.cn/CRAN/src/contrib/survival_3.2-10.tar.gz')

BiocManager::install(c( "data.table","getopt", "boot", "class", "cluster","codetools", "lattice", "nlme"))
BiocManager::install(c( "nnet", "rpart", "IRdisplay","Matrix","ggplot2"))
BiocManager::install(c("IRkernel","reticulate","remotes","devtools","tidyverse","uuid"))
IRkernel::installspec(user=FALSE)
