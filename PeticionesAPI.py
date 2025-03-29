#Cómo hacer peticiones a API, con y sin dependencias

#---------- SIN DEPENDENCIAS -----------
import urllib.error
import urllib.request
import json

api_posts = "https://jsonplaceholder.typicode.com/posts/"

#Abrir URL y obtener la respuesta
try:

    response = urllib.request.urlopen(api_posts)

    data = response.read()

    json_data = json.loads(data.decode("utf-8"))

    print(json_data)

    response.close()

except urllib.error.URLError as e:
    print("Error en la solicitud {e}")


#--------- CON DEPENDENCIAS -------------
import requests

response = requests.get(api_posts)

print(response.json())

json = response.json()

print(json[2])

#pip install requests
#cd BBDD (para ejecutarlo aquí)
#.\venv\Scripts\Activate (para ejecutar el entorno virtual donde se instaló requests)
#.\PeticionesAPI.py (para ejecutar el programa)


#Un POST

try:
    input = {
        "title" : "midu",
        "body" : "dev",
        "userId" : 5
    }

    response = requests.post(api_posts, json=input)

    print(response.json())
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print("Error en la solicitud")


#Un PUT
try:
    input = {
        "title" : "foo",
        "body" : "bar",
        "userId" : 1
    }
    api_posts = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.put(api_posts, json=input)

    print(response.json())
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print("Error en la solicitud")


#LA DIFERENCIA ENTRE EL PUT Y PATCH ES QUE EL PUT DEBES PASARLE TODO EL OBJETO, Y EL PATCH SOLO LOS VALORES A TRATAR


#Usar la API de GPT-4o de OpenAI
#import json

OPENAI_KEY = "sk-XXXXXXXX"

def call_openai_gpt(api_key, promtp):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type" : "application/json",
        "Authorization" : f"Bearer {api_key}"
    }
    data = {
        "model" : "gpt-4o-mini",
        "messages" : [{"role" : "user", "content" : promtp}]
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()

api_response = call_openai_gpt(OPENAI_KEY, "Escribe un breve poema sobre la programación")

print(api_response["choices"][0]["message"]["content"])