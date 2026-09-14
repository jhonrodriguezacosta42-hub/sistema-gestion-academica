def validar_nombre(nombre):
    if not nombre.strip():
        return False
    return True

def validar_nota(nota):
    return 0 <= nota <= 5

def validar_codigo(codigo):
    return codigo.isdigit()

print(validar_nota(4.5))
print(validar_nota(7))
