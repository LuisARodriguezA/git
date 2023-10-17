import requests
# 2023-10-06
# Integrantes:
    # - Luis Alejandro Rodríguez Arenas
    # - Juan David Garcia Barreto
    # - Manuel Arturo Fajardo Contreras
    # - Nicolás Antonio Sánchez Bautista
    # - Juan Ángel Leguizamón González
    # - Andrea Alejandra Suarez Cuervo 
# Notas:
    # Es importante aclarar que el punto 4 solo lo logramos hacer con la API de pokémon, y habían casos como el key de 
    # especies que no estaban en ningúna de las dos API  por lo que se usaron otras keys como "tipo" en el caso de Pokémon o 
    # ningúna adicional como en el caso de la de Rick and Morty en el segundo problema.
#------------------------------------------------------------------------------------------------------------------------
# Primer ejercicio
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
#------------------------------------------------------------------------------------------------------------------------
# Segundo ejercicio
import requests
base_url = "https://rickandmortyapi.com/api/"
response = requests.get(base_url + "character")
if response.status_code == 200:
    data = response.json()
    
    # Ahora iteramos para cada personaje y guardamos en una variable el nombre y estatus
    for character in data["results"]:
        character_name = character["name"]
        character_status = character["status"]
        # OJO LA ESPECIE NO LA LOGRAMOS SACAR PORQUE NO HAY UN ITEM QUE SE LLAME ASÍ EN LA API DE RICK AND MORTY   
        # Se imprime con el formato deseado
        print(f"{character_name}-{character_status}")
else:
    print("No se puede acceder a la API")

# Respuesta
# Rick Sanchez-Alive
# Morty Smith-Alive
# Summer Smith-Alive
# Beth Smith-Alive
# Jerry Smith-Alive
# Abadango Cluster Princess-Alive
# Abradolf Lincler-unknown
# Adjudicator Rick-Dead
# Agency Director-Dead
# Alan Rails-Dead
# Albert Einstein-Dead
# Alexander-Dead
# Alien Googah-unknown
# Alien Morty-unknown
# Alien Rick-unknown
# Amish Cyborg-Dead
# Annie-Alive
# Antenna Morty-Alive
# Antenna Rick-unknown
# Ants in my Eyes Johnson-unknown
#------------------------------------------------------------------------------------------------------------------------
# Tercer ejercicio
import requests
base_url = "https://rickandmortyapi.com/api/"
response = requests.get(base_url + "character")
if response.status_code == 200:
    data = response.json()

    # Creamos las listas para cada categoría que vamos a agrupar
    male_characters = []
    female_characters = []
    none_gender_characters = []

    # Ahora iteramos para cada personaje para categorizarlos por género
    for character in data["results"]:
        character_gender = character["gender"]
        
        if character_gender == "Male":
            male_characters.append(character)
        elif character_gender == "Female":
            female_characters.append(character)
        else:
            none_gender_characters.append(character)

    # Imprimimos cuantos hay de cada genero, como somos inclusivos incluimos el genero None.
    print(f"Male: {len(male_characters)} characters")
    print(f"Female: {len(female_characters)} characters")
    print(f"None: {len(none_gender_characters)} characters")
else:
    print("No se puede acceder a la API")

# Respuestas
# Male: 15 characters
# Female: 4 characters
# None: 1 characters
#------------------------------------------------------------------------------------------------------------------------
# Cuarto ejercicio
# Para el punto cuatro consideramos que era  pertinente hacerlo con la API de Pokémon, y como la categoría de especie estaba populada
# con el mismo nombre del pokemon decidimos hacerlo con el tipo elementar de cada pokemón.

import requests

base_url = "https://pokeapi.co/api/v2/"

pokemon_response = requests.get(base_url + "pokemon")

if pokemon_response.status_code == 200:
    pokemon_data = pokemon_response.json()["results"]

    # Creamos diccionario para ir contando
    type_counts = {}

    # Iteramos por la lista de pokémones y vamos contando cuantos hay de cada tipo
    for pokemon_info in pokemon_data:
        # Esto siguiente extrae el tipo de cada pokemon
        pokemon_url = pokemon_info["url"]
        pokemon_type_response = requests.get(pokemon_url)
        if pokemon_type_response.status_code == 200:
            pokemon_type_data = pokemon_type_response.json()
            for type_info in pokemon_type_data["types"]:
                type_name = type_info["type"]["name"]
                type_counts[type_name] = type_counts.get(type_name, 0) + 1

    # Hacemos sort usando la función lambda para sortear de acuerdo al primer indice de X
    sorted_types = sorted(type_counts.items(), key=lambda x: x[0])

    # Imprimimos la cuenta final
    for type_name, count in sorted_types:
        print(f"{type_name.capitalize()}: {count} Pokémon")
else:
    print("No se puede acceder a la API")

# Resultado
# Bug: 6 Pokémon
# Fire: 3 Pokémon
# Flying: 5 Pokémon
# Grass: 3 Pokémon
# Normal: 5 Pokémon
# Poison: 6 Pokémon
# Water: 3 Pokémon
#------------------------------------------------------------------------------------------------------------------------
# Quinto ejercicio
import requests
base_url = "https://rickandmortyapi.com/api/"

# Contamos las apariciones de los personajes en cada episodio
def count_character_appearances(episode_data):
    character_counts = {}
    for episode in episode_data:
        for character_url in episode["characters"]:
# Identificamos el nombre del personaje partiendo el url y tomando el indice -1, para tomar el nombre y no el endpoint
            character_name = character_url.split("/")[-1]
# Usamos el nombre del personaje (Digo nombre pero es el ID en realidad, para conseguir en cuantos episodios ha salido)
            character_counts[character_name] = character_counts.get(character_name, 0) + 1
    return character_counts

# Usamos episode como endpoints para acceder a la información de los episodios
episode_response = requests.get(base_url + "episode")


if episode_response.status_code == 200:
    episode_data = episode_response.json()["results"]

    # Contamos la aparición de los  personajes
    character_counts = count_character_appearances(episode_data)

    # Para conseguir el stop sorteamos el la lista de character_counts, en reversa desde de 0 a 5 
    # La función lambda se usa para decirle al sort como tiene que organizar los datos que tiene character_counts, en este caso
    # tiene que tomar el elemento x como imput y extraer el segundo elemento, x[1], de esta forma sorteamos por el segundo valor de cada x, pues
    # esto es lo que quiere la api
    top_characters = sorted(character_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    # Hacemos un api request para ver los nombres de los personajes que más aparecen
    character_names = {}
    for character, _ in top_characters:
        # Conseguimos el url de cara caracter para agregar como endpoint
        character_url = f"{base_url}character/{character}"
        # Guardamos respueesta
        character_response = requests.get(character_url)
        # De nuevo verificamos si si responde la api (Lo recomienda ChatGPT entonces lo dejo pero parece un poco redundante si ya verificamos
        # que funciona antes...)
        if character_response.status_code == 200:
            character_data = character_response.json()
            character_name = character_data["name"]
            character_names[character] = character_name

    # Imprimimos los 5 personajes que más aparecen ya añadiendo nombre a cada uno para que se entienda mejor
    for character, appearances in top_characters:
        character_name = character_names.get(character, "Unknown")
        print(f"{character_name}: {appearances} appearances in episodes")
else:
    print("No se puede acceder a la API")

# Respuestas
# Rick Sanchez: 20 appearances in episodes
# Morty Smith: 20 appearances in episodes
# Summer Smith: 14 appearances in episodes
# Jerry Smith: 14 appearances in episodes
# Beth Smith: 13 appearances in episodes
#-----------------------------------------------------------------------------------------------------------------------

# Fin del taller, lo que sigue son códigos de prueba con la PokeAPI
print("Fin del taller, lo que sigue son códigos de prueba con la PokeAPI")

#-----------------------------------------------------------------------------------------------------------------------
# Practica con las APIs
#------------------------------------------------------------------------------------------------------------------------
# Define the base URL for the PokeAPI
base_url = "https://pokeapi.co/api/v2/"

# Make a GET request to the 'pokemon' endpoint without specifying a specific Pokémon
response = requests.get(base_url + "pokemon")

# Check if the request was successful
if response.status_code == 200:
    # The response contains a 'count' field that represents the total number of Pokémon
    data = response.json()
    total_pokemon = data["count"]
    print(f"Total number of Pokémon: {total_pokemon}")
else:
    print("Failed to retrieve data from the PokeAPI, osea esa mierda no funciona")

# _____________________________________________________________________________________

# Define the base URL for the PokeAPI
base_url = "https://pokeapi.co/api/v2/"

# Make a GET request to the 'pokemon' endpoint to retrieve a list of Pokémon
response = requests.get(base_url + "pokemon")

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Iterate through the list of Pokémon and print the desired format
    for pokemon_data in data["results"]:
        pokemon_name = pokemon_data["name"]
        
        # Additional request to get more details about the Pokémon
        pokemon_details_response = requests.get(pokemon_data["url"])
        if pokemon_details_response.status_code == 200:
            pokemon_details = pokemon_details_response.json()
            pokemon_status = pokemon_details["height"]  # You can change this to any other status field you want
            pokemon_species = pokemon_details["species"]["name"]
            
            # Print the formatted string
            print(f"{pokemon_name}-{pokemon_status}-{pokemon_species}")
        else:
            print(f"Failed to retrieve details for {pokemon_name}")
else:
    print("Failed to retrieve data from the PokeAPI")
