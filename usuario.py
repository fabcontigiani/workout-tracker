from datetime import date
import ejercicio

class Usuario:
    def __validarFecha(fecha: str) -> bool:
        returnValue = True
        try:
            date.fromisoformat(fecha)
        except ValueError:
            returnValue = False
        return returnValue

    def __init__(self, nombre: str, contrasena: str, peso: float):
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__peso = peso
        self.__entrenamientos = {}
        self.__haIngresado = False

    def __str__(self):
        return f"Nombre: {self.nombre} | Contrasena: {self.contrasena} | Peso: {self.peso} kgs | Ingresado: {self.haIngresado}"

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

    @property
    def haIngresado(self):
        """Retorna el estado de ingreso del usuario."""
        return self.__haIngresado

    def ingresar(self):
        """Cambia el estado de ingreso del usuario a verdadero."""
        self.__haIngresado = True

    def salir(self):
        """Cambia el estado de ingreso del usuario a falso."""
        self.__haIngresado = False

    def agregarEjercicio(self, nombre: str,
                         fecha: str = date.today().isoformat(),
                         peso: int = None,
                         reps: int = None,
                         sets: int = None,
                         tiempo: int = None):
        # Verifico que el usuario este logeado en la applicacion
        if (not self.__haIngresado):
            print("El usuario debe ingresar primero.")
            return

        # Si la key (fecha) no existe en el diccionario la inicializo con
        # una lista vacia
        if fecha not in self.__entrenamientos:
            self.__entrenamientos[fecha] = []

        # Validar fecha
        if not Usuario.__validarFecha(fecha):
            print("Formato de fecha invalido, debe ser AAAA-MM-DD.")
            return

        if (isinstance(peso, int) and isinstance(reps, int) and
                isinstance(sets, int) and tiempo is None):
            # Tipo PesoReps
            if (peso < 1 or reps < 1 or sets < 1):
                print("Valor entero menor a uno.")
                return
            self.__entrenamientos[fecha].append(
                ejercicio.PesoReps(nombre, peso, reps, sets))
        elif (isinstance(reps, int) and isinstance(sets, int) and
                tiempo is None and peso is None):
            # Tipo Reps
            if (reps < 1 or sets < 1):
                print("Valor entero menor a uno.")
                return
            self.__entrenamientos[fecha].append(
                ejercicio.Reps(nombre, self.peso, reps, sets))
        elif (isinstance(tiempo, int) and peso is None and reps is None
                and sets is None):
            # Tipo Tiempo
            if tiempo < 1:
                print("Valor entero menor a uno.")
                return
            self.__entrenamientos[fecha].append(
                ejercicio.Tiempo(nombre, tiempo))
        else:
            print("Ejercicio invalido.")

    def mostrarFecha(self, fecha: str = date.today().isoformat()):
        # Verifico que el usuario este logeado en la applicacion
        if (not self.__haIngresado):
            print("El usuario debe ingresar primero.")
            return

        # Validar fecha
        if not Usuario.__validarFecha(fecha):
            print("Formato de fecha invalido, debe ser AAAA-MM-DD.")
            return

        # Verifico que la key ingresada exista en el diccionario
        if (fecha not in self.__entrenamientos):
            print("No hay ejercicios en esta fecha.")
            return

        # Recorro la lista de ejercicios correspondiente a la fecha(key)
        print(f">> {fecha} <<")
        for value in self.__entrenamientos[fecha]:
            print(value)

    def quitarEjercicio(self, nombre: str,
                        fecha: str = date.today().isoformat()):
        # Verifico que el usuario este logeado en la applicacion
        if (not self.__haIngresado):
            print("El usuario debe ingresar primero.")
            return

        # Validar fecha
        if not Usuario.__validarFecha(fecha):
            print("Formato de fecha invalido, debe ser AAAA-MM-DD.")
            return

        # Verifico que la fecha sea una key valida
        if fecha not in self.__entrenamientos:
            print("No hay ejercicios en esta fecha.")
            return

        for item in self.__entrenamientos[fecha]:
            if nombre == item.nombre:
                self.__entrenamientos[fecha].remove(item)
                print("Ejercicio eliminado exitosamente.")
                return
        print("Ejercicio no encontrado.")

    def volumenFecha(self, fecha: str = date.today().isoformat()):
        # Verifico que el usuario este logeado en la applicacion
        if (not self.__haIngresado):
            print("El usuario debe ingresar primero.")
            return

        # Validar fecha
        if not Usuario.__validarFecha(fecha):
            print("Formato de fecha invalido, debe ser AAAA-MM-DD.")
            return

        # Verificar que la key (fecha) existe en el diccionario
        if fecha not in self.__entrenamientos:
            print("La fecha ingresada no existe en el diccionario.")
            return

        acumulador = 0
        for item in self.__entrenamientos[fecha]:
            acumulador += item.volumen()
        print(f"El volumen de entrenamiento realizado el dia {fecha} es de {acumulador:.2f} kgs.")
