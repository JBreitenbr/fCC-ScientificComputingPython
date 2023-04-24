import math

class Category:

  def __init__(self,category):
    self.category=category
    self.ledger=[]

  def __str__(self):
    left=math.floor((30-len(self.category))/2)
    right=30-len(self.category)-left
    stri=left*'*'+self.category+right*'*'+"\n"
    for item in self.ledger:
      pt1=item["description"][0:23]+(23-len(item["description"][0:23]))*" "
      pt2=(7-len("{:.2f}".format(item["amount"])))*" "+"{:.2f}".format(item["amount"])
      hlp=pt1+pt2
      stri=stri+hlp+"\n"
    total="Total: "+"{:.2f}".format(self.get_balance())
    stri=stri+total
    return stri

  def deposit(self,amount,description=""):
    dic={}
    dic['amount']=amount
    dic['description']=description
    self.ledger.append(dic)
    

  def withdraw(self,amount,description=""):
    dic={}
    if self.check_funds(amount):
      dic['amount']=-amount
      dic['description']=description
      self.ledger.append(dic)
      return True
    return False

  def transfer(self,amount,other_cat):
    if self.check_funds(amount):
      self.withdraw(amount,"Transfer to "+other_cat.category)
      other_cat.deposit(amount,"Transfer from "+self.category)
      return True
    return False

  def get_balance(self):
    balance=0
    for item in self.ledger:
      balance = balance+item['amount']
    return balance

  def check_funds(self,amount):
    if amount > self.get_balance():
      return False
    return True

def create_spend_chart(categories):
   p=[]
   for cat in categories:
     c_s=0
     for item in cat.ledger:
       if item["amount"]<0:
         c_s+=item["amount"]*(-1)
     p.append(c_s)
   t_s=sum(p)
   for i in range(len(p)):
     p[i]=10*math.floor(10*p[i]/t_s)

   st="Percentage spent by category"+"\n"
   for i in range(100,-1,-10):
     st+=(3-len(str(i)))*" "+str(i)+"|"
     for k in range(len(p)):
       if p[k] >=i:
         st+=" o "
       else:
         st+=3*" "
     st+=" "+"\n"
   st+=4*" "
   for i in range(len(p)):
     st+=3*"-"
   st+="-"+"\n"+" "

   maxi=0
   for cat in categories:
     if len(cat.category)>maxi:
       maxi=len(cat.category)
   cats=[]
   for cat in categories:
     cats.append(cat.category+(maxi-len(cat.category))*" ")
   tl=""
   for i in range(maxi):
     tl+=4*" "
     for j in range(len(cats)):
       tl+=cats[j][i]+2*" "
     if i < maxi-1:
       tl+="\n"+" "

   st+=tl
   return st

