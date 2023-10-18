import requests # Importo request... para poder hacer requests
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


base_url = "https://api.sampleapis.com/futurama/characters" # Indico mi endpoint
response = requests.get(base_url) # Pido que me responda mi endpoint :c 
data = response.json() # Guardo mi info en un .json


edades = []
AgeInd = []
Cantidad = []

for character in data:
    if character["age"] == "Unknown":
            edades.append(0)
    else:
         edades.append(int((character["age"])))
[AgeInd.append(x) for x in edades if x not in AgeInd]
AgeInd.sort()

for x in range(len(AgeInd)):
    Cantidad.append(0)

for character in data:
    if character["age"] == "Unknown":
        Cantidad[0] = Cantidad[0] + 1
    else: 
        index = AgeInd.index(int((character["age"])))
        Cantidad[index] = Cantidad[index] + 1

print(edades)
print(AgeInd)
print(Cantidad)

# Creating histogram

plt.title("Histograma de edades de los personajes de Futurama")
plt.hist(edades, bins = 20, range=(0,210))
plt.show()

