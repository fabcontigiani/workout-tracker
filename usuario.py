from datetime import date

class Usuario:
    def __init__(self, nombre: str, contrasena: str, peso: float):
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__peso = peso
        self.__entrenamientos = {}
        self.__haIngresado = False

    def __str__(self):
        return f"Nombre: {self.__nombre} | Contrasena: {self.__contrasena} | Peso: {self.__peso} | Ingresado: {self.__haIngresado}"

    @property
    def nombre(self):
        return self.__nombre

    @property
    def contrasena(self):
        return self.__contrasena

    @property
    def peso(self):
        return self.__peso

    def toggleIngreso(self):
        self.__haIngresado = not self.__haIngresado

    def agregarEjercicio(self):
        print("[1] Peso+Reps\n[2] Reps\n[3] Tiempo")
        tipo = input("Tipo de ejercicio >> ")
        if tipo == 1:
            peso = input("Peso (en kg):")
            while(not isinstance(peso, float)):
                print("Por favor, ingrese un valor valido.\n")
                peso = input("Peso (en kg):")
            reps = input("Nro de repeticiones: ")
            while (not isinstance(reps, int)):
                print("Por favor, ingrese un valor valido.\n")
                reps = input("Nro de repeticiones: ")
            sets = input("Nro de series: ")
            while (not isinstance(sets, int)):
                print("Por favor, ingrese un valor valido.\n")
                sets = input("Nro de sets: ")
        elif tipo == 2:
            pass
        elif tipo == 3:
            pass
        else:
            print("Tipo de ejercicio invalido.")
            return
