import os
import shutil
print(os.getcwd())
source_path = '/home/user/Automate_boring_stuff'
destination_path = '/home/user/Desktop'

    enter code here

for files in os.listdir(source_path):
    if files.endswith('.docx'):
        print(files)
        shutil.copy(files, destination_path)
