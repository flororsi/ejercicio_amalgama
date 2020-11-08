from abc import ABCMeta, abstractstaticmethod


class Unidad(metaclass=ABCMeta):

    def __init__(self):
        self.nombre = "Unidad"
        self.puntos = 0


class Piquero(Unidad):

    def __init__(self, ejercito):
        self.nombre = "Piquero"
        self.puntos = 5
        self.ejercito = ejercito

    def __str__(self):
        return "{0} puntos: {1} ".format(self.nombre, self.puntos)

    def entrenar(self):
        self.puntos += 3
        self.ejercito.monedas -= 10
        return self.puntos

    def transformar(self):
        if self.ejercito.monedas >= 30:
            self = UnidadFactory().create("Arquero", self.ejercito)
            self.ejercito.monedas -= 30
        return self


class Arquero(Unidad):

    def __init__(self, ejercito):
        self.nombre = "Arquero"
        self.puntos = 10
        self.ejercito = ejercito

    def __str__(self):
        return "{0} puntos: {1} ".format(self.nombre, self.puntos)

    def entrenar(self):
        self.puntos += 7
        self.ejercito.monedas -= 20
        return self.puntos

    def transformar(self):
        if self.ejercito.monedas >= 40:
            self = UnidadFactory().create("Caballero", self.ejercito)
            self.ejercito.monedas -= 40
        return self


class Caballero(Unidad):

    def __init__(self, ejercito):
        self.nombre = "Caballero"
        self.puntos = 20
        self.ejercito = ejercito

    def __str__(self):
        return "{0} puntos: {1} ".format(self.nombre, self.puntos)

    def entrenar(self):
        self.puntos += 10
        self.ejercito.monedas -= 30
        return self.puntos

    def transformar(self):
        raise AssertionError("Caballero no se puede transformar.")


class UnidadFactory():

    @staticmethod
    def create(tipo, ejercito):
        try:
            if tipo == "Piquero":
                return Piquero(ejercito)
            if tipo == "Arquero":
                return Arquero(ejercito)
            if tipo == "Caballero":
                return Caballero(ejercito)
            raise AssertionError("Tipo de unidad no válido")
        except AssertionError as e:
            print(e)
