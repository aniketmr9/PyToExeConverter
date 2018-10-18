import os
python_file_location = input("Enter python file path:")
exe_filename = input("Enter name of executable file:")
version = input("Enter version number:")
description = input("Enter a description:")
python_filename = python_file_location[python_file_location.rfind("\\")+1:]
python_file_path = python_file_location[:python_file_location.rfind("\\")+1]
if os.path.exists(python_file_location):
    if python_filename[-3:] == ".py":
        f = open(python_file_path+"setup.py", "w")
        f.write("from cx_Freeze import setup, Executable"
                "\nsetup(name = '"+exe_filename+"',"
                "\n\tversion = '"+version+"',"
                "\n\tdescription = '"+description+"',"
                "\n\texecutables = [Executable('"+python_filename+"')])")
        f.close()
        os.chdir(python_file_path)
        os.system('python setup.py build')
    else:
        print("Please select a python(.py) file")
else:
    print("Invalid path")
