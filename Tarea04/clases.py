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



class UsuarioPagosServicios(UsuarioBase, BaseIO):

    def __init__(self):
        self.Servicios = []
        super().__init__()
        self.__Captura__()


    def InsertarServicio(self):
        servicio = ServicioPublico()
        self.Servicios.append(servicio)


    def EliminarServicio(self, servicio):
        for serv in self.Servicios:
            if serv.EmpresaServicioPublico == servicio:
                self.Servicios.remove(serv)


    def VisualizarServicios(self):
        for Servicio in self.Servicios:
            print("%s: %.2f" %(Servicio.EmpresaServicioPublico, Servicio.CargoAutomatico))


    def _UsuarioBase__AplicarInversion(self):
        for Servicio in self.Servicios:
            if (self._UsuarioBase__MontoDisponible - Servicio.CargoAutomatico) >= 0:
                self._UsuarioBase__MontoDisponible -= Servicio.CargoAutomatico
                Servicio.CargoAutomatico = 0
            else:
                print("Fondos insuficientes para pagar el servicio: %s\n"
                    %(Servicio.EmpresaServicioPublico)
                )


    def _UsuarioBase__AsignarOperacion(self):
        for Servicio in self.Servicios:
            if Servicio.CargoAutomatico != 0:
                print("Operacion vigente de usuario '%s' para servicio: %s\n"
                    %(self.Propietario, Servicio.EmpresaServicioPublico)
                )
            else:
                Servicio.CargoAutomatico = float(self.Input("Cargo automatico para %s: \n" %(Servicio.EmpresaServicioPublico)))

    
    def __Captura__(self):
        self._UsuarioBase__Propietario = str(self.Input("Propietario: "))
        self._UsuarioBase__MontoDisponible = float(self.Input("Monto Disponible: "))
        n_servicios = int(self.Input("Cantidad de servicios: "))
        for i in range(n_servicios):
            self.InsertarServicio()



class ServicioPublico(BaseIO):

    def __init__(self):
        self.EmpresaServicioPublico = ''
        self.CargoAutomatico = 0
        self.__Captura__()

    def __Captura__(self):
        self.EmpresaServicioPublico = str(self.Input("Servicio Publico: "))
        self.CargoAutomatico = float(self.Input("Cargo automatico: "))

        
        
class agenciabancaria(BaseIO):

    def __init__(self):
        self.UsuariosAhorro = []
        self.UsuariosTasaCero = []
        self.UsuariosPagosServicios = []
        self.Opciones()


    def Opciones(self):

        print("-------------------------------------")
        print("1) Agregar UsuarioAhorro")
        print("2) Agregar UsuarioTasaCero")
        print("3) Agregar UsuariosPagosServicios")
        print("4) Mostrar lista de usuarios")
        print("5) Asignar Fondos")
        print("6) Asignar Operaciones")
        print("7) Procesar Inversiones")
        print("8) Final")
        print("-------------------------------------")
        opcion = int(self.Input("Ingrese una opcion: "))

        if opcion == 1:
            print("Agregando UsuarioAhorro\n")
            self.UsuariosAhorro.append(UsuarioAhorro())

            self.Opciones()

        elif opcion == 2:
            print("Agregando UsuarioTasaCero\n")
            self.UsuariosTasaCero.append(UsuarioTasaCero())

            self.Opciones()

        elif opcion == 3:
            print("Agregando UsuarioPagosServicios\n")
            self.UsuariosPagosServicios.append(UsuarioPagosServicios())
            print("a) Ingresar servicio \nb) Mostrar servicios\nc) Eliminar servicio.\nd) Regresar.\n")
            opcion = str(self.Input("Ingrese una opcion: "))

            while opcion != "d":
                if opcion == "a":
                    self.UsuariosPagosServicios[-1].InsertarServicio()
                    print("\na) Ingresar servicio \nb) Mostrar servicios\nc) Eliminar servicio.\nd) Regresar.\n")
                    opcion = str(self.Input("Ingrese una opcion: "))

                elif opcion == "b":
                    self.UsuariosPagosServicios[-1].VisualizarServicios()
                    print("\na) Ingresar servicio \nb) Mostrar servicios\nc) Eliminar servicio.\nd) Regresar.\n")
                    opcion = str(self.Input("Ingrese una opcion: "))

                elif opcion == "c":
                    servicio = str(self.Input("Servicio a remover: "))
                    self.UsuariosPagosServicios[-1].EliminarServicio(servicio)
                    print("\na) Ingresar servicio \nb) Mostrar servicios\nc) Eliminar servicio.\nd) Regresar.\n")
                    opcion = str(self.Input("Ingrese una opcion: "))

            self.Opciones()
