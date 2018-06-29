import PyPDF2
pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter=PyPDF2.PdfFileWriter()
for PageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(PageNum)
    pdfWriter.addPage(pageObj)
for PageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(PageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
