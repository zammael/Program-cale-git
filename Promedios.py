
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
    x = 0
    y = 0
    for x in vals:
        if x > y:
            y = x
    print("El numero mas grande de los valores es: ")
    print(y)

def small(vals):
    x = 0
    y = 0
    z = 0
    for x in vals:
        if y == z:
            y = x
        if x < y:
            y = x
    print("El numero mas pequeño de los valores es: ")
    print(y)

average(nums)
big(nums)
small(nums)