import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, ward, single, complete,average,linkage, fcluster
from scipy.spatial.distance import pdist


# =================================== Parte 1 ===================================


# Se guarda el nombre del archivo csv
filename_eval = "EnergíaMensualHorariaPantasSEN_4_2022.csv"

# Se carga el archivo csv con las fechas en formato datetime como indice
Tabla = pd.read_csv(filename_eval, index_col="Fechas", parse_dates=True)
print(Tabla)

# Se copia el dataframe Tabla y se crea una nueva columna SemanaIdx
Tabla_caso1 = Tabla
Tabla_caso1["SemanaIdx"]=Tabla_caso1.index.isocalendar().week

# Se obtiene todas las semanas del dataframe
indice_semanas=Tabla_caso1.SemanaIdx.unique()

# Se toma el valor de las semanas asignadas en el enunciado
SemanaA = 1
SemanaB = 2

# Se crea la funcion lambda para filtrar 
filtro = lambda x: x['SemanaIdx'] == indice_semanas[SemanaA - 1] or x['SemanaIdx'] == indice_semanas[SemanaB - 1]

# Se aplica el filtro para
Tabla_caso1 = Tabla_caso1[Tabla_caso1.apply(filtro, axis=1, result_type="reduce")]
print(Tabla_caso1)


# =================================== Parte 2 ===================================


# Se copia el dataframe Tabla_caso1 y se elimina la columna SemanaIdx
Tabla_caso2 =  Tabla_caso1
Tabla_caso2 = Tabla_caso2.drop("SemanaIdx", axis=1)

# Se obtienen los kmeans para 3 grupos
kmedias = KMeans(n_clusters=3)
kmedias = kmedias.fit(Tabla_caso2)
print("Labels: ", kmedias.labels_)
centros = np.array(kmedias.cluster_centers_)
print("Centros: ", centros)

# Se crea una lista con colores en formato hexadecimal
colores = ["#3BB143", "#0B6623", "#9DC183", "#708238", "#C7EA46"
           , "#01796F", "#2E8B57", "#043927", "#D0F0C0", "#A9BA9D"]

# Se grafica el resultado
plt.figure(1,figsize=(40,6))

# Centro 1
plt.subplot(1, 3, 1)
y  = centros[:1, :].tolist()[0]
null=plt.bar(range(len(y)), y, 1/1.5, color=colores)
null=plt.xticks(range(Tabla_caso2.shape[1]), Tabla_caso2.columns,rotation=90,fontsize=10)

# Centro 2
plt.subplot(1, 3, 2)
y= centros[1:2, :].tolist()[0]
null=plt.bar(range(len(y)), y, 1/1.5, color=colores)
null=plt.xticks(range(Tabla_caso2.shape[1]), Tabla_caso2.columns,rotation=90,fontsize=10)

# Centro 3
plt.subplot(1, 3, 3)
y = centros[2:3, :].tolist()[0]
null=plt.bar(range(len(y)), y, 1/1.5, color=colores)
null=plt.xticks(range(Tabla_caso2.shape[1]), Tabla_caso2.columns,rotation=90,fontsize=10)
plt.show()

plt.close()


# =================================== Parte 3 ===================================


# Se copia el dataframe Tabla
Tabla_caso3 = Tabla

# Se transpone la tabla
Tabla_caso3 = Tabla_caso3.transpose().drop("SemanaIdx")

# Se obtienen los kmeans para 3 grupos
kmedias = KMeans(n_clusters=3)
kmedias = kmedias.fit(Tabla_caso3)
print("Labels: ", kmedias.labels_)
centros = np.array(kmedias.cluster_centers_)
print("Centros: ", centros)

# Se plotea el resultado
labels = kmedias.labels_
resultados = pd.DataFrame(data=labels, columns=['cluster'])
plt.scatter(resultados.index, resultados['cluster'], c='black')
plt.plot(resultados)
