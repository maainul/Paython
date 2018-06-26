import  openpyxl,random,os
wb=openpyxl.Workbook()
os.chdir('/home/mainul/Desktop/copy_files')
sheet=wb.create_sheet('My sheet')
for i in range(1,11):
    sheet['A' + str(i)].value=random.randint(1,10)
wb.save('example2.xlsx')


