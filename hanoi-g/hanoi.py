# Recursive Python function to solve the tower of hanoi
def resultadohanoi (disks, source, middle, destination):
    if disks >= 1: 
        resultadohanoi(disks-1,source, destination, middle)
        print("Mover el disco de Torres", source, "a",destination)
        resultadohanoi(disks-1,middle, source, destination)

resultadohanoi(3, 1, 2, 3)
