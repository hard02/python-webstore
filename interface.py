import sqlite3
import matplotlib.pyplot as plt
import numpy as np
# creating database
connection=sqlite3.connect('web_services.db')
print("database loaded successfully") # just to be sure that database is in operation
cursor=connection.cursor()
def inter_face():
 print(" \t welcome to main menu ","\n","enter the number for:")
 print("1=customer  \t 2=aministration")
 mainmenu=int(input("choose your option:")) # main menu option
 if(mainmenu== 1):
     print("welcome to customer","\n","what you wanna do today:") #customer menu
     print("1=buy \t 2=new customer \t 3=update information \t 4=cancel order \t  5=check info \t ")
     menu1=int(input("choose your option:"))
     if(menu1== 1):
         print("so what you gonna buy?")
         print("do you want to use order table?","\n","enter 1 to continue")
         ww=input("enter your choice:")
         if(ww=="1"):
             cursor.execute("select content_id, details from contents")
             op=cursor.fetchall()
             print(op)
         else:
             pass
         pnum=int(input("first, your mobile number:"))
         pid=int(input("enter product id to buy:"))
         pqty=int(input("enter quantity:"))
         pcom=input("any comments:")
         cursor.execute("insert into orders(mobile_no,content_id,quantity,comment) values(?,?,?,?)",(pnum,pid,pqty,pcom,))
         print("your order has been recorded","\n")
         print("\t do you want to see your orders? \t 1=yes \t 2=no")
         a=int(input("enter your choice:"))
         if(a==1):
             numm=pnum
             cursor.execute("select * from orders where mobile_no=?",(numm,))
             b=cursor.fetchall()
             print(b)
         elif(a==2):
             pass
         else:
             print("try again")
     elif(menu1==2):
         print("hello there")
         bnum=int(input("enter your number:"))
         bpwd=input("enter your password:")
         bname=input("enter your name:")
         bmail=input("enter your email:")
         bcust=input("what plan you bought:")
         cursor.execute("insert into customer values(?,?,?,?,?)",(bnum,bpwd,bname,bmail,bcust))
         print("your details have been entered successfully")
         print("you entered the following details:")
         cursor.execute("select * from customer where mobile_no=?",(bnum,))
         b=cursor.fetchall()
         print(b)
     elif(menu1==3):
         print("it's good to update the information")
         unum=int(input("enter your mobile no:"))
         upd=int(input("which info you want to update 1=password \t 2=name \t 3=email \t 4=customer plan   :"))
         if(upd==1):
             upwd=input("enter your new password:")
             cursor.execute("update customer set pwd=? where mobile_no=?",(upwd,unum))
             print("update successfully")
         elif(upd==2):
             uname=input("enter your new name:")
             cursor.execute("update customer set name=? where mobile_no=?",(uname,unum))
             print("update successfully")
         elif(upd==3):
             uemail=input("enter your new email:")
             cursor.execute("update customer set email=? where mobile_no=?",(uemail,unum))
             print("update successfully")
         elif(upd==4):
             ucust=input("enter your new cust_plan:")
             cursor.execute("update customer set cust_plan=? where mobile_no=?",(ucust,unum))
             print("update successfully")
         else:
             print("pls try again")
         print("this is your updated information")
         cursor.execute("select * from customer where mobile_no=?",(unum,))
         gbb=cursor.fetchall()
         print(gbb)
     elif(menu1==4):
         d_id=int(input("enter order id to delete:"))
         cursor.execute("DELETE FROM orders WHERE order_id = ? ", (d_id,))
         print("your order is removed")
     elif(menu1==5):
         unum=int(input("enter mobile number:"))
         print("customer details:")
         cursor.execute("select * from customer where mobile_no=?",(unum,))
         print(cursor.fetchall())
         print("orders:")
         cursor.execute("select * from orders where mobile_no=?",(unum,))
         print(cursor.fetchall())
     else:
         print("please try again")
 elif(mainmenu==2):
     qaz=input("enter admin password:")
     if(qaz=="0000"):
      print(" \t welcome admin ","\n","select option to work on","\n","1=orders \t 2=customers \t 3=providers")
      menu2=int(input("enter your choice:"))
      if(menu2==1):
          print("welcome to orders","\n","select option to work on orders","\n","1=edit \t 2=delete \t 3=add \t 4=show")
          smenu=int(input("enter your choice:"))
          if(smenu==1):
              print(" \t select the info you will work on","\n","1= content_id \t 2= quantity \t 3=comment")
              ssmenu=int(input("enter your option:"))
              if(ssmenu==1):
                  od=int(input("enter the order id to work on:"))
                  qcon=int(input("enter new content id:"))
                  cursor.execute("update orders set content_id=? where order_id=?",(qcon,od))
                  print("changed successfully")
                  print("the new information is :")
                  cursor.execute("select * from orders where order_id=?",(qcon,))
                  ppo=cursor.fetchall()
                  print(ppo)
              elif(ssmenu==2):
                  od=int(input("enter the order id to work on:"))
                  quan=int(input("enter new quantity:"))
                  cursor.execute("update orders set quantity=? where order_id=?",(quan,od))
                  print("changed successfully")
                  print("the new information is :")
                  cursor.execute("select * from orders where order_id=?",(od,))
                  ppo=cursor.fetchall()
                  print(ppo)
              elif(ssmenu==3):
                  com=input("enter new comment:")
                  cursor.execute("update orders set comment=? where order_id=?",(com,od))
                  print("changed successfully")
                  print("the new information is :")
                  cursor.execute("select * from orders where order_id=?",(od,))
                  ppo=cursor.fetchall()
                  print(ppo)
              else:
                  print("try again")
          elif(smenu==2):
              cursor.execute("DELETE FROM orders WHERE order_id = ? ", (od,))
              print("deleted successfully")
          elif(smenu==3):
              anum=int(input("enter mobile no:"))
              acon=int(input("enter content id:"))
              aquan=int(input("enter quantity:"))
              acomm=input("enter comment:")
              cursor.execute("insert into orders(mobile_no,content_id,quantity,comment) values(?,?,?,?)",(anum,acon,aquan,acomm))
              print("entered successfully")
              cursor.execute("select * from orders where mobile_no=?",(anum,))
              ppo=cursor.fetchall()
              print(ppo)
          elif(smenu==4):
              print("what do you want to see","\n","1= data \t 2=graphs")
              ggii=int(input("enter your choice:"))
              if(ggii==1):
                  cursor.execute("select * from orders")
                  a=cursor.fetchall()
                  print(a)
              elif(ggii==2):
                  print("what type of graph you want to see","\n","1=mobile_no vs orders \t 2=content vs orders")
                  aswd=int(input("enter your choice:"))
                  if(aswd==1):
                      cursor.execute("select mobile_no,count(*) from orders group by mobile_no")
                      data=cursor.fetchall()
                      pmob=[]
                      pord=[]
                      for row in data:
                          pmob.append(row[0])
                          pord.append(row[1])
                      print(pmob,pord)
                      pmob=list(map(str,pmob))
                      plt.bar(pmob,pord)
                      plt.xlabel("mobile_no")
                      plt.ylabel("orders")
                      plt.show()
                  elif(aswd==2):
                      cursor.execute("select content_id,count(*) from orders group by content_id")
                      data=cursor.fetchall()
                      pcont=[]
                      pord=[]
                      for row in data:
                          pcont.append(row[0])
                          pord.append(row[1])
                      print(pcont,pord)
                      pcont=list(map(str,pcont))
                      plt.bar(pcont,pord)
                      plt.xlabel("mobile_no")
                      plt.ylabel("orders")
                      plt.show()
          else:
              print("try again")
      elif(menu2==2):
          print("\t welcome to customer","\n","select option to work on","\n","1= edit \t 2 =delete \t 3=add \t 4=show")
          smenu=int(input("enter your choice:"))
          if(smenu==1):
              od=int(input("enter the mobile number to work on:"))
              print(" \t select the info you will work on","\n","1= pwd \t 2= name \t 3=email \t 4=cutomer plan")
              ssmenu=int(input("enter your option:"))
              if(ssmenu==1):
                  qcon=input("enter new pwd:")
                  cursor.execute("update customer set pwd=? where mobile_no=?",(qcon,od,))
                  print("changed successfully")
                  print("the new information is :")
                  cursor.execute("select * from customer where mobile_no=?",(od,))
                  ppo=cursor.fetchall()
                  print(ppo)
              elif(ssmenu==2):
                  quan=input("enter new name:")
                  cursor.execute("update customer set name=? where mobile_no=?",(quan,od,))
                  print("changed successfully")
                  print("the new information is :")
                  cursor.execute("select * from customer where mobile_no=?",(od,))
                  ppo=cursor.fetchall()
                  print(ppo)
              elif(ssmenu==3):
                  com=input("enter new email:")
                  cursor.execute("update customer set email=? where mobile_no=?",(com,od,))
                  print("changed successfully")
                  print("the new information is :")
                  cursor.execute("select * from customer where mobile_no=?",(od,))
                  ppo=cursor.fetchall()
                  print(ppo)
              elif(ssmenu==4):
                  cus=input("enter new customer plan:")
                  cursor.execute("update customer set cust_plan=? where mobile_no=?",(cus,od,))
                  print("changed successfully")
                  print("the new information is :")
                  cursor.execute("select * from customer where mobile_no=?",(od,))
                  ppo=cursor.fetchall()
                  print(ppo)
              else:
                  print("try again")
          elif(smenu==2):
              num=int(input("enter mobile_no:"))
              cursor.execute("DELETE from customer where mobile_no=?",(num,))
              print("deleted successfully")
          elif(smenu==3):
              onum=int(input("enter mobile_no:"))
              opwd=input("enter password:")
              oname=input("enter name:")
              oemail=input("enter email:")
              ocust=input("enter customer plan:")
              cursor.execute("insert into customer values(?,?,?,?,?)",(onum,opwd,oname,oemail,ocust))
              print("enter sucessfully")
              print("the information entered is :")
              cursor.execute("select * from customer where mobile_no=?",(onum,))
              ppo=cursor.fetchall()
              print(ppo)
          elif(smenu==4):
              print("what do you want to see","\n","1= data \t 2=graphs")
              ggii=int(input("enter your choice:"))
              if(ggii==1):
                  cursor.execute("select * from customer")
                  a=cursor.fetchall()
                  print(a)
              elif(ggii==2):
                  print("what type of graph you want to see","\n","1=customer plan ")
                  aswd=int(input("enter your choice:"))
                  if(aswd==1):
                      cursor.execute("select cust_plan,count(*) from customer group by cust_plan")
                      data=cursor.fetchall()
                      pcust=[]
                      pno=[]
                      for row in data:
                          pcust.append(row[0])
                          pno.append(row[1])
                      print(pcust,pno)
                      plt.pie(pno, labels=pcust)
                      plt.legend()
                      plt.title("customer plan")
                      plt.show()
          else:
              print("please try again")
      elif(menu2==3):
          print("\t welcome to providers","\n","select the table to work on","\n","1=providers \t 2=content")
          menu14=int(input("enter your option:"))
          if(menu14==1):
              print("\t welcome to providers","\n","select option to work on","\n","1=edit \t 2=delete \t 3=add \t 4=show")
              qmenu=int(input("enter your option:"))
              if(qmenu==1):
                  pid=int(input("enter the provider id to work on:"))
                  print(" \t select the info you will work on","\n","1= comp_name \t 2= address \t 3=country \t 4=pwd")
                  q1menu=int(input("enter your option:"))
                  if(q1menu==1):
                      qcomp=input("enter new company name:")
                      cursor.execute("update providers set comp_name=? where provider_id=?",(qcomp,pid))
                      print("changed successfully")
                      print("the new information is :")
                      cursor.execute("select * from providers where provider_id=?",(pid,))
                      ppo=cursor.fetchall()
                      print(ppo)
                  elif(q1menu==2):
                      qadd=input("enter new address:")
                      cursor.execute("update providers set address=? where provider_id=?",(qadd,pid))
                      print("changed successfully")
                      print("the new information is :")
                      cursor.execute("select * from providers where provider_id=?",(pid,))
                      ppo=cursor.fetchall()
                      print(ppo)
                  elif(q1menu==3):
                      country=input("enter new country:")
                      cursor.execute("update providers set country=? where provider_id=?",(country,pid))
                      print("changed successfully")
                      print("the new information is :")
                      cursor.execute("select * from providers where provider_id=?",(pid,))
                      ppo=cursor.fetchall()
                      print(ppo)
                  elif(q1menu==4):
                      qpwd=input("enter new password:")
                      cursor.execute("update providers set pwd=? where provider_id=?",(qpwd,pid))
                      print("changed successfully")
                      print("the new information is :")
                      cursor.execute("select * from providers where provider_id=?",(pid,))
                      ppo=cursor.fetchall()
                      print(ppo)
                  else:
                      print("try again")
              elif(qmenu==2):
                  pid=int((input("enter provider id:")))
                  cursor.execute("DELETE from providers where provider_id=?",(pid,))
                  print("deleted successfully")
              elif(qmenu==3):
                  nid=int(input("enter provider id:"))
                  ncomp=input("enter company name:")
                  nadd=input("enter company address:")
                  ncountry=input("enter country:")
                  pwd=input("enter password:")
                  cursor.execute("insert into providers values(?,?,?,?,?)",(nid,ncomp,nadd,ncountry,pwd))
                  print("entered successfully")
                  print("the entered information is :")
                  cursor.execute("select * from providers where provider_id=?",(nid,))
                  ppo=cursor.fetchall()
                  print(ppo)
              elif(qmenu==4):
                  print("what do you want to see","\n","1= data \t 2=graphs")
              ggii=int(input("enter your choice:"))
              if(ggii==1):
                  cursor.execute("select * from providers")
                  a=cursor.fetchall()
                  print(a)
              elif(ggii==2):
                  print("what type of graph you want to see","\n","1=company vs country")
                  aswd=int(input("enter your choice:"))
                  if(aswd==1):
                      cursor.execute("select country,count(*) from providers group by country")
                      data=cursor.fetchall()
                      pcountry=[]
                      pno=[]
                      for row in data:
                          pcountry.append(row[0])
                          pno.append(row[1])
                      print(pcountry,pno)
                      plt.plot(pcountry,pno)
                      plt.xlabel("country")
                      plt.ylabel("number")
                      plt.show()
              else:
                  print("try again")
          elif(menu14==2):
              print("\t welcome to contents","\n","select option to work on","\n","1=edit \t 2=delete \t 3=add \t 4=show")
              qmenu=int(input("enter your option:"))
              if(qmenu==1):
                  zid=int(input("enter the content id to work on:"))
                  print(" \t select the info you will work on","\n","1=title \t 2=details 3=rating \t 4=url \t 5=status \t 6=provider_id \t 7=ac_detail \t 8=price_per_unit")
                  q1menu=int(input("enter your option:"))
                  if(q1menu==1):
                      ztit=input("enter new title:")
                      cursor.execute("update contents set title=? where content_id=?",(ztit,zid))
                      print("changed successfully")
                      print("the new information is :")
                      cursor.execute("select * from contents where content_id=?",(zid,))
                      ppo=cursor.fetchall()
                      print(ppo)
                  elif(q1menu==2):
                      zde=input("enter new details:")
                      cursor.execute("update contents set details=? where content_id=?",(zde,zid))
                      print("changed successfully")
                      print("the new information is :")
                      cursor.execute("select * from contents where content_id=?",(zid,))
                      ppo=cursor.fetchall()
                      print(ppo)
                  elif(q1menu==3):
                      rating=float(input("enter new rating:"))
                      cursor.execute("update contents set rating=? where content_id=?",(rating,zid))
                      print("changed successfully")
                      print("the new information is :")
                      cursor.execute("select * from contents where content_id=?",(zid,))
                      ppo=cursor.fetchall()
                      print(ppo)
                  elif(q1menu==4):
                      url=input("enter new url:")
                      cursor.execute("update contents set url=? where content_id=?",(url,zid))
                      print("changed successfully")
                      print("the new information is :")
                      cursor.execute("select * from contents where content_id=?",(zid,))
                      ppo=cursor.fetchall()
                      print(ppo)
                  elif(q1menu==5):
                      zsta=input("enter new status:")
                      cursor.execute("update contents set status=? where content_id=?",(zsta,zid))
                      print("changed successfully")
                      print("the new information is :")
                      cursor.execute("select * from contents where content_id=?",(zid,))
                      ppo=cursor.fetchall()
                      print(ppo)
                  elif(q1menu==6):
                     zpd=int(input("enter new provider id:"))
                     cursor.execute("update contents set provider_id=? where content_id=?",(zpd,zid))
                     print("changed successfully")
                     print("the new information is :")
                     cursor.execute("select * from contents where content_id=?",(zid,))
                     ppo=cursor.fetchall()
                     print(ppo)
                  elif(q1menu==7):
                     zac=input("enter new ac_detail:")
                     cursor.execute("update contents set ac_detail=? where content_id=?",(zac,zid))
                     print("changed successfully")
                     print("the new information is :")
                     cursor.execute("select * from contents where content_id=?",(zid,))
                     ppo=cursor.fetchall()
                     print(ppo)
                  elif(q1menu==8):
                     zpp=float(input("enter new price per unit:"))
                     cursor.execute("update contents set price_per_unit=? where content_id=?",(zpp,zid))
                     print("changed successfully")
                     print("the new information is :")
                     cursor.execute("select * from contents where content_id=?",(zid,))
                     ppo=cursor.fetchall()
                     print(ppo)
                  else:
                      print("try again")
              elif(qmenu==2):
                      cid=int((input("enter content id:")))
                      cursor.execute("DELETE from contents where content_id=?",(cid,))
                      print("deleted successfully")
              elif(qmenu==3):
                  ncid=int(input("enter content id:"))
                  ntit=input("enter title:")
                  ndd=input("enter detail:")
                  nrt=input("enter rating:")
                  nurl=input("enter url:")
                  nt=input("enter status:")
                  nst=nt.upper()
                  npid=int(input("enter provider id:"))
                  ncd=input("enter account details:")
                  nppu=float(input("enter price per unit:"))
                  cursor.execute("insert into contents values(?,?,?,?,?,?,?,?,?)",(ncid,ntit,ndd,nrt,nurl,nst,npid,ncd,nppu))
                  print("entered successfully")
                  print("the entered information is :")
                  cursor.execute("select * from contents where content_id=?",(ncid,))
                  ppo=cursor.fetchall()
                  print(ppo)
              elif(qmenu==4):
                  print("what do you want to see","\n","1= data \t 2=graphs")
              ggii=int(input("enter your choice:"))
              if(ggii==1):
                  cursor.execute("select * from contents")
                  a=cursor.fetchall()
                  print(a)
              elif(ggii==2):
                  print("what type of graph you want to see","\n","1=content vs rating \t 2=status vs content")
                  aswd=int(input("enter your choice:"))
                  if(aswd==1):
                      cursor.execute("select content_id,rating from contents ")
                      data=cursor.fetchall()
                      pcontent=[]
                      prating=[]
                      for row in data:
                          pcontent.append(row[0])
                          prating.append(row[1])
                      print(pcontent,prating)
                      pcontent=list(map(str,pcontent))
                      plt.plot(pcontent,prating)
                      plt.xlabel("content id")
                      plt.ylabel("rating")
                      plt.show()
                  elif(aswd==2):
                      cursor.execute("select status,count(*) from contents group by status")
                      data=cursor.fetchall()
                      pstatus=[]
                      pno=[]
                      for row in data:
                          pstatus.append(row[0])
                          pno.append(row[1])
                      print(pstatus,pno)
                      plt.pie(pno,labels=pstatus)
                      plt.title("active vs inactive")
                      plt.legend()
                      plt.show()
              else:
                  print("try again")
     else:
         print("try again")
 else:
        print("try again")
 print(" do you want to continue? \t press 1 to continue")
 pp=input("enter your choice:")
 connection.commit()
 if(pp=="1"):
     inter_face()
 else:
     pass
inter_face()
