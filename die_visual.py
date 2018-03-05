# -*- coding:utf-8 -*-
# 3.2 掷骰子
from die import Die

# 创建一个D6实例
die = Die()
# 将掷骰子的结果存储在一个列表中
results = []

# 用for循环 掷骰子100次
for roll_number in range(1000):
    # 掷骰子 方法
    result = die.roll()
    # append()方法添加
    results.append(result)
    
print(results)

# 3.3 分析结果

# 创建空列表 用于存储每种点数出现的次数
frequencies = []

# 遍历可能出现的点数,计算每种点数在results中出现的次数,并附加到空列表frequencies中
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
print(frequencies)

# 3.4 使用pygal可视化包绘制直方图bar
import pygal

# 对结果进行可视化pygal
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = [1, 2, 3, 4, 5, 6]
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')


# 3.5 同时掷两个骰子
print("\n")
from die import Die
import pygal

die_1 = Die()
die_2 = Die()

# 创建空列表记录掷骰子的结果
results= []
for roll_number in range(1000):
    """两个骰子都掷1000次"""
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
print(results)

# 创建空列表存储计算掷骰子的值的次数
frequencies = [] 
for value in range(2, die_1.num_sides+die_2.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
print(frequencies)

# 使用可视化包pygal绘制直方图
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
hist.x_title = "Results"
hist.y_title = "Frequency of Results"

hist.add('D6+D6' ,frequencies)
hist.render_to_file('dice_visual.svg')


# 3.6 同时掷两只不同面数的骰子
print("\n")
from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

results = []
for roll_number in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

frequencies = []

for value in range(2, die_1.num_sides+die_2.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
print(frequencies)

hist = pygal.Bar()

hist.title = "Roll Results of D6 + D10 dice in 1000 times"
hist.x_labels = list(range(2, die_1.num_sides+die_2.num_sides+1))
hist.x_title = "Results"
hist.y_title = "Frequency of Results"

hist.add('D6+D10', frequencies)
hist.render_to_file('dice_different_visual.svg')
