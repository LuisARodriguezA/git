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