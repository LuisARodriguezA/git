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