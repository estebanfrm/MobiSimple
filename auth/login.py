def login_user(file_path):
    email = input("Correo: ")
    password = input("Contraseña: ")

    with open(file_path, "r") as f:
        users = f.readlines()

    for user in users:
        name, user_email, user_password = user.strip().split(",")
        if user_email == email and user_password == password:
            print(f"✅ Bienvenido, {name}!")
            return True

    print("❌ Usuario o contraseña incorrectos.")
    return False
