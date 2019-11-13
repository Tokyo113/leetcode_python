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

def arrange(programs):
    start = 0
    progarms.sort(key= lambda  i: i.end)
    res = 0
    for i in range(len(progarms)):
        if start <= progarms[i].start:
            res += 1
            start = progarms[i].end
    return res


def all_arrange(programs, n):
    '''
    从所有项目中任选n个的所有可能
    :param programs:
    :param n:
    :return:
    '''
    if n > len(programs):
        return None
    res = []
    # base case
    if n == 1:
        for i in programs:
            res.append([i])

    for j in range(len(programs)):
        others = programs[:j] + programs[j + 1:]
        p = all_arrange(others, n-1)
        for x in p:
            res.append(programs[j:j + 1] + x)


    return res

def baoli_method(programs):
    res = []
    for i in range(1, len(programs)+1):
        res += all_arrange(programs, i)
    set_res = []
    for i in range(len(res)):
        res[i].sort()
    for i in range(len(res)):
        # 去掉相同元素
        if not res[i] in set_res:
            set_res.append(res[i])

    return set_res






'''
同类题：注意思路不一样
这里有 n 门不同的在线课程，他们按从 1 到 n 编号。每一门课程有一定的持续上课时间（课程时间）t 以及关闭时间第 d 天。一门课要持续学习 t 天直到第 d 天时要完成，你将会从第 1 天开始。

给出 n 个在线课程用 (t, d) 对表示。你的任务是找出最多可以修几门课。

 

示例：

输入: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
输出: 3
解释: 
这里一共有 4 门课程, 但是你最多可以修 3 门:
首先, 修第一门课时, 它要耗费 100 天，你会在第 100 天完成, 在第 101 天准备下门课。
第二, 修第三门课时, 它会耗费 1000 天，所以你将在第 1100 天的时候完成它, 以及在第 1101 天开始准备下门课程。
第三, 修第二门课时, 它会耗时 200 天，所以你将会在第 1300 天时完成它。
第四门课现在不能修，因为你将会在第 3300 天完成它，这已经超出了关闭日期。
 

提示:

整数 1 <= d, t, n <= 10,000 。
你不能同时修两门课程。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



'''
if __name__ == '__main__':
    pro1 = Program(1,2.5)
    pro2 = Program(2,2.5)
    pro3 = Program(3, 5.5)
    pro4 = Program(4,8.5)
    pro5 = Program(1,1.5)
    pro6 = Program(3,7.5)
    progarms = [pro1, pro2, pro3, pro4, pro5, pro6]
    print(arrange(progarms))
    a = [1,2,3,4]
    b = [(1,3), (3,5), (3,6), (4,7)]
    print(len(baoli_method(b)))




