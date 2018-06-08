import zipfile,os
# change current directory
os.chdir('/home/mainul/Desktop/copy_files')
# Get the current working directory
print(os.getcwd())
# List of the directory
print(os.listdir())
examplezip=zipfile.ZipFile('Automate_the_Boring_Stuff_onlinematerials.zip')
examplezip.extractall()
examplezip.close()

