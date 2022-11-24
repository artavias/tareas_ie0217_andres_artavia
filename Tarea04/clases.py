import sys
from abc import ABCMeta, abstractmethod

"""La siguiente clase se encarga de ser el metaclass
de los usuarios, los metodos abstractos se deben implementar
en las clases hijas y se accesan mediante los metodos
Aplicar() y  Asignar()"""
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


"""La siguiente clase se utiliza para tomar el
input y formatearlo"""
class BaseIO():

    def Input(self, info=""):
        print(info)
        result = sys.stdin.readline().strip()
        return result


"""La clase UsuarioAhorro es hija de la clase
UsuarioBase, implementa el metodo AplicarInversion()
el cual descuenta del monto disponible el monto ahorro
y lo suma a la variable MontoAhorro. El metodo
AasignarOperacion() se define pero no se utiliza"""
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


"""El UsuarioTasaCero tambien es clase hija de 
UsuarioBase. El metodo AplicarInversion() se encarga
de restar al monto disponible el MontoConsumoMes y
restarle 1 al plazo. El metodo AsignarOperacion()
permite asignar un plazo y un MontoConsumoMes si el
Plazo es igual a 0."""
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
            self.__Plazo = int(self.Input("Plazo para usuario %s: " %self._UsuarioBase__Propietario"))
            self.__MontoConsumoMes = float(self.Input("Consumo mensual: "))


    def __Captura__(self):
        self._UsuarioBase__Propietario = str(self.Input("Propietario: "))
        self._UsuarioBase__MontoDisponible = float(self.Input("Monto Disponible: "))
        self.__MontoConsumoMes = float(self.Input("Monto de Consumo Mensual: "))
        self.__Plazo = int(self.Input("Plazo: "))



"""El UsuarioPagosServicios es hija de UsuarioBase.
Se pueden insertar servicios a pagar con el metodo
InsertarServicio(). Eliminarlos con EliminarServicio()
o visualizarlos con VisualizarServicios(). El metodo
AplicarInvsersion() se encarga de restar el el cargo 
automatico al monto disponible si los fondos son
suficientes. AsignarOperacion() se encarga de darle
un nuevo valor al cargo automatico para cada servicio
si no hay una operacion vigente."""
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


"""Clase de servicio publico para manejar
los servicios de forma mas eficiente en la
clase UsuarioPagosServicios, al instanciarse
pide al usuario el nombre del servicio y el
cargo automatico"""
class ServicioPublico(BaseIO):

    def __init__(self):
        self.EmpresaServicioPublico = ''
        self.CargoAutomatico = 0
        self.__Captura__()

    def __Captura__(self):
        self.EmpresaServicioPublico = str(self.Input("Servicio Publico: "))
        self.CargoAutomatico = float(self.Input("Cargo automatico: "))


"""La clase agenciabancaria se encarga de darle
opciones al usuario, crear las clases de usuarios
que se soliciten, y Aplicar o Asignar operaciones
para todos los usuarios, listar los usuarios y
asignar fondos a cada usuario.
Al instanciarse el programa sigue corriendo al menos
que se selecciones la opcion '8' o algo diferente a
los numeros del 1-7"""
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

        elif opcion == 4:
            print("Usuarios Ahorro:\n")
            for usuario in self.UsuariosAhorro:
                print("Usuario: %s" %usuario.Propietario)
                print("Monto Disponible: %.2f" %usuario.MontoDisponible)
                print("Porcentaje de Ahorro: %i" %usuario.Porcentaje)
                print("Monto de Ahorro: %i\n" %usuario.MontoAhorro)

            print("Usuarios TasaCero:\n")
            for usuario in self.UsuariosTasaCero:
                print("Usuario: %s" %usuario.Propietario)
                print("Monto Disponible: %.2f" %usuario.MontoDisponible)
                print("Monto de Consumo Mensual: %.2f" %usuario._UsuarioTasaCero__MontoConsumoMes)
                print("Plazo: %i\n" %usuario._UsuarioTasaCero__Plazo)

            print("Usuarios PagosServicios:\n")
            for usuario in self.UsuariosPagosServicios:
                print("Usuario: %s" %usuario.Propietario)
                print("Monto Disponible: %.2f" %usuario.MontoDisponible)
                usuario.VisualizarServicios()
                print("\n")

            self.Opciones()

        elif opcion == 5:
            print("Seleccione un usuario: \n")
            for usuario in self.UsuariosAhorro:
                print("Usuario: %s" %usuario.Propietario)
            for usuario in self.UsuariosTasaCero:
                print("Usuario: %s" %usuario.Propietario)
            for usuario in self.UsuariosPagosServicios:
                print("Usuario: %s" %usuario.Propietario)

            usuario_a_modificar = str(self.Input())

            for usuario in self.UsuariosAhorro:
                if usuario.Propietario == usuario_a_modificar:
                    usuario.MontoDisponible = float(self.Input("Monto Disponible: "))
            for usuario in self.UsuariosTasaCero:
                if usuario.Propietario == usuario_a_modificar:
                    usuario.MontoDisponible = float(self.Input("Monto Disponible: "))
            for usuario in self.UsuariosPagosServicios:
                if usuario.Propietario == usuario_a_modificar:
                    usuario.MontoDisponible = float(self.Input("Monto Disponible: "))

            self.Opciones()

        elif opcion == 6:
            for usuario in self.UsuariosAhorro:
                usuario.Asignar()
            for usuario in self.UsuariosTasaCero:
                usuario.Asignar()
            for usuario in self.UsuariosPagosServicios:
                usuario.Asignar()

            self.Opciones()

        elif opcion == 7:
            for usuario in self.UsuariosAhorro:
                usuario.Aplicar()
            for usuario in self.UsuariosTasaCero:
                usuario.Aplicar()
            for usuario in self.UsuariosPagosServicios:
                usuario.Aplicar()
            
            self.Opciones()

        elif opcion == 8:
            quit()

Banco = agenciabancaria()
