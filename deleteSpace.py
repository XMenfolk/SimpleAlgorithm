# coding=utf-8

from __future__ import print_function

"""
如果将一句话作为一个字符串，那么这个字符串中必然会有空格（这里仅讨论英文），比如"How are you."，但
有的时候，会在两个单词之间多大一个空格。现在的任务是，如果一个字符串中有连续的两个空格，请把它删除。
"""

string = "I love code."
print(string)

str_lst = string.split(" ")
print(str_lst)

words = [s for s in str_lst if s!=""] #利用列表解析，将空格检出
print(words)

new_string = " ".join(words)
print(new_string)