from PyPDF2 import PdfFileReader

def listar_campos_preenchiveis(pdf_path):
    reader = PdfFileReader(pdf_path)
    fields = reader.getFields()

    print('{')
    for field_name in fields.keys():
        print(f"'{field_name}':,")
    print('}')

listar_campos_preenchiveis('fichas/gay.pdf')
