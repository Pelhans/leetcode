#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    def Clone(self, head):
        if head is None:
            return None
        labelList = []
        nodeList = []
        randomList = []
        tmp = head
        while tmp:
            nodeList.append(tmp)
            labelList.append(tmp.label)
            randomList.append(tmp.random)
            tmp = tmp.next
        randomToNode = map(lambda c: nodeList.index(c) if c in nodeList else -1, randomList)
        emptyNode = RandomListNode(None)
        pre = emptyNode
        nodeList = map(lambda c: RandomListNode(c), labelList)
        for idx,node in enumerate(nodeList):
            if randomToNode[idx] != -1:
                node.random = nodeList[randomToNode[idx]]
            pre.next = node
            pre = pre.next
        return emptyNode.next
