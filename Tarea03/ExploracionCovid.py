import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def CargarArchivo(nombre = ''):
    '''Estsa funcion se encarga de cargar el
    archivo csv y retorna un dataframe de pandas'''

    data_frame = pd.read_csv(nombre)

    return data_frame



def ChangeIndex(DataFrame, index = ''):
    '''Esta funcion se encarga de transformar el indice del
    dataframe por una columna 'index' '''

    DataFrame.set_index(index, inplace = True)




df = CargarArchivo('time_series_covid19_confirmed_ready.csv')

ChangeIndex(df, 'fechas')

print('Datos para distintos paises del 2020-10-01 al 2020-10-15: \n')
print(df.loc['2020-10-01':'2020-10-15'][['Costa.Rica', 'Uruguay', 'Brazil', 'Spain', 'Italy', 'France']])



#Datos a graficar
CostaRica = list(df['Costa.Rica'])
x = np.linspace(1, len(CostaRica), len(CostaRica))

#Plot para los datos de Costa Rica en las fechas indicadas
plt.plot(x, CostaRica)
plt.title("Casos Reportados de Covid-19 para Costa Rica")
plt.xlabel("Día")
plt.ylabel("Número de Casos Reportados")
plt.show()


#Datos a graficar para españa, italia y francia
Esp = list(df.iloc[252:267]["Spain"])
Ita = list(df.iloc[252:267]["Italy"])
Fra = list(df.iloc[252:267]["France"])


#Plot de españa, italia y francia
x_2 = np.linspace(1, len(Esp), len(Esp))
plt.plot(x_2, Esp, label = 'España', marker = "p")
plt.plot(x_2, Ita, label = 'Italia', marker = "p")
plt.plot(x_2, Fra, label = 'Francia', marker = "p")
plt.title("Casos Reportados de Covid-19")
plt.xlabel("Día")
plt.ylabel("Número de Casos Reportados")
plt.legend()
plt.show()




