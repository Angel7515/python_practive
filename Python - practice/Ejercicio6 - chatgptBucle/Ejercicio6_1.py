from dotenv import load_dotenv
from openai import OpenAI
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración para obtener la API KEY de OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Iniciar el bucle de conversación
while True:
    # Leer la pregunta del usuario desde la consola
    prompt = input("You: ")

    # Salir del bucle si el usuario ingresa "adios" o "exit"
    if prompt.lower() in ["adios", "exit"]:
        print("Hasta luego. ¡Adiós!")
        break

    # Enviar la pregunta a la API
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un historiador experto solo en la Historia de Mexico y responderas amablemente indicando que solo puedes hablar de la historia de Mexico"},
            {"role": "user", "content": prompt}
        ]
    )

    # Mostrar la respuesta de la API
    print("Assistant:", completion.choices[0].message.content)