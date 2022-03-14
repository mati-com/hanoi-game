#Primero utilizo un arreglo vacio y un For
numbers= [1,2,3,4,5,6]
update = []
for value in numbers:
    #Multiplicación
    update.append(value*2)
print(update)

#Ahora utlizo map funtion
def operation (value):
    return value*2
print((list(map(operation,numbers))))

#Puedo escribir menos codigo utilizando lambda
print(list(map((lambda value: value*2),numbers)))
