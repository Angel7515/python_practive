import PyPDF2
from dotenv import load_dotenv
load_dotenv()
import os
from bardapi import Bard

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

page = reader._get_page(0)

contenido = page.extract_text()

api_key = os.environ.get("_BARD_API_KEY")
bard = Bard(token=api_key)
prompt = "Crea una cita en formato apa7 del siguiente texto "
request = prompt + contenido
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\nSolicitud enviada: " + request +" \n -*-*-*-*-*-*-*-*-*-*-*-*-")
bard_response = bard.get_answer(request)["content"]
print(bard_response)