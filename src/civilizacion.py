from abc import ABCMeta, abstractstaticmethod


class ICivilizacion(metaclass=ABCMeta):

    @abstractstaticmethod
    def entrenar():
        pass


class Chinos:

    def __init__(self):
        self.nombre = "Chinos"
        self.piqueros = 2
        self.arqueros = 25
        self.caballeros = 2

    def __str__(self):
        return self.nombre


class Ingleses:

    def __init__(self):
        self.nombre = "Ingleses"
        self.piqueros = 10
        self.arqueros = 10
        self.caballeros = 10

    def __str__(self):
        return self.nombre


class Bizantinos:

    def __init__(self):
        self.nombre = "Bizantinos"
        self.piqueros = 5
        self.arqueros = 8
        self.caballeros = 15


class CivilizacionFactory():

    @staticmethod
    def create(tipo):
        try:
            if tipo == "Chinos":
                return Chinos()
            if tipo == "Ingleses":
                return Ingleses()
            if tipo == "Bizantinos":
                return Bizantinos()
            raise AssertionError("Tipo de civilizacion no válido")
        except AssertionError as e:
            print(e)
