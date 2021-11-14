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

class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, estatura, nivelAcademico, numeroTelefonico, empresa, puesto, sueldo):
        super().__init__(nombre, apellido, edad, estatura, nivelAcademico, numeroTelefonico)
        self.__empresa = empresa
        self.__puesto = puesto
        self.__sueldo = sueldo

    def getEmpresa(self):
        return self.__empresa
    def getPuesto(self):
        return self.__puesto
    def getSueldo(self):
        return self.__sueldo

    def Curriculum(self):
        print(' ')
        print('|--------------------------------|')
        print('      ',Persona.getNombre(self),Persona.getApellido(self))
        print('|--------------------------------|')
        print('          --Contacto--')
        print(' Telefono: ',Persona.getNumeroTelefonico(self))
        print('     --Informacion personal--')
        print(' Edad: ',Persona.getEdad(self))
        print(' Estatura: ',Persona.getEstatura(self))
        print('    --Informacion Educativa--')
        print(' Nivel academico: ',Persona.getNivelAcademico(self))
        print('      --Historial Laboral--')
        print(' Empresa: ',Empleado.getEmpresa(self))
        print(' Puesto: ',Empleado.getPuesto(self))
        print('|--------------------------------|')

class Gerente(Empleado):
    _puesto = 'Gerente'
    def __init__(self, nombre, apellido, edad, estatura, nivelAcademico, numeroTelefonico, empresa, sueldo):
        super().__init__(nombre, apellido, edad, estatura, nivelAcademico, numeroTelefonico, empresa, self._puesto, sueldo)

    def Entrevistar(self, gerente, persona):
        print('\n--Entrevista de trabajo--')
        print('**Entrevistador:')
        print('Buen dia',persona.getNombre(), ',soy',gerente.getNombre(),'y sere la persona responsable de realizar la entrevista.')
        print('La empresa',gerente.getEmpresa(),'le agradece su interes por formar parte de nuestro equipo de trabajo.')
        print('**Solicitante:')
        print('Un placer',gerente.getNombre(),', gracias por considerar mi solicitud')
        print('**Entrevistador:')
        print('Bien, comencemos con la entrevista.')
        print('¿Cual es su nombre completo?')
        print('**Solicitante:')
        print(persona.getNombre(),persona.getApellido())
        print('**Entrevistador:')
        print('¿Cual es su edad?')
        print('**Solicitante:')
        print(persona.getEdad(),'años')
        print('**Entrevistador:')
        print('¿Cual es su maximo nivel academico?')
        print('**Solicitante:')
        print(persona.getNivelAcademico())
        print('**Entrevistador:')
        print('¿Cuenta con algun numero telefonico para futuro contacto?')
        print('**Solicitante:')
        print(persona.getNumeroTelefonico())
        print('**Entrevistador:')
        print('Eso es todo por el momento, en un futuro se le dara a conocer la resolucion de su solicitud.')

    def Contratar(self, gerente, persona):
        print('\n--Resolucion de Solicitud de Empleo--')
        Decision = random.randint(1, 2)
        if Decision == 1:
            print('Aspirante:', persona.getNombre(), persona.getApellido())
            print('Enhorabuena',persona.getNombre(),'su solicitud de empleo ha sido aprovada.')
            print('Bienvenido a la empresa', gerente.getEmpresa())
        elif Decision == 2:
            print('Aspirante:',persona.getNombre(),persona.getApellido())
            print('Sentimos informarles que su solicitud de empleo ha sido rechazada.')

    def TrabajoAleatorio(self):
        print(' ')
        TA = random.randint(1, 3)
        if TA == 1:
            print('El Gerente',Persona.getNombre(self), 'esta planificando las actividaes de la empresa.')
        elif TA == 2:
            print('El Gerente',Persona.getNombre(self), 'esta organizando los recursos de la empresa.')
        elif TA == 3:
            print('El Gerente',Persona.getNombre(self), 'esta planificando los objetivos de la empresa.')
