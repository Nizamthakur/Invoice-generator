from docxtpl import DocxTemplate

doc = DocxTemplate("invoice.docx")

doc.render({})
doc.save("newInvoice.docx")

