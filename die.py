# -*- coding:utf-8 -*-
# 3. 玩转Pygal可视化包

# 3.1 创建Die类
from random import randint

class Die():
    """表示一个骰子的类"""
    
    def __init__(self, num_sides=6):
        """初始化 创建一个6面的骰子"""
        self.num_sides = num_sides
        
    def roll(self):
        """模拟掷骰子,使用randint随机返回1到骰子面数的数"""
        return randint(1, self.num_sides)
        
