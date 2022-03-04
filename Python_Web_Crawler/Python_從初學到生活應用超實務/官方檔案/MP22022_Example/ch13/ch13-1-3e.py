import docx

doc = docx.Document("word文件4.docx")
doc.add_page_break()
doc.save("word文件5.docx")
 


