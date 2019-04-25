#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return "".join([chr(ord(i) + 32)  if (ord(i) >= 65 and ord(i) <= 90) else i for i in list(str)])
