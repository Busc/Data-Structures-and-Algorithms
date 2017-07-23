# -*- coding:utf-8 -*-

class Solution(object):

    def __init__(self, random_list):
        self.random_list = random_list

    ##########insertion sort###########

    #基本思想：前面元素已排好序，将当前考察元素插入到前方序列合适的位置
    #时间复杂度：O(n^2)

    def insert_sort(self):
        for i in range(1, len(self.random_list)):  #初始时第一个元素为已排序序列
            current_elem = self.random_list[i]
            j = i
            while j > 0 and self.random_list[j-1] > current_elem:
                self.random_list[j] = self.random_list[j-1]
                j -= 1   #反序比较，确定插入位置
            self.random_list[j] = current_elem
        return self.random_list

    ##########bubble sort###########

    # 基本思想：相邻两元素比较大小，不断减少序列中的逆序；每次完整的扫描都将一个最大元素推到乱序段最右
    # 时间复杂度：O(n^2)

    def bubble_sort(self):   # 注意搞清内外循环次数的设置
        for i in range(0, len(self.random_list)):
            # 发现逆序则需要交换的标志变量exchanges(默认不需要交换)
            exchanges = False
            # 每轮扫描都要进行
            for j in range(1, len(self.random_list)-i):
                if self.random_list[j-1] > self.random_list[j]:
                    self.random_list[j-1], self.random_list[j] = self.random_list[j], self.random_list[j-1]
                    exchanges = True
            if not exchanges:
                break
        return self.random_list

    ##########selection sort#########

    # 基本思想：每次扫描寻找选择最大的元素，从首元素开始，每遇到更大的就更新
    # 时间复杂度：时间复杂度O(n^2)

    def select_sort(self):
        for i in range(len(self.random_list)-1):
            max_ind = 0  # 每次扫描均默认首元素最大
            for j in range(1, len(self.random_list)-i):
                if self.random_list[max_ind] < self.random_list[j]:
                    max_ind = j  # 更新较大值的索引
            # 存放最大值到未排序右端
            self.random_list[max_ind], self.random_list[j] = self.random_list[j], self.random_list[max_ind]
        return self.random_list

    ##########merge sort###########

    # 基本思想：分治法策略进行二路归并，每次操作都是把两个有序序列合并为一个
    # 时间复杂度：O(nlogn)

    def merge_sort(self):
        if len(self.random_list) > 1:
            mid = len(self.random_list) // 2
            left_half = self.random_list[:mid]
            right_half = self.random_list[mid:]
            Solution(left_half).merge_sort()
            Solution(right_half).merge_sort()
            i = j = k = 0
            # 反复复制两分段中最小值
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    self.random_list[k] = left_half[i]
                    i += 1
                else:
                    self.random_list[k] = right_half[j]
                    j += 1
                k += 1
            # 复制前分段剩余数据
            while i < len(left_half):
                self.random_list[k] = left_half[i]
                i += 1
                k += 1
            # 复制后分段剩余数据
            while j < len(right_half):
                self.random_list[k] = right_half[j]
                j += 1
                k += 1
        return self.random_list

    ##########quick sort###########

    # 基本思想：选择最后的元素作为主元，数组划分为四部分“主元+不大于主元+小于主元+未处理”
    # 时间复杂度：O(nlogn)
    def quick_sort(self, begin_ind, end_ind):
        if begin_ind >= end_ind:
            return
        # 选择最后的元素作为主元
        pivot = self.random_list[end_ind]
        # i指向需排序数组首元素之前
        i = begin_ind - 1
        # j初始时指向首元素,随后一直移动到主元前面的元素位置
        for j in range(begin_ind, end_ind):
            if self.random_list[j] < pivot:  # 发现小元素
                i += 1   # i向后移动一个位置
                self.random_list[i], self.random_list[j] = self.random_list[j], self.random_list[i]  # 小元素换位
        # 主元被交换,位于两部分之间,位置索引为i+1
        self.random_list[end_ind], self.random_list[i+1] = self.random_list[i+1], self.random_list[end_ind]
        # 按照相同方式，以递归调用分别处理两部分，直至排序完成
        self.quick_sort(begin_ind, i)
        self.quick_sort(i+2, end_ind)
        return self.random_list


##################测试用例######################
def main():
    random_list = [54, 26, 93, 15, 77, 31, 44, 55, 20]

    #print(Solution(random_list).insert_sort())
    #print(Solution(random_list).bubble_sort())  # 实际效果劣于插入排序
    #print(Solution(random_list).select_sort())  # 不如插入排序
    #print(Solution(random_list).merge_sort())
    print(Solution(random_list).quick_sort(0, len(random_list)-1))

if __name__ == "__main__":
    main()