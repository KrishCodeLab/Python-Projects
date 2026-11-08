import os

# Phase 1 : Understand directory handeling

# Where are files located ?
location = os.getcwd()
# Returns the current working directory
print(location)


system_path=r"C:\Users\Krushana"
userdefined=input("Enter Directory : ")
joined_path=os.path.join(system_path,userdefined)
print(joined_path)
# print(os.listdir(joined_path))

# What files are present inside the folder ?
list_of_file=os.listdir(joined_path)
print(list_of_file)

# Which entries are files and folders ?
for file in list_of_file:
  full_path=os.path.join(joined_path,file)
  print(full_path)
  
  if os.path.isfile(full_path):
    print("It is File "+ file)
  elif os.path.isdir(full_path):
    print("It is Folder "+ file)