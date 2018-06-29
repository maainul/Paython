from docx import Document

document = Document('demo.docx')
for para in document.paragraphs:
    print(para.text)
