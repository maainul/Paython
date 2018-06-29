import os
for files in os.listdir('.'):
    if files.endswith('.docx'):
        print(files)
