# -*- coding: utf-8 -*-
def absolute_mission ():
  n=int(input("choose a number: "))
  if n > 0:
      print(n)
  else:
      print(0-n)
  return absolute_mission

print(absolute_mission())