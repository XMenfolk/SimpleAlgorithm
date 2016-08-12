# coding=utf-8

"""

找出字符串中第一个出现次数为1的字符
"""
def firstCharacter(strstr):
    for s in strstr:
        if strstr.count(s) == 1:
            return s

if __name__ == '__main__':
    print firstCharacter('1cdfg523fdsg1cd')
