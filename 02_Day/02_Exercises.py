#Exercices 02
Primer_Nombre = "Axel"
Segundo_Nombre = "Yael"
Apellidos = "Martínez Martínez"
Nombre_Completo = "Axel Yael Martínez Martínez"

Pais_de_Origen = "Estados Unidos Mexicanos"
Ciudad_de_Recidencia = "Aguascalientes, Ags."

Edad = "18 Años"
Año_en_Curso = "2025" 

is_married = "No esta Casado"
is_true = True

Gustos_Personales = {
    "Armar Model kits", 
    "Escuchar a Ado",
    "Cocinar", 
    "Dibujar",
    "Leer Manga",
    "Jugar Video Juegos"
}
#Imprimir las Variables
print("Apellidos - ", Apellidos ,type(Apellidos))
print("Nombre Completos - ", Nombre_Completo, type(Nombre_Completo), len(Nombre_Completo))
print("Pais de Origen - ", Pais_de_Origen, type(Pais_de_Origen))
print("Ciudad de Recidencia - ", Ciudad_de_Recidencia, type(Ciudad_de_Recidencia))
print("Edad - ", Edad, type(Edad))
print("Año - ", Año_en_Curso, type(Año_en_Curso))
print("Esta Casado - ", is_married, type(is_married))
print("Gustos Personales - ", Gustos_Personales, type(Gustos_Personales))

#Exercises_02_Part_2
print("////////////////////////////////////////////////////////////////////////////////")
N1 = 5
N2 = 4

Suma = N1 + N2
Resta = N1 - N2
Multiplicacion = N1 * N2
Division = N1 / N2
Potencia = N1 ** N2
Floor_Division = N1 // N2
#Imprimir las Variables
print("Los resultados son los siguientes -")
print("Suma - ", Suma)
print("Resta - ", Resta)
print("Multiplicacion -", Multiplicacion)
print("Division - ", Division)
print("Potencia - ", Potencia)
print("Floor Division - ", Floor_Division)

#Exercises_02_circle
print("////////////////////////////////////////////////////////////////////////////////")
Radio = 30
Diametro = 60

Area = 3.1416 * Radio**2
Circunferencia = 301416 * Diametro
#Imprimir los Valores
print("El Area del Circulo es = ", Area)
print("La Circunferencia del Circulo es = ", Circunferencia)

print("////////////////////////////////////////////////////////////////////////////////")
R2 = int(input("Ingresa el Radio Deseado = "))
print ("El radio que ingresaste es = ", R2)

A2 = 3.1416 * R2**2
print("El Area del Circulo es = ", A2)