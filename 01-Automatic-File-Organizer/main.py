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
  list_of_files=os.listdir(functional_path)
  print(list_of_files)

  files_list=[]
  folders_list=[]
# Which entries are files and folders ?
  for file in list_of_files:
    full_path=os.path.join(functional_path,file)
    # print(full_path)
  
    if os.path.isfile(full_path):
      file_info=os.path.splitext(file)
      file_name=file_info[0]
      file_extension=file_info[1]
      files_list.append(file)
      if file_extension.lower()==".txt":
          print(file_name," is text file")
      elif file_extension.lower()==".py":
          print(file_name," is python file")
      elif file_extension.lower()==".java":
          print(file_name," is java file")
      elif file_extension.lower()==".jpg":
          print(file_name," is jpg photo file")
  
    
    elif os.path.isdir(full_path):
      folders_list.append(file)
    
  print(files_list)
  print(folders_list)
  
else:
  print("Invalid Directory Path !")


