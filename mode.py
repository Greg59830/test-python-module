# -*- coding: utf-8 -*-
def mode_value(ls):
  count= {}
  for i in ls:
    if i in count:
      count[i]+=1
  else:
     count[i]=1

  return [key for key in count.keys() if count[key] == max(count.values())]
print(mode_value([2,2,4,5,5,2,6,1,1,2]))
