import docx

doc = docx.Document("word文件2.docx")
records = (
    ('王小明', '02-12345678', 78),
    ('陳小安', '02-23456789', 67),
    ('李四', '02-34567890', 82) )
table = doc.add_table(rows=1, cols=3)
row = table.rows[0]
row.cells[0].text = '姓名' 
row.cells[1].text = '電話'
row.cells[2].text = '成績'
for name, tel, score in records:
    row_cells = table.add_row().cells
    row_cells[0].text = name
    row_cells[1].text = tel
    row_cells[2].text = str(score)
doc.save("word文件3.docx")
 


