from abc import ABC, abstractmethod

class Ejercicio(ABC):
    def __init__(self, nombre: str, grupoMuscular: str):
        self.__nombre = nombre
        self.__grupoMuscular = grupoMuscular
        self.__esCardio = None

    @property
    def nombre(self):
        return self.__nombre

    @property
    def grupoMuscular(self):
        return self.__grupoMuscular

    @property
    def esCardio(self):
        return self.__esCardio

    @abstractmethod
    def volumen(self):
        pass


class PesoReps(Ejercicio):
    def __init__(self, nombre: str, grupoMuscular: str, esCardio: bool, peso: int, reps: int, sets: int):
        super().__init__(nombre, grupoMuscular)
        self.__esCardio = False
        self.__peso = peso
        self.__reps = reps
        self.__sets = sets

    @property
    def peso(self):
        return self.__peso

    @property
    def reps(self):
        return self.__reps

    @property
    def sets(self):
        return self.__sets


class Reps(Ejercicio):
    def __init__(self, nombre: str, grupoMuscular: str, esCardio: bool, pesoCorporal: float, reps: int, sets: int):
        super().__init__(nombre, grupoMuscular)
        self.__esCardio = False
        self.__pesoCorporal = pesoCorporal
        self.__reps = reps
        self.__sets = sets

    @property
    def pesoCorporal(self):
        return self.__pesoCorporal

    @property
    def reps(self):
        return self.__reps

    @property
    def sets(self):
        return self.__sets

class Tiempo(Ejercicio):
    def __init__(self, nombre: str, grupoMuscular: str, tiempo: int):
        super().__init__(nombre, grupoMuscular)
        self.__esCardio = True
        self.__tiempo = tiempo

    @property
    def tiempo(self):
        return self.__tiempo
