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
          directory="txt"
          directory_creation_path=os.path.join(functional_path,directory)

          if os.path.exists(directory_creation_path) and os.path.isdir(directory_creation_path):
             print("Folder Already Exist !!! ")
             
          else:
            # Creating folder in user specified path
             os.mkdir(directory_creation_path)
             print("Folder Created Successfully !!! ")
             
          print(file_name," is text file")
      elif file_extension.lower()==".py":
          directory="python"
          directory_creation_path=os.path.join(functional_path,directory)
          
          if os.path.exists(directory_creation_path) and os.path.isdir(directory_creation_path):
             print("Folder Already Exist !!! ")
                       
          else:
          # Creating folder in user specified path
              os.mkdir(directory_creation_path)
              print("Folder Created Successfully !!! ")

          print(file_name," is python file")
      elif file_extension.lower()==".java":
          directory="java"
          directory_creation_path=os.path.join(functional_path,directory)
                    
          if os.path.exists(directory_creation_path) and os.path.isdir(directory_creation_path):
              print("Folder Already Exist !!! ")
                                 
          else:
          # Creating folder in user specified path
              os.mkdir(directory_creation_path)
              print("Folder Created Successfully !!! ")

          print(file_name," is java file")
      elif file_extension.lower()==".jpg":
          directory="jpg"
          directory_creation_path=os.path.join(functional_path,directory)
                    
          if os.path.exists(directory_creation_path) and os.path.isdir(directory_creation_path):
              print("Folder Already Exist !!! ")
                                 
          else:
          # Creating folder in user specified path
              os.mkdir(directory_creation_path)
              print("Folder Created Successfully !!! ")

          print(file_name," is jpg photo file")
      elif file_extension=="":
          directory="NoExtensionFiles"
          directory_creation_path=os.path.join(functional_path,directory)
                    
          if os.path.exists(directory_creation_path) and os.path.isdir(directory_creation_path):
              print("Folder Already Exist !!! ")
                                 
          else:
          # Creating folder in user specified path
              os.mkdir(directory_creation_path)
              print("Folder Created Successfully !!! ")

          print(file_name," has no extension")
      
  
    
    elif os.path.isdir(full_path):
      folders_list.append(file)
    
  print(files_list)
  print(folders_list)
  
else:
  print("Invalid Directory Path !")


