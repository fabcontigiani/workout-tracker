import usuario

class App:
    def __init__(self):
        self.__nombre = "Workout Tracker"
        self.__usuarios = []

    def registrarUsuario(self, nombre: str, contrasena: str, peso: float):
        for item in self.__usuarios:
            if nombre == item.nombre:
                print("Usuario ya registrado.")
                return
        item = usuario.Usuario(nombre, contrasena, peso)
        self.__usuarios.append(item)
        print("Usuario registrado exitosamente.")

    def mostrarUsuarios(self):
        for item in self.__usuarios:
            print(item)

    def iniciarSesion(self, nombre: str, contrasena: str):
        for item in self.__usuarios:
            if nombre == item.nombre:
                if contrasena == item.contrasena:
                    item.ingresar()
                    print("Ha ingresado exitosamente.")
                    return item
                else:
                    print("Contrasena incorrecta.")
                    return
        print("El usuario ingresado no ha sido registrado aun.")

    def cerrarSesion(self, nombre: str):
        for item in self.__usuarios:
            if nombre == item.nombre:
                item.salir()
                print("Ha cerrado sesion exitosamente.")
                return
        print("Usuario no encontrado.")


    def eliminarUsuario(self, nombre: str):
        for item in self.__usuarios:
            if nombre == item.nombre:
                self.__usuarios.remove(item)
                print("Usuario eliminado exitosamente.")
                return
        print("Usuario no encontrado.")
