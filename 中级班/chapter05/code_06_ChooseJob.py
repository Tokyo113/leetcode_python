#coding:utf-8
'''
@Time: 2020/2/19 17:49
@author: Tokyo
@file: code_06_ChooseJob.py
@desc:
为了找到自己满意的工作，牛牛收集了每种工作的难度和报酬。牛牛选工作的标准是在难度不超过自身能力
值的情况下，牛牛选择报酬最高的工作。在牛牛选定了自己的工作后，牛牛的小伙伴们来找牛牛帮忙选工作，
牛牛依然使用自己的标准来帮助小伙伴们。牛牛的小伙伴太多了，于是他只好把这个任务交给了你。
class Job {
public int money;// 该工作的报酬
public int hard; // 该工作的难度
public Job(int money, int hard) {
this.money = money;
this.hard = hard;
}
}
给定一个Job类型的数组jobarr，表示所有的工作。给定一个int类型的数组arr，表示所有小伙伴的能力。
返回int类型的数组，表示每一个小伙伴按照牛牛的标准选工作后所能获得的报酬。
'''
import functools
def cmp(a,b):
    if a[0] < b[0] or (a[0]==b[0] and a[1]>b[1]):
        return -1
    elif a[0] == b[0] and a[1] == b[1]:
        return 0
    else:
        return 1


def chooseJobs(job, ability):
    if job == [] or ability == []:
        return None
    job.sort(key=functools.cmp_to_key(cmp))
    jobMap = {}
    jobMap[job[0][0]] = job[0][1]
    pre = job[0][1]
    for i in job[1:]:
        if jobMap.get(i[0]) is None and i[1] > pre:
            jobMap[i[0]] = i[1]
            pre = i[1]

    res = []

    for i in ability:
        while i >= 0:
            if jobMap.get(i) != None:
                res.append(jobMap.get(i))
                break
            else:
                i -= 1
    return res






if __name__ == '__main__':
    a = [[1,2], [2,2], [4,5], [6,8], [3,5], [4,6], [5,8]]
    print(chooseJobs(a,[1,2,3,4]))