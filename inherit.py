# coding=utf-8


from __future__ import print_function

__metaclass__ = type


class Person:

    def __init__(self):
        print('have two eyes')

    def hobby(self, music):
        print('love %s' % music)

class Rockboy(Person):
    def __init__(self):
        super(Rockboy, self).__init__()
        print ('have a guitar')
    @staticmethod
    def hobby(music):
        print ('love rock and roll: %s'% music)
        print ('love skids')

if __name__ == '__main__':
    boy = Rockboy()
    boy.hobby('fuck you')
    Rockboy.hobby('aaa')