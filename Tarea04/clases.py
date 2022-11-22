import sys
from abc import ABCMeta, abstractmethod

class UsuarioBase(metaclass=ABCMeta):

    def __init__(self):
        self.__Propietario = ''
        self.__MontoDisponible = 0

    @property
    def Propietario(self):
        return (self.__Propietario)

    @Propietario.setter
    def Propietario(self, Propietario):
        self.__Propietario = Propietario
    

    @property
    def MontoDisponible(self):
        return (self.__MontoDisponible)

    @MontoDisponible.setter
    def MontoDisponible(self, monto):
        self.__MontoDisponible = monto

    def __AplicarInversion(self):
        pass
    
    def __AsignarOperacion(self):
        pass
 
    def Aplicar(self):
        return self.__AplicarInversion()

    def Asignar(self):
        return self.__AsignarOperacion()



class UsuarioAhorro(UsuarioBase):

    def __init__(self):

        self.__Porcentaje = 1
        self.__MontoAhorro = 0
        UsuarioBase.__init__(self)
        
    @property
    def Porcentaje(self):
        return(self.__Porcentaje)

    @Porcentaje.setter
    def Porcentaje(self, porcentaje):
        self.__Porcentaje = porcentaje

    @property
    def MontoAhorro(self):
        return(self.__MontoAhorro)

    @property
    def __AplicarInversion(self):

        # Se calcula el monto que se transfiere al ahorro
        x = ((self.__Porcentaje(self) / 100) * self.__MontoDisponible)

        # Se debita el monto
        self.__MontoDisponible -= x
        self.__MontoAhorro(x)

        return self.__MontoAhorro(x)

    def __AsignarOperacion(self):
        pass

chito = UsuarioAhorro()
chito.__MontoDisponible = 150000
chito.__Porcentaje = 20
chito.Aplicar()
print(chito)
print(chito.__MontoDisponible)