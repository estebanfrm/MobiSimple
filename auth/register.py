import re

def es_correo_valido(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None

def register_user(file_path):
    name = input("Nombre: ")
    email = input("Correo: ")
    if not es_correo_valido(email):
        print("❌ Correo inválido. Debe tener formato usuario@dominio.com")
        return
    password = input("Contraseña: ")

    with open(file_path, "a") as f:
        f.write(f"{name},{email},{password}\n")

    print("✅ Registro exitoso.")
