#Almacenar las edades de 6 estudiantes
edades = []

def almacenar_edades(edad):
    edades.append(edad)

def mostrar_edades():
    return edades

for i in range(10):
    while True:
        try:
            edad = int(input(f"Estudiante # {i + 1} dime tu edad: "))
            almacenar_edades(edad)
            break
        except ValueError:
            print("Se debe ingresar un numero entero")