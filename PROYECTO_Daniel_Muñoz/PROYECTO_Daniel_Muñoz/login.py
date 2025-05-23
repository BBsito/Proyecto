import csv

USERS_FILE = "users.csv"

def cargar_usuarios() -> dict:
    usuarios: dict = {}
    try:
        with open(USERS_FILE, "r", encoding="utf-8", newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    usuario, password = row
                    usuarios[usuario] = password
    except FileNotFoundError:
        pass
    return usuarios

def guardar_usuarios(usuarios: dict) -> None:
    with open(USERS_FILE, "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        for usuario, password in usuarios.items():
            writer.writerow([usuario, password])

def registrar_usuario() -> None:
    usuarios: dict = cargar_usuarios()
    print("=== Registro de usuario ===")
    while True:
        usuario: str = input("Nuevo nombre de usuario: ").strip()
        if not usuario:
            print("El nombre no puede estar vacío.")
            continue
        if usuario in usuarios:
            print("Ese usuario ya existe.")
            continue
        break
    while True:
        password: str = input("Nueva contraseña: ").strip()
        if not password:
            print("La contraseña no puede estar vacía.")
            continue
        break
    usuarios[usuario] = password
    guardar_usuarios(usuarios)
    print("Usuario registrado correctamente.\n")

def login() -> bool:
    usuarios: dict = cargar_usuarios()
    print("=== Login ===")
    for _ in range(3):
        usuario: str = input("Usuario: ").strip()
        password: str = input("Contraseña: ").strip()
        if usuario in usuarios and usuarios[usuario] == password:
            print(f"Bienvenido, {usuario}.\n")
            return True
        else:
            print("Usuario o contraseña incorrectos.")
    print("Demasiados intentos fallidos. Saliendo del programa.")
    return False
