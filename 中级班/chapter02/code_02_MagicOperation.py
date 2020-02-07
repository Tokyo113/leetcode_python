#coding:utf-8
'''
@Time: 2020/2/7 18:22
@author: Tokyo
@file: code_02_MagicOperation.py
@desc:
给一个包含n个整数元素的集合a，一个包含m个整数元素的集合b。
定义magic操作为，从一个集合中取出一个元素，放到另一个集合里，且操作过
后每个集合的平均值都大大于于操作前。
注意以下两点：
1）不可以把一个集合的元素取空，这样就没有平均值了
2）值为x的元素从集合b取出放入集合a，但集合a中已经有值为x的元素，则a的
平均值不变（因为集合元素不会重复），b的平均值可能会改变（因为x被取出
了）
问最多可以进行多少次magic操作？
'''

def magicOp(a,b):
    avg_a = avg(sum(a), len(a))
    avg_b = avg(sum(b), len(b))
    if avg_a == avg_b:
        return 0
    if avg_a < avg_b:
        # 保证a是大集合，b是小集合
        a, b = b, a
    a.sort()
    sumA, lenA = sum(a), len(a)
    sumB, lenB = sum(b), len(b)
    op = 0
    for i in a:
        if i > avg(sumB, lenB) and i < avg(sumA, lenA) and i not in b:
            sumA -= i
            lenA -= 1
            sumB += i
            lenB += 1
            op += 1
            b.append(i)

    return op
def avg(sum,length):
    return sum/length

if __name__ == '__main__':
    a = [1,2,5]
    b = [2,3,4,5,6]
    print(magicOp(a,b))








