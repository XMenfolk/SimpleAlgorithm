# coding=utf-8


from __future__ import print_function
from __future__ import division
import random

"""
按照下面的要求实现对列表的操作：
1. 产生一个列表，其中有 40 个元素，每个元素是 0 到 100 的一个随机整数
2. 如果这个列表中的数据代表着某个班级 40 人的分数，请计算成绩低于平均分的学生人数，并输出
3. 对上面的列表元素从大到小排序
"""

# 0到100之间，随机得到40个整数，组成列表
score = [random.randint(0, 100) for i in range(40)]
print(score)

num = len(score)  # 学生人数
sum_score = sum(score)  # 对列表中的整数求和
ave_score = sum_score / num  # 计算平均数
less_score = [i for i in score if i < ave_score]  # 找出小于平均分的学生分数，组成列表
less_score_num = len(less_score)  # 计算成绩低于平均分的学生人数

print('平均分是：%.1f' % ave_score)
print('成绩小于平均分的学生人数：%d' % less_score_num)

sorted_score = sorted(score, reverse=True)  # 对元列表元素排序
print(sum_score)
