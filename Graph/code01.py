#coding:utf-8
'''
@Time: 2020/4/12 15:53
@author: Tokyo
@file: code01.py
@desc:
'''

def huochai(strs):
    if strs is None or strs == '':
        return -1
    return process(strs,0,'',0)

def process(strs,i,cur,state):


