
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

average(nums)