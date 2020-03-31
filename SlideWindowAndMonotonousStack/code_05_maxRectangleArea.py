#coding:utf-8
'''
@Time: 2020/3/31 21:34
@author: Tokyo
@file: code_05_maxRectangleArea.py
@desc:
'''


def largestRectangleArea(heights):
    if heights == None or heights == []:
        return 0

    stack = []
    maxArea = 0
    for i in range(len(heights)):
        while stack != [] and heights[i] <= heights[stack[-1]]:
            pp = stack.pop()
            left = -1 if stack == [] else stack[-1]
            right = i
            maxArea = max(maxArea, (right-left-1)*heights[pp])
        stack.append(i)

    while stack != []:
        pp = stack.pop()

        left = -1 if stack == [] else stack[-1]
        maxArea = max(maxArea, (len(heights)-left-1)*heights[pp])
    return maxArea








if __name__ == '__main__':
    arr = [2,1,5,6,2,3]
    print(largestRectangleArea(arr))
