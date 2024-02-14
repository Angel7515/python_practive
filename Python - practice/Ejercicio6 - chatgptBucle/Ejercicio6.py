from dotenv import load_dotenv
from openai import OpenAI
import os

#cargar variables de entorno (.env)
load_dotenv()

# Configuracion para obtener la API KEY de OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
                )

#Solicitud de usuario
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system", "content":"you are an assistant who knows all possible and creative topics."},
        {"role":"user", "content":"Who is CIMMYT?"}
    ]
)

print(completion.choices[0].message.content)