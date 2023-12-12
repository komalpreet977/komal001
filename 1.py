phone_directory={}
i=0
print("\n WELCOME TO THE GRANN'S PHONE DIRECTORY\n1. Add a record\n2. Search a record\n3. Update a record\n4. Sort the records alphabetically\n5. Delete a record\n6. Quit")
while i<=6:
 i=int(input("enter multiple choices: "))
 if i==1:
  a=input("enter your name: ")
  b=input("enter your phone number: ")
  phone_directory[a]=b
  print("record is added successfully")

  
 elif i==2:
  a=input("enter search a record: ")
  if a in phone_directory:
   print(phone_directory[a])
  else:
   print("record not found")

 elif i==3:
  a=input("enter name to serch:")
  b=input("enter new 10 digit phone number: ")
  if a in phone_directory:
   phone_directory[a]=b
   print("record updated")
  else:
   print("record not found")

 elif i==4:
  mydic={"komal":8699978349,"seerat":6472239434}
  mykeys=list(mydic.keys())
  mykeys.sort()
  print(mykeys)
  sorted_dic={i:mydic[i] for i in mykeys}
  print(sorted_dic)

 elif i==5:
  a=input("enter name to delete")
  if a in phone_directory:
    phone_directory.pop(a)
    print("record deleted")

 elif i==6:
  print("exit from whole program")
  print("\n WELCOME TO THE GRANN'S PHONE DIRECTORY\n1. Add a record\n2. Search a record\n3. Update a record\n4. Sort the records alphabetically\n5. Delete a record\n6. Quit")







