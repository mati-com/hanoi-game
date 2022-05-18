# Función recursiva de Python para resolver la torre de hanoi
# Primera forma
def resultadohanoi (disks, source, middle, destination):
    if disks >= 1: 
        resultadohanoi(disks-1,source, destination, middle)
        print("Mover el disco de Torres", source, "a",destination)
        resultadohanoi(disks-1,middle, source, destination)

resultadohanoi(3, 1, 2, 3)


# Función recursiva de Python para resolver la torre de hanoi
# Segunda forma mas compleja

def TorredeHanoi(n , source2, destination2, auxiliary):
	if n==1:
		print ("Mover el disco 1 desde la fuente",source2,"al destino",destination2)
		return
	TorredeHanoi(n-1, source2, auxiliary, destination2)
	print ("Mover el disco",n,"de la fuente",source2,"al destino",destination2)
	TorredeHanoi(n-1, auxiliary, destination2, source2)
		
# A, C, B el nombre de los "palitos" del hanoi
n = 4
TorredeHanoi (n,'A','B','C')