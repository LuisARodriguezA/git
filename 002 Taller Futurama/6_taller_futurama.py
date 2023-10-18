import requests # Importo request... para poder hacer requests

base_url = "https://api.sampleapis.com/futurama/characters" # Indico mi endpoint
response = requests.get(base_url) # Pido que me responda mi endpoint :c 
data = response.json() # Guardo mi info en un .json

# Creo las listas para guardar los nombres completos
NombresCompletos = []
Prueba = []
NombresSinEspacios = []

# Utilizamos el método format para agregar a una lista los Nombrs completos de los personajes
for character in data:
    NombresCompletos.append("{} {} {}".format(character["name"]["first"],character["name"]["middle"],character["name"]["last"]))

# Usamos replace para remplazar los dobles espacios de los personajes que no tienen middle name
for x in NombresCompletos:
    NombresSinEspacios.append(((x.replace("  "," ")).lstrip()))

# Imprimimos la lista :)
print(NombresSinEspacios)
    