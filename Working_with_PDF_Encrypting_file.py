import PyPDF2
pdfFile = open('meetingminutes.pdf', 'rb')
pdfRead = PyPDF2.PdfFileReader(pdfFile)
pdfWrite = PyPDF2.PdfFileWriter()
for pageNum in range(pdfRead.numPages):
    pdfObj = pdfRead.getPage(pageNum)
    pdfWrite.addPage(pdfObj)

pdfWrite.encrypt('swordfish')
resultpdf = open('enc.pdf', 'wb')
pdfWrite.write(resultpdf)
resultpdf.close()
