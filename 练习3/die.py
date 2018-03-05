# -*- coding:utf-8 -*-

# 模拟掷骰子
from random import randint

class Die():
    """表示一个骰子的类"""
    
    def __init__(self, num_sides=6):
        """初始化骰子 创建一个6面的骰子"""
        self.num_sides = num_sides
        
    def roll(self):
        """模拟掷骰子 使用randint()函数随机返回数值1和骰子面数的值"""
        return randint(1, self.num_sides)
        
# 记住是创建类
