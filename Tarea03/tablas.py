import pandas as pd
from os import getcwd
from numpy import mean, std



datos = {'nombre': ["Juan Carlos","Francisco","Edudardo","Anabelle","Sonia","Mathew","Jimmy"],
         'carrera': ["Ing. Eléctrica","Educacion Física","Matemáticas","Ing. Mecánica","Derecho","Idiiomas","Ing. Civil"],
         'Edad': [21,20,19,29,22,21,22]
         }


indices = ["e1", "e2", "e3", "e4", "e5", "e6", "e7"]
df = pd.DataFrame(datos, index=indices)
df_por_nombre = df.sort_values(by=['nombre'])
df_por_carrera = df.sort_values(by=['carrera'], ascending=False)


print("Tabla:\n", df, "\n")

print("Tabla ordenada por nombres:\n", df_por_nombre, "\n")

print("Tabla ordenada por carrera:\n", df_por_carrera, "\n")

print("Primeros 3 usando iloc:\n", df.iloc[:3], "\n")

print("Utilizando indice textual\n", df[3:], "\n")

print("Carrera y edad para 2, 3 y 5:\n", df.loc[["e3", "e4", "e6"]][["carrera", "Edad"]])


print("\nExportando DataFrame a excel como \'DataFrame_B90789a.xlsx\' en el directorio actual...")
path = getcwd() + "\DataFrame_B90789.xlsx"
data_a_excel = pd.ExcelWriter(path)
df.to_excel(data_a_excel)
data_a_excel.save()
print("DataFrame exportado a: " + path)






