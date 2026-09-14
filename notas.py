def agregar_nota(estudiante, nota):
    if 0 <= nota <= 5:
        estudiante["notas"].append(nota)
        return True
    return False


def calcular_promedio(estudiante):
    notas = estudiante["notas"]
    if not notas:
        return 0
    return sum(notas) / len(notas)


def estado_estudiante(estudiante):
    promedio = calcular_promedio(estudiante)
    if promedio >= 3:
        return "APROBADO"
    return "NO APROBADO"
    try:
    nota = float(input("Digite la nota: "))

    if nota < 0 or nota > 5:
        print("La nota debe estar entre 0 y 5.")
    else:
        print("Nota válida.")

except ValueError:
    print("Error: debe ingresar un número.")
