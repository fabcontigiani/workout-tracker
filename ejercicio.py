from abc import ABC, abstractmethod

class Ejercicio(ABC):
    def __init__(self, nombre: str, esCardio: bool):
        self.__nombre = nombre
        self.__esCardio = esCardio

    def __str__(self):
        raise NotImplementedError()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def esCardio(self):
        return self.__esCardio

    # @abstractmethod
    # def volumen(self):
    #     pass


class PesoReps(Ejercicio):
    def __init__(self, nombre: str, peso: int, reps: int, sets: int):
        super().__init__(nombre, False)
        self.__peso = peso
        self.__reps = reps
        self.__sets = sets

    def __str__(self):
        return f"{self.nombre} | {self.peso} kgs | {self.reps} reps | {self.sets} sets"

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
    def __init__(self, nombre: str, pesoCorporal: float, reps: int, sets: int):
        super().__init__(nombre, False)
        self.__pesoCorporal = pesoCorporal
        self.__reps = reps
        self.__sets = sets

    def __str__(self):
        return f"{self.nombre} | {self.reps} reps | {self.sets} sets"

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
    def __init__(self, nombre: str, tiempo: int, esCardio: bool):
        super().__init__(nombre, esCardio)
        self.__tiempo = tiempo

    def __str__(self):
        return f"{self.nombre} | {self.tiempo} mins"

    @property
    def tiempo(self):
        return self.__tiempo
