'''Project : Auto Files Organization
       Name : Bibek Kumar Sah
       Enrollment Number : 20SOECE11097
       Section : 3CEC '''

import os

import shutil

# reading the folder's path
path = r"D:\Auto Files Organization"

os.chdir(path)
os.getcwd()

# check the extension name
os.listdir()

# get the extension name
list_extension = []
for fl in os.listdir():
    extension = fl.split(".")[-1]
    list_extension.append(extension)

# print(list_extension)

list_extension = set(list_extension)
print(list_extension)
print(len(list_extension))

# create a folder on desktop

folderpath = os.environ["UserProfile"] + "\\" + "Desktop" + "\\" + "Auto_files_organization"
print(folderpath)
os.mkdir(folderpath)


# transfer the files with specific folder

for ex in list_extension:
    print(ex, end=",")
    os.mkdir(folderpath + "\\" + ex)
    for fl in os.listdir():
        if ex in fl:
            shutil.copy(fl, folderpath + "\\" + ex)
