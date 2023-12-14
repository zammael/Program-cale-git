
nums = []

i = int(input ("Cuantos valores desea introducir? "))
for x in range(i):
    nums.append(int(input (f"Introduzca el valor numero {x+1}: ")))

def average(vals):
    res = 0
    for x in vals:
        res = res + x
    print("El promedio de los valores es: ")
    print(res/i)

def big(vals):
    y = 0
    z = 0
    p = 0
    for x in vals:
        z += 1
        if z == 1:
            y = x
            p = z
        if x > y:
            y = x
            p = z    # p se utiliza para tomar el valor del contador z cuando se haya encontrado el numero
    print("El numero mas grande de los valores es: ")
    print(y)
    print("Y su posicion es: ")
    print(p)

def small(vals):
    y = 0
    z = 0
    p = 0
    for x in vals:
        z += 1
        if z == 1:
            y = x
            p = z
        if x < y:
            y = x
            p = z
    print("El numero mas pequeño de los valores es: ")
    print(y)
    print("Y su posicion es: ")
    print(p)

average(nums)
big(nums)
small(nums)
