#coding:utf-8
'''
@Time: 2019/11/11 14:25
@author: Tokyo
@file: code_02_BestArrange.py
@desc:
'''

class Program(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def bestArrange(programs, start):
    # 优先安排结束时间早的program
    programs.sort()
    res = 0
    for i in range(len(programs)):
        if start <= programs[i].start:
            res += 1
            start = programs[i].end

    return res

if __name__ == '__main__':
    pro1 = Program(1,2.5)
    pro2 = Program(2,2.5)
    pro3 = Program(3, 5.5)
    pro4 = Program(4,8.5)
    pro5 = Program(1,1.5)
    pro6 = Program(3,7.5)
    progarms = [pro1, pro2, pro3, pro4, pro5, pro6]
    print(bestArrange(progarms, 0.5))



