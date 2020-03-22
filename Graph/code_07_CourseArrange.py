#coding:utf-8
'''
@Time: 2020/3/19 17:27
@author: Tokyo
@file: code_07_CourseArrange.py
@desc:
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例 1:

输入: 2, [[1,0]]
输出: [0,1]
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
示例 2:

输入: 4, [[1,0],[2,0],[3,1],[3,2]]
输出: [0,1,2,3] or [0,2,1,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
     因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。

拓扑排序
'''
import collections
def courses(n,courses):
    if n == 1:
        return [0]
    # 图
    courseMap = collections.defaultdict(list)
    zeroInQueue = []
    inMap = {}

    for b,a in courses:
        # 建立图
        courseMap[a].append(b)
        # 统计每个节点的入度
        inMap[b] = inMap.get(b,0)+1

    for i in range(n):
        if inMap.get(i) is None:
            zeroInQueue.append(i)

    print(courseMap)
    print(inMap)
    res = []
    while zeroInQueue != []:
        ele = zeroInQueue.pop(0)
        res.append(ele)
        print(ele)

        # 最后一个节点没有next，所以不在courseMap中
        if courseMap.get(ele) != None:
            for i in courseMap.get(ele):
                inMap[i] -= 1
                if inMap.get(i) == 0:
                    zeroInQueue.append(i)
    return res if len(res) == n else []


if __name__ == '__main__':
    print(courses(4, [[1,0],[2,0],[3,1],[3,2]]))


