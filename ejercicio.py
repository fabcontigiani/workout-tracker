class Ejercicio:
    def __init__(self, nombre:str, grupoMuscular: str):
        self.__nombre = nombre
        self.__grupoMuscular = grupoMuscular
        self.__esCardio = esCardio

class PesoReps(Ejercicio):
    def __init__(self, nombre:str, grupoMuscular: str, esCardio: bool, peso: int, reps: int):
        super().__init__(nombre, grupoMuscular)
        self.__esCardio = False
        self.__peso = peso
        self.__reps = reps
        self.__volumen = peso * reps

class Reps(Ejercicio):
    def __init__(self, nombre:str, grupoMuscular: str, esCardio: bool, pesoCorporal: float, reps: int):
        super().__init__(nombre, grupoMuscular)
        self.__esCardio = False
        self.__pesoCorporal = pesoCorporal
        self.__reps = reps
        self.__volumen = pesoCorporal * reps

class Tiempo(Ejercicio):
    def __init__(self, nombre:str, grupoMuscular: str, tiempo: int):
        self.__esCardio = True
        super().__init__(nombre, grupoMuscular)
        self.__tiempo = tiempo