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