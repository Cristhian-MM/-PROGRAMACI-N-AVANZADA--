#Modulo empleado.
import random

class Persona:
    def __init__(self, nombre, apellido, edad, estatura, nivelAcademico, numeroTelefonico):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__estatura = estatura
        self.__ninelAcademico = nivelAcademico
        self.__numeroTelefonico = numeroTelefonico

    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getEdad(self):
        return self.__edad
    def getEstatura(self):
        return self.__estatura
    def getNivelAcademico(self):
        return self.__ninelAcademico
    def getNumeroTelefonico(self):
        return self.__numeroTelefonico

    def Presentarce(self):
        print('\nHola, soy',self.__nombre,self.__apellido,'y tengo',self.__edad,'años. Es un gusto conocerte.')

    def Vestir(self, prenda1, prenda2, accesorio):
        print('\nVestimenta de', self.__nombre,'para hoy.')
        print('*', prenda1)
        print('*', prenda2)
        print('*', accesorio)

    def Comer(self, alimento, bebida):
        print(' ')
        print(self.__nombre, 'comera:')
        print('*', alimento)
        print('*', bebida)

    def Dormir(self, horas):
        print(' ')
        print(self.__nombre,'dormira por',horas,'hrs.')
        if horas < 8:
            print('-Es menos del tiempo recomendado :(')
        elif horas >= 8:
            print('-Ese es el tiempo recomendado :)')

    def AccionAleatoria(self):
        print(' ')
        AA = random.randint(1,3)
        if AA == 1:
            print(self.__nombre, 'esta viendo TV.')
        elif AA == 2:
            print(self.__nombre, 'esta jugando videojuegos.')
        elif AA == 3:
            print(self.__nombre, 'esta leyendo un libro.')
