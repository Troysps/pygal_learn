# -*- coding:utf-8 -*-
# 使用matplotlib模拟掷骰子
from die import Die
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 模拟一个D6掷骰子
# 创建实例
die_1 = Die()
results_1 = [die_1.roll() for roll_number in range(1000)]
frequencies_1 = [results_1.count(value) for value in range(1, die_1.num_sides+1)]

# 确定x值和y值 x是1-6 y是1-6数值之间出现的频数
x_values_1 = list(range(1, die_1.num_sides+1))
y_values_1 = frequencies_1
plt.bar(x_values_1, y_values_1, width=0.5, fc='g')

plt.title('模拟掷1个D6骰子', fontsize=24)
plt.xlabel('骰子面', fontsize=14)
plt.ylabel('频数', fontsize=14)
plt.show()

# 模拟两个D6掷骰子 这里需要导入numpy进行排序 方便些
die_2 = Die()
results_2 = [die_2.roll() for roll_number in range(1000)]
frequencies_2 = [results_2.count(value) for value in range(1, die_2.num_sides+1)]

# 这里x加0.4 是为了不重叠x轴上的值
x_values_2 = [x+0.4 for x in range(1, die_1.num_sides+1)]
y_values_2 = frequencies_2
total_width, n = 0.8, 2
width = total_width / n


plt.bar(x_values_1, y_values_1, label='a', width=width, fc='g')
plt.bar(x_values_2, y_values_2, label='b', width=width, fc='r')
plt.title('模拟掷2个D6骰子', fontsize=24)
plt.xlabel('骰子面', fontsize=14)
plt.ylabel('频数', fontsize=14)
plt.legend()
plt.show()
