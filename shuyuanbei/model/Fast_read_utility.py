import time
import warnings
import os
import sys
from scipy.sparse import csr_matrix, vstack
from multiprocessing import Process, Queue, Manager
import anndata as ad
import sys  
sys.path.append('/opt/model/')
import my_module  # 导入自行编写的动态链接库文件


class Consumer_process_class():  # 定义消费者进程 即每个处理进程类 用于存放数据和处理数据
    def __init__(self, debug=False):
        self.cell_name_list_temp = []  # 存放每个进程接收的 cell_name
        self.sparse_value_temp = None  # 存放每个进程接收的sparse_value
        self.debug = debug

    def run(self, q, memory_queue, end_flag):  # 进程循环运行函数
        while True:
            data = q.get()  # 阻塞 取出队列中的数据
            if data == 'end':  # 数据读取完 接收到end 标志
                memory_queue.put((self.cell_name_list_temp, self.sparse_value_temp))  # 将 进程中处理的所有数据 加入存储队列
                end_flag.put('deal_end')  # 并抛出进程 end标志
                break
            cell_name, sparse_value = my_module.deal_data(data,63561)  # 调用cython程序 返回细胞列表 和 稀疏矩阵
            if self.sparse_value_temp is None:
                self.sparse_value_temp = sparse_value
            else:
                self.sparse_value_temp = vstack((self.sparse_value_temp, sparse_value))
            self.cell_name_list_temp.extend(cell_name)
            if self.debug == True:  # 打印相关信息
                print(sparse_value.shape)
                print(type(sparse_value))
                print('\n', os.getpid(), '进程已处理完批次数据')


def producter_process(filename, per_pocess_deal_row, receive_queue_list, collect_process_data_flag_list, comsumer_njobs,
                      debug=False):  # 生产者 产生数据 queue_list: 存放多个消费者的消息队列
    process_index = 0
    buffer_str_data_list = []  # 缓冲区 存放所有的行数据

    with open(filename, encoding='utf-8', mode='r') as reader:
        row = 0
        if debug == True:
            st_time = time.time()
        for line in reader:
            if row > 0:
                buffer_str_data_list.append(line.encode('utf-8'))
                if row % per_pocess_deal_row == 0:  # 到达每个进程缓冲区的数量 便加入消息队列 进程检测并处理
                    receive_queue_list[process_index].put(buffer_str_data_list)
                    collect_process_data_flag_list[process_index] = True
                    if debug == True:
                        print('读取%d行的时间为:' % (per_pocess_deal_row), time.time() - st_time)
                        st_time = time.time()
                        print('创建进程')
                    process_index += 1
                    buffer_str_data_list = []
                if process_index == comsumer_njobs:  # 开始并行处理数据
                    process_index = 0
            row += 1

    if len(buffer_str_data_list) > 0:  # 剩下没有处理完的 数据 通过消息队列 交给第一个进程处理
        receive_queue_list[0].put(buffer_str_data_list)

    if debug == True:
        print('总行数为', row)
    for item in receive_queue_list:  # 生产者读取完数据后 传递end标志 结束进程
        item.put('end')
    pass


class Fast_read_data():  # 快读函数
    def __init__(self, filename, per_pocess_deal_row, njobs, debug=False):
        self.filename = filename
        self.per_pocess_deal_row = per_pocess_deal_row  # 每个进程处理多少数据
        self.consumer_njobs = njobs - 1  # 一个生产者 进程 7个 消费者进程
        self.cell_name_list = []
        self.sparse_value_arr = None
        self.debug = debug

    def create_and_alloc_process(self):  # 创建进程 定义消息队列

        receive_queue_list = []  # 存放 所有消费者的消息队列列表
        self.memory_queue_list = []  # 存放 所有消费者的数据存储队列列表
        self.process_end_queue_list = []  # 存放 所有消费者的进程结束标志队列列表
        self.process_object_list = []  # 存放 所有创建的消费者进程对象列表
        self.consumer_process_objcet_list = []  # 存放所有的对象
        self.collect_process_data_flag_list = Manager().list([False] * 50) # 用于记录所有进程 是否有处理数据

        for i in range(self.consumer_njobs):  # 创建消费者进程
            receive_queue = Queue()
            memory_queue = Queue()
            end_queue = Queue()

            single_process_class = Consumer_process_class(self.debug)  # 创建消费者进程处理对象
            process = Process(target=single_process_class.run, args=(receive_queue, memory_queue, end_queue,),
                              daemon=True)  # 创建消费者进程
            process.start()  # 开启进程

            self.memory_queue_list.append(memory_queue)
            receive_queue_list.append(receive_queue)
            self.process_end_queue_list.append(end_queue)

            self.process_object_list.append(process)
            self.consumer_process_objcet_list.append(single_process_class)

        productor_process = Process(target=producter_process, args=(
        self.filename, self.per_pocess_deal_row, receive_queue_list, self.collect_process_data_flag_list,
        self.consumer_njobs, self.debug), daemon=True)  # 创建生产者进程
        productor_process.start()  # 开启进程
        productor_process.join()  # 开启进程 阻塞等待生产者进程结束

        self.wait_process_end()  # 阻塞 等待 所有进程处理数据

        return self.cell_name_list, self.sparse_value_arr

    def wait_process_end(self):  # 以阻塞方式等待 消费者进程处理完数据
        for item in self.process_end_queue_list:
            while item.get() != 'deal_end':  # 阻塞等待进程结束
                pass
        print('所有消费者进程处理完毕')
        if self.collect_data() == True:
            self.kill_consumer_process()
        return True

    def collect_data(self):  # 整理所有进程的数据

        index = 0
        for item in self.memory_queue_list:
            if self.collect_process_data_flag_list[index] == True: # 如果进程中有数据 便可以 从该进程收集数据
                while item.qsize():
                    cell_name_list, sparse_value = item.get()
                    self.cell_name_list.extend(cell_name_list)
                    if sparse_value is None:
                        self.sparse_value_arr = sparse_value
                    else:
                        self.sparse_value_arr = vstack((self.sparse_value_arr, sparse_value))
            index += 1
        if self.debug == True:
            print('细胞名称列表长度为:', len(self.cell_name_list))
            print('稀疏矩阵shape为:', self.sparse_value_arr.shape)
        return True

    def kill_consumer_process(self):  # kill消费者进程
        for item in self.process_object_list:
            if item.is_alive():
                item.kill()
        print('所有进程处理和回收完毕')
        return True


def fast_read_data(filename, per_pocess_deal_row=3000, njobs=8, debug=False):
    fast_read_data = Fast_read_data(filename, per_pocess_deal_row=per_pocess_deal_row, njobs=njobs, debug=debug)
    cell_name_list, sparse_value_arr = fast_read_data.create_and_alloc_process()
    adata = ad.AnnData(sparse_value_arr.tocsr())
    adata.obs_names = cell_name_list
    return adata


if __name__ == '__main__':
    st_time = time.time()
    fast_read_data(filename, per_pocess_deal_row=2000, njobs=8, debug=False)
    print(time.time() - st_time)
