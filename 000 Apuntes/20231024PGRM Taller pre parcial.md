
2023-10-24
18:00:59
Tags: #UNAL #PGRM #Python 
___
# Taller pre parcial
___
## Agrupar por genero a los personajes
```run-python
def gender_groupby(data, generos):
    #Get all genders with set and dict comprenhension //https://michaeliscoding.com/how-to-create-a-list-of-unique-items-with-a-comprehension-in-python/

    #lista de personajes agrupados por generos
    generos = {genero : [] for genero in generos}
    for genero in generos:
        generos.update({genero : [value for key, value in data.items() if value['gender'] == genero]})
    
    print(generos)
```
___
# Sources
1. [How to create a list of unique items with a comprehension in Python](https://michaeliscoding.com/how-to-create-a-list-of-unique-items-with-a-comprehension-in-python/)
___