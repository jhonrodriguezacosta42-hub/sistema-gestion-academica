from archivos import guardar_datos, cargar_datos
from estudiantes import (
    agregar_estudiante,
    mostrar_estudiantes,
    buscar_estudiante,
    eliminar_estudiante,
    estudiantes
)

from notas import (
    agregar_nota,
    calcular_promedio,
    estado_estudiante
)

def menu():
    # Al iniciar el programa, cargamos lo
    # que ya estaba guardado en datos.json
    global estudiantes
    estudiantes[:] = cargar_datos()

    while True:
        print("=====================================")
        print("      SISTEMA DE GESTIÓN ACADÉMICA")
        print("=====================================")
        print("1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Registrar nota")
        print("5. Consultar promedio")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            agregar_estudiante(codigo, nombre)
            guardar_datos(estudiantes)
            print("Estudiante registrado correctamente.")

        elif opcion == "2":
            mostrar_estudiantes()

        elif opcion == "3":
            codigo = input("Código a buscar: ")
            est = buscar_estudiante(codigo)
            print(est if est else "No encontrado.")

        elif opcion == "4":
            codigo = input("Código del estudiante: ")
            est = buscar_estudiante(codigo)

            if est:
                try:
                    nota = float(input("Nota (0 a 5): "))

                    if agregar_nota(est, nota):
                        guardar_datos(estudiantes)
                        print("Nota registrada correctamente.")
                    else:
                        print("La nota debe estar entre 0 y 5.")

                except ValueError:
                    print("Error: debe ingresar un número.")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "5":
            codigo = input("Código del estudiante: ")
            est = buscar_estudiante(codigo)

            if est:
                print("Promedio:", calcular_promedio(est))
                print("Estado:", estado_estudiante(est))
            else:
                print("Estudiante no encontrado.")

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()