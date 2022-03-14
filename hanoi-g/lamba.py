#Sin la utilización de lambda
def x(y):
    y = y*2
    return y 
print(x(5))

#Utilizo lambda
x = lambda y: y*2
print(x(5))