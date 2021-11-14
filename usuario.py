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
        return self.__haIngresado

    def ingresar(self):
        self.__haIngresado = True

    def salir(self):
        self.__haIngresado = False

    def agregarEjercicio(self, objeto: object,
                         fecha: str = date.today().isoformat()):
        # Verifico que el usuario este logeado en la applicacion
        if (not self.__haIngresado):
            print("El usuario debe ingresar primero.")
            return

        # Si la key (fecha) no existe en el diccionario la inicializo con
        # una lista vacia
        if fecha not in self.__entrenamientos:
            self.__entrenamientos[fecha] = []
        self.__entrenamientos[fecha].append(objeto)
        print("Ejercicio agregado exitosamente.")

    def agregarEjercicio2(self, tipo: int, nombre: str,
                          fecha: str = date.today().isoformat(),
                          peso: int = None, reps: int = None,
                          sets: int = None, tiempo: int = None):
        # Verifico que el usuario este logeado en la applicacion
        if (not self.__haIngresado):
            print("El usuario debe ingresar primero.")
            return

        # Si la key (fecha) no existe en el diccionario la inicializo con
        # una lista vacia
        if fecha not in self.__entrenamientos:
            self.__entrenamientos[fecha] = []

        if tipo == 1:
            # Tipo PesoReps
            if peso is not None and isinstance(peso, int):
                if reps is not None and isinstance(reps, int):
                    if sets is not None and isinstance(sets, int):
                        self.__entrenamientos[fecha].append(
                            ejercicio.PesoReps(nombre, peso, reps, sets))
                    else:
                        print("Nro de sets invalido.")
                        return
                else:
                    print("Nro de reps invalido.")
                    return
            else:
                print("Peso invalido.")
                return
        elif tipo == 2:
            pass
        elif tipo == 3:
            pass
        else:
            print("Tipo de ejercicio incorrecto")

    def agregarEjercicio3(self, nombre: str,
                          fecha: str = date.today().isoformat(),
                          peso: int = None, reps: int = None, sets: int = None,
                          tiempo: int = None):

        # Verifico que el usuario este logeado en la applicacion
        if (not self.__haIngresado):
            print("El usuario debe ingresar primero.")
            return

        # Si la key (fecha) no existe en el diccionario la inicializo con
        # una lista vacia
        if fecha not in self.__entrenamientos:
            self.__entrenamientos[fecha] = []

        # TODO Validar fecha

        if (isinstance(peso, int) and isinstance(reps, int) and
                isinstance(sets, int) and tiempo is None):
            # Tipo PesoReps
            self.__entrenamientos[fecha].append(
                ejercicio.PesoReps(nombre, peso, reps, sets))
        elif (isinstance(reps, int) and isinstance(sets, int) and
                tiempo is None and peso is None):
            # Tipo Reps
            self.__entrenamientos[fecha].append(
                ejercicio.Reps(nombre, self.pesoCorporal, reps, sets))
        elif (isinstance(tiempo, int) and peso is None and reps is None
                and sets is None):
            # Tipo Tiempo
            self.__entrenamientos[fecha].append(
                ejercicio.Tiempo(nombre, tiempo))
        else:
            print("Ejercicio invalido.")

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
        print(f">> {fecha} <<")
        for value in self.__entrenamientos[fecha]:
            print(value)

    def quitarEjercicio(self, nombre: str,
                       fecha: str = date.today().isoformat()):
        # Verifico que el usuario este logeado en la applicacion
        if (not self.__haIngresado):
            print("El usuario debe ingresar primero.")
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

        # Verificar que la key (fecha) existe en el diccionario
        if fecha not in self.__entrenamientos:
            print("La fecha ingresada no existe en el diccionario.")
            return

        acumulador = 0
        for item in self.__entrenamientos[fecha]:
            acumulador += item.volumen()
        print(f"El volumen de entrenamiento realizado el dia {fecha} es de {acumulador:.2f} kgs.")
