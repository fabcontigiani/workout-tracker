from datetime import date
import ejercicio

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

    @peso.setter
    def peso(self, nuevo_peso: float):
        if (not isinstance(nuevo_peso, float)):
            print("Valor invalido.")
            return
        self.__peso = nuevo_peso

    def agregarEjercicio(self, objeto: ejercicio.Ejercicio,
                         fecha: str = date.today().isoformat()):
        """
        Acepta un objeto del tipo Ejercicio (PesoReps, Reps o Tiempo) y,
        opcionalmente, una string para indicar la fecha, en formato iso
        AAAA-MM-DD, que sera la key a la que estara asociada la lista a la cual
        se agregara el objeto. De no especificar una fecha tomara por defecto
        el dia de la fecha.

        @param objeto: Ejercicio a agregar
        @param fecha: Fecha en formato iso que hara de key del dicccionario
        """
        # Verifico que el usuario este logeado en la applicacion
        if (not self.__haIngresado):
            print("El usuario debe ingresar primero.")
            return

        if fecha not in self.__entrenamientos:
            self.__entrenamientos[fecha] = []
        self.__entrenamientos[fecha].append(objeto)
        print("Ejercicio agregado exitosamente.")

    def mostrarFecha(self, fecha: str = date.today().isoformat()):
        # Verifico que el usuario este logeado en la applicacion
        if (not self.__haIngresado):
            print("El usuario debe ingresar primero.")
            return

        # Verifico que la key ingresada exista en el diccionario
        if (fecha not in self.__entrenamientos):
            print("No hay ejercicios en esta fecha.")
            return

        # Recorro la lista de ejercicios correspondiente a la fecha(key)
        for value in self.__entrenamientos[fecha]:
            print(value)
