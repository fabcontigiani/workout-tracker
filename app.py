import usuario

class App:
    def __init__(self):
        self.__nombre = "Workout Tracker"
        self.__usuarios = []

    def registrarUsuario(self, nombre: str, contrasena: str, peso: float):
        if (not isinstance(nombre, str) or not isinstance(contrasena, str) or
                not isinstance(peso, float)):
            print("Argumentos invalidos")
            return

        for item in self.__usuarios:
            if nombre == item.nombre:
                print("Usuario ya registrado.")
                return
        item = usuario.Usuario(nombre, contrasena, peso)
        self.__usuarios.append(item)

    def mostrarUsuarios(self):
        for item in self.__usuarios:
            print(item)

    def iniciarSesion(self, nombre: str, contrasena: str):
        if (not isinstance(nombre, str) or not isinstance(contrasena, str)):
            print("Argumentos invalidos")
            return

        for item in self.__usuarios:
            if nombre == item.nombre:
                if contrasena == item.contrasena:
                    if item.haIngresado is True:
                        print("El usuario ya inicio sesion previamente.")
                        return
                    item.haIngresado = True
                    return item
                else:
                    print("Contrasena incorrecta.")
                    return
        print("El usuario ingresado no ha sido registrado aun.")

    def cerrarSesion(self, nombre: str):
        if not isinstance(nombre, str):
            print("Argumento invalido")
            return

        for item in self.__usuarios:
            if nombre == item.nombre:
                if item.haIngresado is False:
                    print("El usuario ya cerro sesion previamente.")
                    return
                item.haIngresado = False
                return
        print("Usuario no encontrado.")

    def eliminarUsuario(self, nombre: str):
        if not isinstance(nombre, str):
            print("Argumento invalido")
            return

        for item in self.__usuarios:
            if nombre == item.nombre:
                self.__usuarios.remove(item)
                return
        print("Usuario no encontrado.")
