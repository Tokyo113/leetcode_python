#coding:utf-8
'''
@Time: 2019/11/17 10:48
@author: Tokyo
@file: code_05_ReverseStackUsingRecursive.py
@desc:
'''

def reverse(stack):
    if len(stack) == 0 or stack is None:
        return None
    p = getAndRemoveLastElement(stack)
    reverse(stack)
    stack.append(p)





def getAndRemoveLastElement(stack):
    if len(stack) == 0:
        return None
    res = stack.pop()
    if len(stack) == 0:
        return res
    else:
        last = getAndRemoveLastElement(stack)
        stack.append(res)
        return last



if __name__ == '__main__':
    a = [1,2,3,4,5]
    reverse(a)
    print(a)