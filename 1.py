phone_directory={}
i=0
print("\n PHONE DIRECTORY\n1. Add a record\n2. Search a record\n3. Update a record\n4. Sort the records alphabetically\n5. Delete a record\n6. Quit")
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
   c=phone_directory[a]
  else:
   print("record not found")
