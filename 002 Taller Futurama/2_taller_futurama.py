import requests # Importo request... para poder hacer requests

base_url = "https://api.sampleapis.com/futurama/characters" # Indico mi endpoint
response = requests.get(base_url) # Pido que me responda mi endpoint :c 
data = response.json() # Guardo mi info en un .json

Especies = []
Cantidad = []
EspeciesIndividuales = []

for character in data:
    Especies.append(character["species"])

# Especies = list(set(Especies))

[EspeciesIndividuales.append(x) for x in Especies if x not in EspeciesIndividuales]

print(EspeciesIndividuales)

for x in range(len(EspeciesIndividuales)):
    Cantidad.append(0)

print(Cantidad)

for character in data:
    index = EspeciesIndividuales.index(character["species"])
    Cantidad[index] = Cantidad[index] + 1

print(Cantidad)