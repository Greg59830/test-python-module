# -*- coding: utf-8 -*-

def max_misson ():
  list1 = []
  n = int(input("Enter number of elements in list: "))
  for i in range(1, n+1):
    element=int(input("Enter elements: "))
    list1.append(element)
  print("Largest element is: ", max(list1))

print(max_misson())