#1, 2, 3
Edad = 18 
Altura = 1.75
z = 8 + 6j 

#4
B = float(input("Ingresa El Valor: "))
A = float(input("Ingresa El Valor: "))
AR = 0.5 * B * A

#5
lA = float(input("Ingresa el Lado A:"))
lB = float(input("Ingresa el Lado B:"))
lC = float(input("Ingresa el Lado C:"))
P = lA + lB + lC 
print("El Perimetro es = ", P)

#6
L = float(input("ingresa la longitud:"))
An = float(input("ingresa la anchura:"))
A1 = L * An
P = 2 * (L + An)
print("la Area es: ",A1)
print("El Perimetro es: ", P)

#7
R = float(input("Ingresa el radio:"))
pi = 3.14
A2 = pi * R**2  
C = 2 * pi * R

#8, 9, 10
m = 2  # Pendiente
b = -2 # Intersección con el eje y

# Calcular la intersección con el eje x
# y = mx + b => 0 = 2x - 2
# 0 = 2x - 2 => x = 1
interseccion_x = -b / m

print("Pendiente (m): {m}")
print("Intersección con el eje y (b): (0, {b})")
print("Intersección con el eje x: ({interseccion_x}, 0)")

# La pendiente es (m = y2-y1/x2-x1). Halla la pendiente y la distancia euclidiana entre el punto (2, 2) y el punto (6, 10)
import math 
x1, y1 = 2, 2
x2, y2 = 6, 10
# Calcular la pendiente (m)
m = (y2 - y1) / (x2 - x1)
print(f"Pendiente (m): {m}")
# Calcular la distancia euclidiana
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distancia Euclidiana: {distancia}")

#11
x = float(input("ingresa el valor de x: "))
y= x**2 + 6*x + 9
if  y == 0:
    print("y es igual: ", y)
else:
    print("y no es igual a 0")

# 12
longitudPython = len("python")
longitudDragon = len("dragon")
print(longitudPython)
print(longitudDragon)

# 13
print("Ejercicio 13")
print('on' in "python" and 'on' in "dragon" )

# 14
print("Ejercicio 14")
print('jerga' in "Espero que este curso no esté lleno de jerga")

# 15
print("Ejercicio 15")
print(not 'on' in "python" and 'on' in "dragon")

# 16.
print("Ejercicio 16")
lonPython = len("python")
print(float(lonPython))
print(type(float(lonPython)))
print(str(lonPython))
print(type(str(lonPython)))

# 17
print("Ejercicio 17")
numero = int(input("ingresa un numero: ")) 
if numero % 2 == 0 :
    print("numero par")
else :
    print("numero impar")

# 18
print(7 // 3 == int(2.7)) 

# 19
print("Ejercicio 19")
print(type('10') == type(10))

# 20
print("Ejercicio 20")
print(int(9.8) == 10)

# 21
hours = int(input("horas de trabajo: "))
tarifa = int(input("tarifa por hora"))
salario = hours * tarifa 
print("tu salario es de: ", salario)

# 22
print("Ejercicio 22")
years = int(input("Ingresa los years:"))
life = years * 31540000
print("tiempo de vida en segundos son: ", life)   

# 23
print("Ejercicio 23")
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")