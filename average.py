# -*- coding: utf-8 -*-
def average_mission(n):
  #n as number a for average value in loop
  sum_n = 0
  for a in n:
    sum_n = sum_n + a
    aver = sum_n / len(n)
    return aver
  print(aver)
average_mission (([11,21,31,41])) 