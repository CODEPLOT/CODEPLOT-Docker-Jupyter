# -*- coding: utf-8 -*-
import time
import scanpy as sc
import os
import sys
import pandas as pd
import warnings
import parc

from Fast_read_utility import fast_read_data # 导入自定义快读类
warnings.simplefilter('ignore')
print(sys.path)



def cell_qc(adata): # 质控
    sc.pp.filter_genes(adata, min_cells=5)  # 每一个基因至少在5个细胞中表达
    # adata.var['mt'] = adata.var_names.str.startswith('MT-')    # 抽取带有MT的字符串
    # sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)    # 数据过滤
    # adata = adata[adata.obs.pct_counts_mt < 5, :] # 提取线粒体dna在5%以下
    return adata

def preprocessing_data(adata): # 标准化 并 提取高变基因 并降维
    sc.pp.normalize_total(adata, target_sum=1e4)  # 每个细胞的基因表达的数量综合为target_sum
    sc.pp.log1p(adata)  # 取对数
    sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=5.5, min_disp=0.5)  # 5
    adata = adata[:, adata.var.highly_variable]     # 提取高变基因
    sc.pp.scale(adata, max_value=10, zero_center=False)    # 中心化
    sc.tl.pca(adata, svd_solver='arpack', use_highly_variable=True, n_comps=50)  # PCA
    return adata

def deal_data(adata,result_filename):

    adata = cell_qc(adata) # 质控
    adata = preprocessing_data(adata) # 预处理 标准化

    parc_obj = parc.PARC(adata.obsm['X_pca'], jac_std_global=0.15, random_seed=1, small_pop=150,resolution_parameter = 0.48,num_threads=8,knn = 30,n_iter_leiden=5,distance='cosine',jac_weighted_edges=True,hnsw_param_ef_construction = 180)
    parc_obj.run_PARC()
    parc_labels = parc_obj.labels
    adata.obs["PARC"] = pd.Categorical(parc_labels)

    category_class = adata.obs['PARC']
    category_class = {'Cell': category_class.index, 'Lable': category_class.values}
    category_class = pd.DataFrame(category_class)

    category_class.to_csv(result_filename, index=None,encoding='utf-8')


def main(to_pred_dir,result_save_path):
    data_filename = os.path.join(to_pred_dir,"dataset.csv")
    # info_filename = os.path.join(to_pred_dir,"add_info.csv")

    adata = fast_read_data(data_filename,per_pocess_deal_row=1000,njobs=8,debug=False) # debug 设置为True可以打印详细信息

    deal_data(adata,result_save_path)


if __name__ == "__main__":
    to_pred_dir = sys.argv[1]  # 所需预测的文件夹路径
    result_save_path = sys.argv[2]  # 预测结果保存文件路径

    main(to_pred_dir, result_save_path)
