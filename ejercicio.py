from abc import ABC, abstractmethod

class Ejercicio(ABC):
    def __init__(self, nombre: str):
        self.__nombre = nombre

    def __str__(self):
        raise NotImplementedError("Cada subclase tendra uno diferente")

    @property
    def nombre(self):
        return self.__nombre

    @abstractmethod
    def volumen(self):
        raise NotImplementedError("Subclase implementa esto.")


class PesoReps(Ejercicio):
    def __init__(self, nombre: str, peso: int, reps: int, sets: int):
        super().__init__(nombre)
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

    def volumen(self):
        # El volumen de entrenamiento sera:
        return self.peso * self.reps * self.sets


class Reps(Ejercicio):
    def __init__(self, nombre: str, pesoCorporal: float, reps: int, sets: int):
        super().__init__(nombre)
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

    def volumen(self):
        # Se considerara dos tercios del peso corporal del usuario a la hora
        # del calculo de volumen de entrenamiento
        return (2/3) * self.pesoCorporal * self.reps * self.reps


class Tiempo(Ejercicio):
    def __init__(self, nombre: str, tiempo: int):
        super().__init__(nombre)
        self.__tiempo = tiempo

    def __str__(self):
        return f"{self.nombre} | {self.tiempo} mins"

    @property
    def tiempo(self):
        return self.__tiempo

    def volumen(self):
        # Ejercicios de este tipo no se consideraran para el calculo del
        # volumen de entrenamiento
        return 0
