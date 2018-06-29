import PyPDF2
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
page = pdfReader.numPages
print(page)
pageObj = pdfReader.getPage(0)
pageObj.extractText()
