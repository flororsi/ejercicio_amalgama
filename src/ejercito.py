from unidad import UnidadFactory

class Ejercito:

    def __init__(self, civilizacion):
        self.monedas = 1000
        self.civilizacion = civilizacion
        self.historial = []
        self.unidades = []

        for _ in range(civilizacion.piqueros):
            self.unidades.append(UnidadFactory().create("Piquero", self))
        for _ in range(civilizacion.arqueros):
            self.unidades.append(UnidadFactory().create("Arquero", self))
        for _ in range(civilizacion.caballeros):
            self.unidades.append(UnidadFactory().create("Caballero", self))

    def __find_max(self, puntos, i, max_index):
        if puntos > max_index[0][0]:
            if puntos > max_index[1][0]:
                max_index[0][0] = max_index[1][0]
                max_index[0][1] = max_index[1][1]
                max_index[1][0] = puntos
                max_index[1][1] = i
            else:
                max_index[0][0] = puntos
                max_index[0][1] = i
        return max_index

    def __eliminar_unidades(self, max_index, lista_unidades):
        if max_index[0][1] > max_index[1][1]:
            del lista_unidades[max_index[0][1]]
            del lista_unidades[max_index[1][1]]
        else:
            del lista_unidades[max_index[1][1]]
            del lista_unidades[max_index[0][1]]

    def atacar(self, otro):
        puntos_self = 0
        puntos_otro = 0

        max_index_self = [[0, 0], [0, 0]]
        max_index_otro = [[0, 0], [0, 0]]

        for i, unidad in enumerate(self.unidades):
            puntos_self += unidad.puntos
            max_index_self = self.__find_max(unidad.puntos, i, max_index_self)

        for i, unidad in enumerate(otro.unidades):
            puntos_otro += unidad.puntos
            max_index_otro = self.__find_max(unidad.puntos, i, max_index_otro)

        if puntos_self > puntos_otro:
            self.monedas += 100
            self.__eliminar_unidades(max_index_otro, otro.unidades)
            self.historial.append(" \
                Ganó batalla contra ejercito de civilización: {} \
                ".format(otro.civilizacion))
            otro.historial.append(" \
                Perdió battalla contra ejercito de civilización: {} \
                ".format(self.civilizacion))
        elif puntos_self < puntos_otro:
            otro.monedas += 100
            self.__eliminar_unidades(max_index_self, self.unidades)
            otro.historial.append(" \
                Ganó batalla contra ejercito de civilización: {} \
                ".format(self.civilizacion))
            self.historial.append(" \
                Perdió battalla contra ejercito de civilización: {} \
                ".format(otro.civilizacion))
        else:
            del otro.unidades[max_index_otro[0][1]]
            del self.unidades[max_index_self[0][1]]
            self.historial.append(" \
                Empató batalla contra ejercito de civilización: {} \
                ".format(otro.civilizacion))
            otro.historial.append(" \
                Empató battalla contra ejercito de civilización: {} \
                ".format(self.civilizacion))
