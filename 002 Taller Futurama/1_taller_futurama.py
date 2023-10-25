import requests # Importo request... para poder hacer requests

base_url = "https://api.sampleapis.com/futurama/characters" # Indico mi endpoint
response = requests.get(base_url) # Pido que me responda mi endpoint :c 
data = response.json() # Guardo mi info en un .json

# Creo las listas para guardar a los personajes de acuerdo a su genero
Male = []
Female = []
Non_binary = []

# Primero veo cuales generos hay (Inclusión ante todo))
# for character in data:
 #    print(character["gender"])

# Ahora los agrego a las listas de acuerdo a su genero
for character in data:
    if character["gender"] == "Male":
        Male.append(character["name"]["first"])
    elif character["gender"] == "Female":
        Female.append(character["name"]["first"])
    else:
        Non_binary.append(character["name"]["first"])

# Imprimimos las listas
print(Male)
print(Female)
print(Non_binary)