# Primer problema con API de Rick and Morty
#Importamos requests
import requests

# Definimos el URL base de la API de Rick and Morty que sacamos de internet 
base_url = "https://rickandmortyapi.com/api/"

# Establecemos el request tipo GET con el endpoints character, para poder contar los personajes
response = requests.get(base_url + "character")

# ChatGPT nos recomienda sacar cosas de la API solo despues de mirar si esta si esta online, por eso hacemos el check del status
if response.status_code == 200:
    # Ya adentro guardamos la respuesta en data
    data = response.json()
    # El total de personajes se encuentra en el apartadod de info en la llave count
    total_characters = data["info"]["count"]
    # Imprimimos el número de caracteres
    print(f"El número total de personajes es: {total_characters}")
else:
    print("No se puede acceder a la API")

# Respuesta
# El número total de personajes es: 826