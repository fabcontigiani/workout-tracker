from datetime import date
import Ejercicio

class Usuario:
    def __init__(self, nombre: str, contrasena: str, peso: float):
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__peso = peso
        self.__entrenamientos = {}
        self.__haIngresado = False

    def __str__(self):
        return f"Nombre: {self.__nombre} | Contrasena: {self.__contrasena} | \
        Peso: {self.__peso} | Ingresado: {self.__haIngresado}"

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
        # Prompt al usuario para elegir tipo de ejercicio
        print("[1] Peso+Reps\n[2] Reps\n[3] Tiempo")
        tipo = input("Tipo de ejercicio >> ")

        if tipo == 1:
            # Tipo Peso + Reps
            nombre = input("Nombre del ejercicio >> ")
            while(not isinstance(nombre, str)):
                print("Por favor, ingrese un valor valido.\n")
                nombre = input("Nombre del ejercicio >> ")
            grupoMuscular = input("Grupo muscular >> ")
            while(not isinstance(grupoMuscular, str)):
                print("Por favor, ingrese un valor valido.\n")
                grupoMuscular = input("Grupo muscular >> ")
            peso = input("Peso (en kg) >> ")
            while(not isinstance(peso, float)):
                print("Por favor, ingrese un valor valido.\n")
                peso = input("Peso (en kg) >> ")
            reps = input("Nro de repeticiones >> ")
            while (not isinstance(reps, int)):
                print("Por favor, ingrese un valor valido.\n")
                reps = input("Nro de repeticiones >> ")
            sets = input("Nro de series >> ")
            while (not isinstance(sets, int)):
                print("Por favor, ingrese un valor valido.\n")
                sets = input("Nro de sets >> ")

            # Creo la instancia correspondiente al ejercicio
            value = Ejercicio.PesoReps(nombre, grupoMuscular, peso, reps, sets)

        elif tipo == 2:
            pass
        elif tipo == 3:
            pass
        else:
            print("Tipo de ejercicio invalido.")
            return

        # Prompt para key del diccionario, el cual sera la fecha que
        # desee el usuario
        while True:
            fecha = input("Ingrese fecha [AAAA-MM-DD](default=hoy) >> ")
            if (fecha == ""):
                fecha = date.today()
            try:
                key = date.fromisoformat(fecha)
                break
            except:
                print("Por favor, ingrese un valor valido.\n")

        # Chequeo si la key existe ya en el diccionario, de no hacerlo,
        # la inicializo con una lista vacia
        if (key.isoformat() not in self.__entrenamientos):
            self.__entrenamientos[key.isoformat()] = []

        # Agrego el ejercicio a la lista de ejercicios correspondiente a
        # la fecha(key) que indico el usuario, convirtiendo esta en string
        self.__entrenamientos[key.isoformat()].append(value)
