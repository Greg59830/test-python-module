# -*- coding: utf-8 -*-
def fact_mission():
  n=int(input("Choose a number: "))
  fact= int(input("chooose a factorial: "))

  for i in range(1,n+1):
    fact=fact*i
  print(fact)
print(fact_mission())