from auth.register import register_user
from auth.login import login_user

FILE_PATH = "data/users.txt"

def main():
    print("1. Registrarse")
    print("2. Iniciar sesión")
    choice = input("Elige una opción: ")

    if choice == "1":
        register_user(FILE_PATH)
    elif choice == "2":
        login_user(FILE_PATH)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
