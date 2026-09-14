estudiantes = []

def agregar_estudiante(codigo, nombre):
    estudiante = {
        "codigo": codigo,
        "nombre": nombre,
        "notas": []
    }
    estudiantes.append(estudiante)

def mostrar_estudiantes():
    if not estudiantes:
        print("No existen estudiantes registrados.")
        return

    for estudiante in estudiantes:
        print(estudiante["codigo"], "-", estudiante["nombre"])

def buscar_estudiante(codigo):
    for estudiante in estudiantes:
        if estudiante["codigo"] == codigo:
            return estudiante
    return None

def eliminar_estudiante(codigo):
    estudiante = buscar_estudiante(codigo)
    if estudiante:
        estudiantes.remove(estudiante)
        return True
    return False