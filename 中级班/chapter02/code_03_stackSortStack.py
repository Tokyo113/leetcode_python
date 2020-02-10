#coding:utf-8
'''
@Time: 2020/2/9 17:58
@author: Tokyo
@file: code_03_stackSortStack.py
@desc:
请编写一个程序，对一个栈里的整型数据，按升序进行排序（即排序前，栈里
的数据是无序的，排序后最大元素位于栈顶），要求最多只能使用一个额外的
栈存放临时数据，但不得将元素复制到别的数据结构中
'''

def sortStack(stack):
    '''
    申请一个辅助栈，从上至下是从小到大，再倒回去即可
    :param stack:
    :return:
    '''
    helper = []
    while stack != []:
        ele = stack.pop()
        while helper != [] and ele > helper[-1]:
            stack.append(helper.pop())

        helper.append(ele)

    while helper != []:
        stack.append(helper.pop())
    return


if __name__ == '__main__':
    stack = [5,2,3,1,7,4,7]
    sortStack(stack)
    print(stack)