# -*- coding:utf-8 -*-
# 使用可视化包pygal进行可视化随机漫步
from random_walk import RandomWalk
import pygal

rw = RandomWalk()
rw.fill_walk()

# 使用pygal.Line()
rw_line = pygal.Line()
rw_line.title = 'Random walk correction'
rw_line.x_title = 'x'
rw_line.y_title = 'y'
# 如何将两个list分解为 (x1, y1) 一一对应

rw_line.add('x_values', rw.x_values)
rw_line.add('y_values', rw.y_values)
rw_line.render_to_file('使用pygal模拟随机漫步.svg')
