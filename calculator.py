# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 00:52:26 2019

@author: Brian
"""

class Calculator:
    def __init__(self,NumberList):
        self.NumberList = NumberList
        
    def sum(self):
        result = 0
        for num in self.NumberList:
            result += num
        return result
    
    def avg(self):
        total = self.sum()
        return total / len(self.NumberList)
    
    
    
cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

for i in range(10):
    print(cal1.sum())


cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())
