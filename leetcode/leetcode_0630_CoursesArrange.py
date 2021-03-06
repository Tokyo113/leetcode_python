

#coding:utf-8
'''
@Time: 2019/11/13 9:20
@author: Tokyo
@file: leetcode_0630_CoursesArrange.py
@desc:
'''

'''
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

思路：
和基本题型安排会议室一样，优先选择结束早的
但存在反例[(5,5),(2,6),(4,6)],按以上的贪心策略只能一门课
所以正确的贪心策略：
已加入的课程按花费时间放入大根堆，新加入一门课程如果超出期限的话
从大根堆弹出一个持续时间最长的课再加入新课程
只要新课程的持续时间小于堆顶，就一定可以加入，
因为新加入的课程的持续时间是一定晚于前面的课程的


'''
import heapq
def coursesArrange(courses):
    heap = []
    courses.sort(key=lambda i:i[1])
    start = 0
    for i in range(len(courses)):
        if start + courses[i][0] <= courses[i][1]:

           start += courses[i][0]
           heapq.heappush(heap, (-courses[i][0], courses[i][1]))
        # 注意已经按照结束时间排过序，后面的结束时间一定更晚，但持续时间又比堆顶的小，就一定可以加入
        elif len(heap) != 0 and -heap[0][0] > courses[i][0]:
            # 堆中第一个值为负，表示持续时间
            # start 减去堆顶的然后加上该课程
            start += heapq.heappop(heap)[0] + courses[i][0]
            heapq.heappush(heap,(-courses[i][0], courses[i][1]))



    return len(heap)


def coursesNum(courses):
    if courses == [] or courses is None:
        return 0
    courses.sort(key=lambda i:i[1])
    start = 0
    heap = []
    for i in range(len(courses)):
        if start+courses[i][0] <= courses[i][1]:
            start += courses[i][0]
            heapq.heappush(heap, [-courses[i][0], courses[i][1]])
        elif courses[i][0] <= -heap[0][0]:
            popCourse = heapq.heappop(heap)
            start = start +popCourse[0] + courses[i][0]
            heapq.heappush(heap, [-courses[i][0], courses[i][1]])
    return len(heap)


if __name__ == '__main__':

    courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    print(coursesArrange(courses))
    print(coursesNum(courses))
    courses1 = [(5,5),(2,6),(4,6)]
    print(coursesArrange(courses1))
    print(coursesNum(courses1))