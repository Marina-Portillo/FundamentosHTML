# Tuplas
# (item1, item2, itemN)
# Inmutables
my_Tuple = ("uno",2,3.1,False)
print(type(my_Tuple))
print(my_Tuple[0])
print(my_Tuple[-1])
#error
#my_Tuple[0] = "nuevo Valor"


#Conjuntos Set
#{item1, item2, itemN}
#Coleccion sin índice y sin duplicados
my_set ={1,2,2,2,3,4,"uno"}
print(type(my_set))
print(my_set)
my_set.add(5)
a = {1,2,3,4}
b= {4,5,6,7}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# Diccionarios
# {item1: valor, item2: valor}
alumno ={
    "name": "Goku",
    "lastname": "Sayayin",
    "age": 19,
    "genero": "H",
    "calificaciones": [9,9,9]
}
print(type(alumno))
print(alumno)
print(alumno["name"],alumno["lastname"])
if alumno["age"] < 18:
    print("Es menor de Edad")
alumno["calificaciones"].append(10)
print(alumno["calificaciones"])
