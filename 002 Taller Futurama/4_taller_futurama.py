import requests # Importo request... para poder hacer requests

base_url = "https://api.sampleapis.com/futurama/characters" # Indico mi endpoint
response = requests.get(base_url) # Pido que me responda mi endpoint :c 
data = response.json() # Guardo mi info en un .json

EdadesMale = []
EdadesFemale = []
EdadesNon_binaty = []

for character in data:
    if character["gender"] == "Male":
        EdadesMale.append(int(character["age"]))
    if character["gender"] == "Female":
        EdadesFemale.append(int(character["age"]))
    else:
        EdadesNon_binaty.append(int(character["age"]))

print(EdadesNon_binaty)
print(EdadesFemale)
print(EdadesMale)