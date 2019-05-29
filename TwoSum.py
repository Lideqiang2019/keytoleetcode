#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def __init__(self,nums,target):
        self.nums=nums
        self.target=target

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            """
            enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
            同时列出数据和数据下标，一般用在 for 循环当中
            返回值是数组和数值
            >>>seq = ['one', 'two', 'three']
            >>> for i, element in enumerate(seq):
            print i, element
            """

            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None

    """
    用遍历的方法，将目标target与所取的数进行比对，如果满足条件则输出
    满足条件的下标
    """
nums=[2,4,6,9]
target=15
L=Solution(nums,target)
print(L.twoSum(nums,target))

