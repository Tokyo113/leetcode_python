#coding:utf-8
'''
@Time: 2019/11/17 10:48
@author: Tokyo
@file: code_05_ReverseStackUsingRecursive.py
@desc:
给你一个栈，请你逆序这个栈，不能使用额外的数据结构，只能使用递归函数

1.取出栈底的元素
2.逆序剩余部分
3.将该元素放到栈顶
'''

def reverseStack(stack):
    if len(stack) <= 1 or stack is None:
        return

    ele = helper(stack)
    reverseStack(stack)
    stack.append(ele)


def helper(stack):
    if len(stack) == 1:
        return stack.pop()
    res = stack.pop()
    last = helper(stack)
    stack.append(res)
    return last







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
    # reverse(a)
    reverseStack(a)
    print(a)