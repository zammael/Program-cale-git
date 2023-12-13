

i = int(input ("Cuantos valores desea introducir? "))
res = 0
for x in range(i):
    nums = int(input (f"Introduzca el valor numero {x+1}: "))
    res = res + nums
    
print("El promedio de los valores es: ")
print(res/i)