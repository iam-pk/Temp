import os

print("cafe coffe day")
print("A lot can happen over coffe")
a=input("enter your choice")
if a=="adminstration":
   with open("adminstration.txt","w") as b:
#please enter your designation
#enter the id-password
    name=input("enter your name")
    ID=input("enter your id")
    Password=input("enter the password")
#password must contains 6 numeric with 2
#special characters or alphabates
    if Password=="1234ab6":
       print("correct password")
       b.write(name)
       b.write("\n")
       b.write(ID)
       b.write("\n")
       b.write(Password)
       b.write("\n")
       b.write("total assests:6601.88crore,net income:583.92crore,")
    else:
        b.write("wrong password")
elif a=="customer":
   p=input("enter the name")
   c=int(input("enter the table number"))
   menu_path = r"D:\code\python\menu.jpg"
   os.startfile(menu_path) 
   f=input("enter the order")
   h=open("order1.txt","w")
   s=open("order2.txt","w")
   h.write(p)
   h.write("\n")
   h.write(str(c))
   h.write("\n")
   h.write(f)
   h.write("\n")
   s.write(f)
   h.close()
   s.close()


   
if a=="staff":
   s=input("choose kitchen staff or working staff:")
   if s=="kitchen staff":
      print("todays order!")
      m=open("order2.txt","r")
      n=m.read()
      print(n)
   if s=="working staff":  
      mn=open("order1.txt","r")
      nm=mn.read()
      print(nm)