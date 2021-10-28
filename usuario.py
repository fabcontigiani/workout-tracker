class Usuario:
    def __init__(self, nombre: str, contrasena: str, peso: float):
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__peso = peso
        self.__entrenamientos = {}
        self.__haIngresado = False
    
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
        if self.__haIngresado:
            self.__haIngresado = False
        else:
            self.__haIngresado = True