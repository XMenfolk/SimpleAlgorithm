# coding=utf-8

"""
统计考试成绩
"""

from __future__ import division


def average_score(scores):
    """
    统计平均分
    :param scores:
    :return:
    """
    score_values = scores.values()
    sum_scores = sum(score_values)
    average = sum_scores / len(score_values)
    return average


def sorted_score(scores):
    """
    对成绩从高到低排序
    :param scores:
    :return:
    """

    score_lst = [(scores[k], k) for k in scores]
    sort_lst = sorted(score_lst, reverse=True)
    return [(i[1], i[0]) for i in sort_lst]


def max_score(scores):
    """
    成绩最高的姓名和分数.
    """
    lst = sorted_score(scores)  # 引用分数排序的函数 sorted_score
    max_score = lst[0][1]
    return [(i[0], i[1]) for i in lst if i[1] == max_score]


def min_score(scores):
    """
    成绩最低的姓名和分数.
    """
    lst = sorted_score(scores)
    min_score = lst[len(lst) - 1][1]
    return [(i[0], i[1]) for i in lst if i[1] == min_score]


if __name__ == "__main__":
    examine_scores = {"google": 98, "facebook": 99, "baidu": 52,
                      "alibaba": 80, "yahoo": 49, "IBM": 70,
                      "android": 76,"apple": 99, "amazon": 99}
    ave = average_score(examine_scores)
    print "the average score is: ", ave  # 平均分
    sor = sorted_score(examine_scores)
    print "list of the scores: ", sor  # 成绩表
    xueba = max_score(examine_scores)
    print "Xueba is: ", xueba  # 学霸们
    xuezha = min_score(examine_scores)
    print "Xuzha is: ", xuezha  # 学渣们
