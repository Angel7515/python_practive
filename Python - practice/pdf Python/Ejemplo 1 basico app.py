#Dentro de este ejemplo solo se lee la primer pagina y se extrae todo su contenido para despues guardarlo en un nuevo archivo.
import PyPDF2

pdf = open("pdf Python/IA McCulloch and Pitts.pdf", "rb")  # Para sistemas basados en Unix (Linux)

reader = PyPDF2.PdfReader(pdf)
page = reader._get_page(0)

content = page.extract_text()

print(content)

# guardar el contenido de la pagina en un nuevo archivo txt 

with open("pdf Python/info_pdf.txt", "w") as txt: 
    txt.write(content)
