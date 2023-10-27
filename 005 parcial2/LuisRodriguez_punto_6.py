enteros = [1,2,3,4,5]

cuadrados = [x**2 for x in enteros]

print(cuadrados)

# __________________________________________

nombres1 = ["Juan","Ana","Pedro","Luisa"]

nombres_final=list(filter(lambda x: len(x)==4, nombres1))

print(nombres_final)

# __________________________________________

lista_C = [0,20,25,30,35]

lista_F = list(map(lambda x:(x*(9/5)+32), lista_C))

print(lista_F)

#___________________________________________

n = [1,2,3,4,5,6,7,8,9,10]

n_par =[x for x in n if x%2 == 0]

print(n_par)


#___________________________________________

palabras = ["casa", "sapo"]

palabras_c = list(filter(lambda x: x[0]=="c",palabras))

print(palabras_c)