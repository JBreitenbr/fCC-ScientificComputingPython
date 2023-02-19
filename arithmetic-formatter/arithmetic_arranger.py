def arithmetic_arranger(problems,val=False):
    if len(problems)>5:
      return "Error: Too many problems."
    n1=[]
    op=[]
    n2=[]

    for i in range(len(problems)):
       n1.append((problems[i].split(" "))[0])
       op.append((problems[i].split(" "))[1])
       n2.append((problems[i].split(" "))[2])
    for i in range(len(problems)):
       if n1[i].isnumeric()==False or n2[i].isnumeric()==False:
         return "Error: Numbers must only contain digits."
       if len(n1[i])>4 or len(n2[i])>4:
         return "Error: Numbers cannot be more than four digits."
       if op[i] not in ['+','-']:
         return "Error: Operator must be '+' or '-'."
    wd1=[]
    wd2=[]
    for i in range(len(problems)):
      wd1.append(max(len(n1[i]),len(n2[i]))+2-len(n1[i]))

    for i in range(len(problems)):
       wd2.append(max(len(n1[i]),len(n2[i]))+1-len(n2[i]))
    ln1=""
    for i in range(len(problems)):
       ln1+=wd1[i]*" "+n1[i]+4*" "
    ln2=""
    for i in range(len(problems)):
       ln2+=op[i]+wd2[i]*" "+n2[i]+4*" "
    ln3=""
    for i in range(len(problems)):
       ln3+=(wd1[i]+len(n1[i]))*"-"+4*" "
    
    res=[]
    for i in range(len(problems)):
       if op[i]=="+":            
          res.append(str(int(n1[i])+int(n2[i])))
       if op[i]=="-":
          res.append(str(int(n1[i])-int(n2[i])))
    ln4=""
    for i in range(len(problems)):
       ln4+=(wd1[i]+len(n1[i])-len(res[i]))*" "+res[i]+4*" "
    stri=ln1[:-4]+"\n"+ln2[:-4]+"\n"+ln3[:-4]
    if val==False:
       arranged_problems=stri
    else: 
       arranged_problems=stri+"\n"+ln4[:-4]

       
    return arranged_problems

    
