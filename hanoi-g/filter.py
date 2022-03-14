"""Filter crea una lista de elementos, para que una lista de funcion devulve verdadero, 
a diferencia de map que solo agrego una operacion. Filter simplemente nos realiza una comparación,
dependiendo de lo que le enviemos en una función. """

numbers = [1,2,3,4,5,6]
even = []
for value in numbers:
    if (value % 2 == 0):
        even.append(value)
print(even)
#ahora utilizo filter
def iseven (number)