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

