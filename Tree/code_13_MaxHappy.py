#coding:utf-8
'''
@Time: 2019/11/28 18:04
@author: Tokyo
@file: code_13_MaxHappy.py
@desc:

派对的最大快乐值

员工信息的定义如下:
class Employee {
    public int happy; // 这名员工可以带来的快乐值
    List<Employee> subordinates; // 这名员工有哪些直接下级
}

公司的每个员工都符合 Employee 类的描述。整个公司的人员结构可以看作是一棵标准的、 没有环的
多叉树。树的头节点是公司唯一的老板。除老板之外的每个员工都有唯一的直接上级。 叶节点是没有
任何下属的基层员工(subordinates列表为空)，除基层员工外，每个员工都有一个或多个直接下级。

这个公司现在要办party，你可以决定哪些员工来，哪些员工不来。但是要遵循如下规则。
1.如果某个员工来了，那么这个员工的所有直接下级都不能来
2.派对的整体快乐值是所有到场员工快乐值的累加
3.你的目标是让派对的整体快乐值尽量大

给定一棵多叉树的头节点boss，请返回派对的最大快乐值。

'''

class Employee(object):
    def __init__(self, happy, subordinates):
        self.happy = happy
        self.subordinates = subordinates




def happyParty(boss):
    return max(process(boss)[0], process(boss)[1])


def process(employee):
    '''
    返回employee来和不来整棵树的最大快乐值
    :param employee:
    :return: (参加时整棵树的最大值，不参加时整棵树的最大值)
    '''
    if employee.subordinates == None:
        return employee.happy, 0


    lai = employee.happy
    bulai = 0
    for i in employee.subordinates:
        lai += process(i)[1]
        bulai += max(process(i)[0], process(i)[1])

    return lai, bulai




if __name__ == '__main__':
    d = Employee(80, None)
    e = Employee(100, None)
    a = Employee(10, [d])
    b = Employee(5, None)
    c = Employee(150, [e])
    boss = Employee(20, [a, b, c])
    print(happyParty(boss))


