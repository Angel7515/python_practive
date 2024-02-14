import PyPDF2
from openai import OpenAI
import openai


pdf = open("Ejercicio5 OpenAI - pdf/67115.pdf","rb")
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
print("soy un contenido : ",contenido)
prompt = "Crea una cita en formato apa7 del siguiente texto: \n"
request = prompt + contenido
# Reemplaza 'TU_CLAVE_API' con tu clave de API real de OpenAI
clave_api = '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'
client = openai.OpenAI(api_key=clave_api)


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Eres un asistente académico con conocimientos en el formato APA 7. Hábil para generar citas precisas y conformes a las normas de la American Psychological Association."},
    {"role": "user", "content": request}
  ]
)

print("**************************\n\n")
print(completion.choices[0].message)

print("**************************\n\n")
print(completion['choices'][0]['message']['content'])

print("**************************\n\n")
