import requests

base_url = "http://10.203.1.15:8000/"

response = requests.get(base_url)



data = response.json()

sedes = list({value["Sede Andina"] for key, value in data.items()})

anos = list({value["Año"] for key, value in data.items()})


print(sedes)
print(anos)

programas = {x : [] for x in anos}
for programa in programas:
    programas.update({programa : [value for key, value in data.items() if value["Año"]== programa]})

print(programas)