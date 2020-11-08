from unidad import UnidadFactory
from ejercito import Ejercito
from civilizacion import CivilizacionFactory

if __name__ == "__main__":

    # INICIALIZAR
    civilizacion1 = CivilizacionFactory().create("Chinos")
    ejercito1 = Ejercito(civilizacion1)

    civilizacion2 = CivilizacionFactory().create("Ingleses")
    ejercito2 = Ejercito(civilizacion2)

    # ENTRENAR
    ejercito1.unidades[26].entrenar()
    ejercito1.unidades[27].entrenar()
    ejercito2.unidades[25].entrenar()
    ejercito2.unidades[27].entrenar()
    print("- Monedas Ejercito2 luego de 2 entrenamientos: ", ejercito2.monedas)
    
    # ATACAR
    ejercito1.atacar(ejercito2)
    ejercito1.atacar(ejercito2)
    ejercito2.atacar(ejercito1)
    print("- Monedas Ejercito2 luego de ganar 2 batallas: ", ejercito2.monedas)

    # HISTORIAL
    print("")
    print("- Historial Ejercito 1: ", ejercito1.historial)
    print("- Historial Ejercito 2: ", ejercito2.historial)

    # TRANSFORMAR
    print("")
    print("Unidad antes de transformar: ", ejercito2.unidades[0])
    ejercito2.unidades[0] = ejercito2.unidades[0].transformar()
    print("Unidad luego de transformar: ", ejercito2.unidades[0])
    print("Monedas Ejercito 2 luego de transformar: ", ejercito2.monedas)
