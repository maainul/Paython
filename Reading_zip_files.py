import zipfile,os
# previous directory
print(os.getcwd())
# Change directory
print(os.chdir('/home/mainul/Desktop/copy_files'))
print(os.getcwd())
exampleZip=zipfile.ZipFile('Automate_the_Boring_Stuff_onlinematerials.zip')
print(exampleZip.namelist())
sampleinfo=exampleZip.getinfo('automate_online-materials/alarm.wav')
print(sampleinfo)
print(sampleinfo.file_size)
print(sampleinfo.compress_size)
print('Compressed file is %sx smaller' %(round(sampleinfo.file_size/sampleinfo.compress_size,4)))
exampleZip.close()
