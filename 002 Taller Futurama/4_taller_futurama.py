import requests # Importo request... para poder hacer requests
import matplotlib.pyplot as plt # Usamos matplotlib para graficar todo


base_url = "https://api.sampleapis.com/futurama/characters" # Indico mi endpoint
response = requests.get(base_url) # Pido que me responda mi endpoint :c 
data = response.json() # Guardo mi info en un .json

# Creamos las listas en las que vamos a guardar las edades
EdadesMale = []
EdadesFemale = []

# Tenemos una edad que es desconocida, por lo que voy a modificar data para que sea iguial a 0
# Esto con la intención de que no sea un problema al momento de guardar los datos como int.
for character in data:
    if character["age"] == "Unknown": 
        character["age"] = 0

for character in data:
    if character["gender"] == "Male": # Mirar si el personaje es Male y guardar su edad en la lista para EdadesMale
        EdadesMale.append(int(character["age"]))
    else:
        EdadesFemale.append(int(character["age"])) # Si es Female guardar en la otra lista :)

# Plot del primer histograma
plt.hist(EdadesFemale, label='Female', bins=14, alpha=.7, edgecolor='red')
 
# Plot del segundo histograma
plt.hist(EdadesMale, label="Male", bins=14, alpha=.7, edgecolor='yellow')

# Titulo del plot
plt.title("Histograma de edades de los personajes de Futurama Agrupados por género")
 
# Ahora vamos contando cada individuo identificando su indice correspondiente
plt.show()