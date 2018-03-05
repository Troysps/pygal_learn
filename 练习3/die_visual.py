# -*- coding:utf-8 -*-
# 使用pygal可视化包 对掷骰子的结果进行汇总成直方图
from die import Die
import pygal

die_1 = Die()
# 列表生成式
results_1 = [die_1.roll() for roll_number in range(1000)]


frequencies_1 = [results_1.count(value) for value in range(1, die_1.num_sides+1)]

    
# 使用pygal进行可视化 条形图

hist_1 = pygal.Bar()

hist_1.title = '掷D6骰子100次的频数分布'
hist_1.x_labels = list(range(1 , die_1.num_sides+1))
hist_1.x_title = '数值'
hist_1.y_title = '频次'

hist_1.add('D6', frequencies_1)
hist_1.render_to_file('die_visual.svg')

# 创建两个D8骰子 基本条形图之复合条形图
die_2 = Die(8)
die_3 = Die(8)

results_2 = [die_2.roll() for roll_number in range(1000)]
results_3 = [die_3.roll() for roll_number in range(1000)]
frequencies_2 = [
    results_2.count(value) for value in range(1 ,die_2.num_sides+1)
        ]
frequencies_3 = [
    results_3.count(value) for value in range(1 ,die_3.num_sides+1)
        ]
        
hist_2 = pygal.Bar()


hist_2.title = '掷两个D8骰子1000次的频数分布'
hist_2.x_labels = list(range(1 , die_2.num_sides+1))
hist_2.x_title = '数值'
hist_2.y_title = '频次'


# add()增加两个不同个体的观测值集合 形成复合条形图
hist_2.add('一个D8', frequencies_2)
hist_2.add('另一个D8', frequencies_3)
hist_2.render_to_file('two_D8_visual_pygal_Bar.svg')


# 层叠条形图 使用函数pygal.StackedBar()
hist_3 = pygal.StackedBar()

hist_3.title = '掷两个D8骰子1000次的频数分布'
hist_3.x_labels = list(range(1 , die_2.num_sides+1))
hist_3.x_title = '数值'
hist_3.y_title = '频次'

hist_3.add('一个D8', frequencies_2)
hist_3.add('另一个D8', frequencies_3)
hist_3.render_to_file('two_D8_visual_pygal_StackedBar.svg')

# 水平条形图 使用函数pygal.HorizontalBar()构建水平条形图
hist_4 = pygal.HorizontalBar()

hist_4.title = '掷两个D8骰子1000次的频数分布,其中1值出现的频次'


hist_4.add('一个D8', results_2.count(1))
hist_4.add('另一个D8', results_3.count(1))
hist_4.render_to_file('two_D8_visual_pygal_HorizontalBar.svg')

# pygal可视化真的好看

# 同时掷三个D6骰子
die_4 = Die()
die_5 = Die()
die_6 = Die()

results = [
    die_4.roll()+die_5.roll()+die_6.roll()
    for roll_number in range(1000)
    ]
    
frequencies_4 = [
    results.count(value)
    for value in range(3, die_4.num_sides+die_4.num_sides+die_6.num_sides+1)
    ]

# 如何将列表中的值求得sum print(sum(list))

pie_1 = pygal.Pie()
pie_1.title = '三个D6骰子之和各值的比例分布'
pie_1.add('和为3', frequencies_4[0]/1000)
pie_1.add('和为4', frequencies_4[1]/1000)
pie_1.add('和为5', frequencies_4[2]/1000)
pie_1.add('和为6', frequencies_4[3]/1000)
pie_1.add('和为7', frequencies_4[4]/1000)
pie_1.add('和为8', frequencies_4[5]/1000)
pie_1.add('和为9', frequencies_4[6]/1000)
pie_1.add('和为10', frequencies_4[7]/1000)
pie_1.add('和为11', frequencies_4[8]/1000)
pie_1.add('和为12', frequencies_4[9]/1000)
pie_1.add('和为13', frequencies_4[10]/1000)
pie_1.add('和为14', frequencies_4[11]/1000)
pie_1.add('和为15', frequencies_4[12]/1000)
pie_1.add('和为16', frequencies_4[13]/1000)
pie_1.add('和为17', frequencies_4[14]/1000)
pie_1.add('和为18', frequencies_4[15]/1000)

pie_1.render_to_file('sum_of_three_D6_pie.svg')
# 可以进行更进一步的分割 运用四分位数的概念 将数值划分开来 更易于理解其数值之和的分布
pie_2 = pygal.Pie()

pie_2.title = '运用四分位数进行可视化图形'
pie_2.add('骰子面数之和在3-6之间', sum(frequencies_4[0:4])/1000)
pie_2.add('骰子面数之和在7-10之间', sum(frequencies_4[4:8])/1000)
pie_2.add('骰子面数之和在11-14之间', sum(frequencies_4[8:12])/1000)
pie_2.add('骰子面数之和在15-18之间', sum(frequencies_4[12:16])/1000)

pie_2.render_to_file('使用四分位数进行可视化图形.svg')


# 同时掷两个骰子将点数相乘
die_7 = Die()
die_8 = Die()

results_4 = [
    die_7.roll()*die_8.roll()
    for roll_number in range(1000)
    ]
    
frequencies_5 = [
    results_4.count(value)
    for value in range(1, die_7.num_sides*die_8.num_sides+1)
    ]
    
# 玩条形图
hist_5 = pygal.Bar()
hist_5.title = '两个D6骰子随机数值乘积分布'
hist_5.x_title = '相乘数值'
hist_5.y_title = '频数'
hist_5.x_labels = list(range(1, die_7.num_sides*die_8.num_sides+1))

hist_5.add('D6*D6', frequencies_5)
hist_5.render_to_file('两个D6骰子随机数值乘积分布.svg')
 
