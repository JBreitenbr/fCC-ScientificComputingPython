import copy
import random

class Hat:
  def __init__(self,**kwargs):
    d=dict(**kwargs)
    contents=[]
    for k in d.keys():
      for v in range(d[k]):
        contents.append(k)
    self.contents=contents

  def draw(self,num):
    cnt=self.contents
    l=len(cnt)
    smp=[]
    if num >= l:
      return cnt
    else:
      for i in range(num):
        rnd=random.randint(0,l-1)
        smp.append(cnt.pop(rnd))
        l=l-1
    return smp

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  l_exp=[]
  succ=0
  for key in expected_balls:
    l_exp.append(expected_balls[key])
  
  for i in range(num_experiments):
      new = copy.deepcopy(hat)
      drawn=new.draw(num_balls_drawn)
      l_dr=[]
      for key in expected_balls:
       l_dr.append(drawn.count(key))
      if l_dr >= l_exp:
        succ+=1
      
  return succ/num_experiments

