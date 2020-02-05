#coding:utf-8
'''
@Time: 2019/11/27 14:16
@author: Tokyo
@file: code_02_MonotonousStack.py
@desc:
'''


def getNearLessNoRepeat(arr):
    '''
    没有重复值的求解两边小于它的数的index
    注意单调栈中存放的是下标index
    主要分为三个部分
    1. 弹出不合规的元素
    2.入栈
    3.清算
    :param arr:
    :return:
    '''
    res = [[-1,-1] for i in range(len(arr))]
    stack = []

    for i in range(len(arr)):
        # 1.弹出不合规的元素，并生成结果
        while (len(stack) != 0) and (arr[i] < arr[stack[-1]]):
            popIndex = stack.pop()
            leftIndex = stack[-1] if stack != [] else -1
            res[popIndex][0] = leftIndex
            res[popIndex][1] = i
        # 入栈
        stack.append(i)
    # 清算
    while stack != []:
        popIndex = stack.pop()
        leftIndex = stack[-1] if stack != [] else -1
        res[popIndex][0] = leftIndex
        res[popIndex][1] = -1
    return res



def getNearLess(arr):
    '''
    含有重复值的情况
    此时单调栈中存放的是list[]
    :param arr:
    :return:
    '''
    res = [[-1,-1] for i in range(len(arr))]
    stack = []
    for i in range(len(arr)):
        while stack != [] and arr[i] < arr[stack[-1][0]]:
            popList = stack.pop()
            # 取被压在下面的列表中最晚加入的那个
            leftIndex = stack[-1][-1] if stack != [] else -1
            # 对poplist中每个元素添加信息
            for popi in popList:
                res[popi][0] = leftIndex
                res[popi][1] = i
        # 入栈
        if stack != [] and arr[stack[-1][0]] == arr[i]:
            stack[-1].append(i)
        else:
            stack.append([i])


    # 结算
    while stack != []:
        popList = stack.pop()
        leftIndex = stack[-1][-1] if stack != [] else -1
        for popi in popList:
            res[popi][0] = leftIndex
            res[popi][1] = -1

    return res




def baoli(arr):
    '''
    暴力解法，O(N2)
    :param arr:
    :return:
    '''
    res = [[-1,-1] for i in range(len(arr))]

    for i in range(len(arr)):
        for pre in range(i-1,-1,-1):
            if arr[pre] < arr[i]:
                res[i][0] = pre
                break

        for last in range(i+1,len(arr)):
            if arr[last] < arr[i]:
                res[i][1] = last
                break

    return res






def generateRandomArray(maxSize, maxValue):
    import random
    random_list = []
    for i in range(int((maxSize+1)*random.random())):
        random_list.append(int((maxValue+1)*random.random())-int(maxValue*random.random()))
    return random_list





if __name__ == '__main__':
    testTime = 5000
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(0, testTime):
        arr1 = generateRandomArray(maxSize, maxValue)


        a = dandiaozhan(arr1)
        b = baoli(arr1)

        if (a != b):
            succeed = False
            print(arr1)
            print('right ans', baoli(arr1))
            print('your ans', getNearLess(arr1))
            break
    print("Nice!" if succeed else "Fucking fucked")





