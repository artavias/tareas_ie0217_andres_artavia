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


    @abstractmethod
    def __AplicarInversion(self):
        pass

    
    @abstractmethod
    def __AsignarOperacion(self):
        pass

 
    def Aplicar(self):
        self.__AplicarInversion()


    def Asignar(self):
        self.__AsignarOperacion()



class BaseIO():

    def Input(self, info=""):
        print(info)
        result = sys.stdin.readline().strip()
        return result



class UsuarioAhorro(UsuarioBase, BaseIO):

    def __init__(self):
        self.__Porcentaje = 1
        self.__MontoAhorro = 0
        super().__init__()
        self.__Captura__()
        

    @property
    def Porcentaje(self):
        return(self.__Porcentaje)


    @Porcentaje.setter
    def Porcentaje(self, porcentaje):
        self.__Porcentaje = porcentaje


    @property
    def MontoAhorro(self):
        return(self.__MontoAhorro)


    def _UsuarioBase__AplicarInversion(self):
        # Se calcula el monto que se transfiere al ahorro
        x = ((self.Porcentaje / 100) * self._UsuarioBase__MontoDisponible)

        # Se debita el monto
        self._UsuarioBase__MontoDisponible -= x
        self.__MontoAhorro += x


    def _UsuarioBase__AsignarOperacion(self):
        pass


    def __Captura__(self):
        self._UsuarioBase__Propietario = str(self.Input("Propietario: "))
        self._UsuarioBase__MontoDisponible = float(self.Input("Monto Disponible: "))
        self.Porcentaje = int(self.Input("Porcentaje de Ahorro: "))



class UsuarioTasaCero(UsuarioBase, BaseIO):

    def __init__(self):
        self.__MontoConsumoMes = 0
        self.__Plazo = 0
        super().__init__()
        self.__Captura__()


    @property
    def MontoConsumoMes(self):
        return(self.MontoConsumoMes)


    @property
    def Plazo(self):
        return(self.Plazo)


    def _UsuarioBase__AplicarInversion(self):
        if(self.__Plazo) != 0:
            #typecasting para evitar errores
            self.__MontoConsumoMes = int(self.__MontoConsumoMes)
            self.__Plazo = int(self.__Plazo)

            self._UsuarioBase__MontoDisponible -= self.__MontoConsumoMes
            self.__Plazo -= 1
            if(self.__Plazo) == 0:
                self.__MontoConsumoMes = 0


    def _UsuarioBase__AsignarOperacion(self):
        if (self.__Plazo) != 0:
            print("El cliente", self._UsuarioBase__Propietario,"tiene una operacion vigente\n")
        else:
            self.__Plazo = int(self.Input("Plazo: "))
            self.__MontoConsumoMes = float(self.Input("Consumo mensual: "))


    def __Captura__(self):
        self._UsuarioBase__Propietario = str(self.Input("Propietario: "))
        self._UsuarioBase__MontoDisponible = float(self.Input("Monto Disponible: "))
        self.__MontoConsumoMes = float(self.Input("Monto de Consumo Mensual: "))
        self.__Plazo = int(self.Input("Plazo: "))
