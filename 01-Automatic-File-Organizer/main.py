import os

# Phase 1 : Understand directory handeling

# Where are files located ?
location = os.getcwd()
# Returns the current working directory
print(location)


base_path=r"C:\Users\Krushana"
directory=input("Enter Directory : ")
functional_path=os.path.join(base_path,directory)
print(functional_path)
# print(os.listdir(joined_path))

# Check Path Exits in system or not
if os.path.exists(functional_path) and os.path.isdir(functional_path):
  print("Directory Exits")
  # What files are present inside the folder ?
  list_of_file=os.listdir(functional_path)
  print(list_of_file)

# Which entries are files and folders ?
  for file in list_of_file:
    full_path=os.path.join(functional_path,file)
    print(full_path)
  
    if os.path.isfile(full_path):
      print("It is File "+ file)
    elif os.path.isdir(full_path):
      print("It is Folder "+ file)
else:
  print("Invalid Directory Path !")

