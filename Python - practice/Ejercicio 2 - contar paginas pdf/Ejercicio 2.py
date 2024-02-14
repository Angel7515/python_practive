import PyPDF2

pdf = open("Ejercicio 2 - contar paginas pdf/Ethics_of_Artificial_Intelligence-2.pdf","rb")

reader = PyPDF2.PdfReader(pdf)

n_pages = len(reader.pages)

for nu_page in range(len(reader.pages)):
    print("Page ", nu_page)
    info_page = reader._get_page(nu_page)
    extract_info = info_page.extract_text()
    print(extract_info)
    print('***************************************************')


print('paginas',n_pages)