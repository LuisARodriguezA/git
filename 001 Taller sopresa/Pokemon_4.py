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
    print("Failed to retrieve Pokémon data from the PokeAPI")

# Resultado
# Bug: 6 Pokémon
# Fire: 3 Pokémon
# Flying: 5 Pokémon
# Grass: 3 Pokémon
# Normal: 5 Pokémon
# Poison: 6 Pokémon
# Water: 3 Pokémon