import requests # Importo request... para poder hacer requests
import matplotlib.pyplot as plt

base_url = "https://api.sampleapis.com/futurama/characters" # Indico mi endpoint
response = requests.get(base_url) # Pido que me responda mi endpoint :c 
data = response.json() # Guardo mi info en un .json

Especies = []
Cantidad = []
EspeciesIndividuales = []

# Creamos una lista con todas las especies
for character in data:
    Especies.append(character["species"])


# Especies = list(set(Especies)) <--- Un metodo para eliminar items repetidos en una lista
# Decidí usar este metodo pues usa Comprensión de listas, lo cual hace más cool el codigo
[EspeciesIndividuales.append(x) for x in Especies if x not in EspeciesIndividuales]

# Creamos una lista para guardar la cuantos ind. hay de cada especie
for x in range(len(EspeciesIndividuales)):
    Cantidad.append(0)

# Ahora vamos contando cada individuo identificando su indice correspondiente
for character in data:
    index = EspeciesIndividuales.index(character["species"])
    Cantidad[index] = Cantidad[index] + 1

# Usamos matplotlib para graficar todo

# Establecemos el tamaño de la figura
fig = plt.figure(figsize = (10, 5))

# Creamos el plot de color azul con las variables x y y respectivas
plt.bar(EspeciesIndividuales, Cantidad, color ='blue', 
        width = 0.5)

# Ponemos nombres a los ejes
plt.xlabel("Especies")
plt.ylabel("Camtodad de personajes")
plt.title("Cantidad de personajes por Especie")

# Pongo manca de agua... porque uno nunca sabe
fig.text(0.9, 0.15, 'LuisARodriguezA', fontsize = 12,
         color ='grey', ha ='right', va ='bottom',
         alpha = 0.7)

# Sacamos el plot :)
plt.show()