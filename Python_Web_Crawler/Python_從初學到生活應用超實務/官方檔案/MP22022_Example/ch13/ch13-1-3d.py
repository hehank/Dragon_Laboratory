import docx
from docx.shared import Cm

doc = docx.Document("word文件3.docx")
doc.add_picture("koala_small.png", width=Cm(3))
doc.save("word文件4.docx")
 


