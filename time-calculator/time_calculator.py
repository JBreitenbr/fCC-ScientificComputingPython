def add_time(start, duration,start_day=""):
   import math

   dig=start.split()[0]
   tgl=start.split()[1]

   start_h=int(dig.split(":")[0])
   start_m=int(dig.split(":")[1])
   start_mins=start_h*60+start_m
  
   dur_h=int(duration.split(":")[0])
   dur_m=int(duration.split(":")[1])
   dur_mins=dur_h*60+dur_m

   res_mins=start_mins+dur_mins
   if tgl=="PM":
      res_mins=start_mins+dur_mins+720
   hlp=res_mins/(60*24) 
   res_days=math.floor(hlp)
   res_m=(res_mins-60*24*res_days)%60
   res_h=int((res_mins-60*24*res_days-   res_m)/60)
   n_tgl=tgl
   if res_h>12:
      res_h=res_h-12
      n_tgl="PM"
   if res_h==12:
      n_tgl="PM"
   if res_days>0:
      if tgl=="AM":
         n_tgl="PM"
      if tgl=="PM":
         n_tgl="AM"
   if res_h==0 and n_tgl=="AM":
      res_h=12
   if duration=="24:00":
      n_tgl=tgl
   
   if res_m<10:
      res_m_str="0"+str(res_m)
   else:
      res_m_str=str(res_m)
   dres_str=str(res_h)+":"+res_m_str
   res_str=dres_str+" "+n_tgl

   wdays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
   if start_day != "":
      start_day_c=start_day.capitalize() 
      ind_st=wdays.index(start_day_c)
      day_en=wdays[(ind_st+res_days)%7]

   if start_day!="" and res_days==0:
      res_str_d=start_day_c
      res_all=res_str+", "+res_str_d
   if start_day!="" and res_days==1:
      res_str_d=day_en
      res_all=res_str+", "+res_str_d + " (next day)"
   if start_day=="" and res_days==0:
      res_all=res_str
   if start_day=="" and res_days==1:
      res_all=res_str + " (next day)"

   days_lt=" ("+str(res_days)+" days later)"
   if start_day=="" and res_days>1:
      res_all=res_str+days_lt
   if start_day!="" and res_days>1:
      res_all=res_str+", "+day_en+days_lt


   return res_all
