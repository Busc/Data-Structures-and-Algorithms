# -*- coding:utf-8 -*-

#################二分查找#################

# 适用条件：有序线性表(这里假设数据升序排列)
# 基本思想：按比例逐步缩小需要考虑的数据范围，以快速逼近需要找的数据
# 时间复杂度：O(logn)

def binary_search(random_list, item):
    first_ind, last_ind = 0, len(random_list)-1  # 初始时考虑的区间是整个序列
    item_index = None
    while first_ind <= last_ind:
        # 取待考察区间的中间项索引
        mid_index = (first_ind + last_ind)//2
        if random_list[mid_index] == item:
            item_index = mid_index
            break
        else:
            if random_list[mid_index] < item:
                first_ind = mid_index + 1
            else:
                last_ind = mid_index - 1
    return item_index

#################测试用例#################
random_list = [0, 1, 2, 8, 13, 17, 19, 32, 42, 42]
print(binary_search(random_list, 42))
print(binary_search(random_list, 3))
print(binary_search(random_list, 13))


