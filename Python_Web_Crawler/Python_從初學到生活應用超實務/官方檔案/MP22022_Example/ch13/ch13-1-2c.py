import docx

doc = docx.Document("Python開發環境.docx")
for style in doc.styles:
    print(style.name, end=" ")

