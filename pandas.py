# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:25:41 2020

@author: JOliv
"""

#PANDAS

#Instalacion de Pandas
#!pip install pandas
#!pip install numpy

import pandas as pd
import numpy as np

"""
NOTA IMPORTANTE: si alguna linea no hace nada aparentemente, correr con f9
"""
#%% 
"""
SERIES

Las series son arreglos de una sola dimension, y se pueden crea a partir de 
objetos como tuplas, listas, diccionarios o arrays.

La caracteristica fundamental de las series es que las observaciones las acomoda
con un indice o un vector de posicion.
"""
serie1 = pd.Series(np.random.rand(8))
print(serie1)
#Construye un cuadro con 8 numeros aleatorios indexados 

serie2 = pd.Series(np.random.rand(8), name = 'mi primer serie')
print(serie2)
#Le damos un nombre a la columna

#%% Acceder a los indices
print(serie1[5])
print(serie2[7])

#Se puede modificar la numeracion de los indices para mayor comodidad
serie2 = pd.Series(np.random.rand(8), index=range(1,9), name='mi segunda serie')
print(serie2)
#De esta forma los indices ya no comienzan desde 0 sino desde 1

#Se tiene total control sobre los indices 
serie3 = pd.Series(np.random.rand(5), index = [3,6,2,8,5])
print(serie3)
print(serie3[2])

#De hecho podemos hacer que los indices sean strings
serie4 = pd.Series(np.random.rand(5), index = ['a', 'b', 'c', 'd', 'e'])
print(serie4)
print(serie4['d'])

#Creando un serie a partir de un diccionario
diccionario = {'Nombre':['Jorge', 'Oliver'], 'Apellido' :['Perez', 'Espinoza']}
seriedic = pd.Series(diccionario)
print(seriedic)

#La estructura de las series son la base de los Dataframes 

#%%
"""
DATAFRAMES

Los dataframes son una estructura nativa de R, muy util para el analisis de datos
Una de sus caracteristicas más importantes y utiles es que no es necesario que 
sus columnas sean del mismo type. 

A las columnas se les llama campos
A las filas se les llama registros

Otra caracteristica fundamental es que todos los campos deben tener el mismo
numero de registros.

Se puede contruir df a partir de dict, tuples, arrays .

Por default, tanto el nombre de los campos como los registros python los construye
con valores numericos empezando desde el 0

De manera técnica, cada columna de un df es una serie
"""
pd.DataFrame(data = [(0,1,2),(1,2,3),(2,3,4),(3,4,5)])

#Construyendo un df a partir de un dict
estudiantes = {'Nombre':['Pedro', 'Pablo', 'Hugo','Paco','Luis','Juan'], 
               'Apellido':['Lopez','Rodriguez','Ramirez','Perez','Oca', np.nan],
               'Matricula':['123456','629834','789012','345678','901234','567890'],
               'Edad':[20,45,np.nan,23,10,18]
               }
print(estudiantes)

df = pd.DataFrame(data = estudiantes, index= range(1,7))
print(df)

#Ademas podemos darle un nombre a cada registro en lugar de un numero

registro = ["Persona1", 'Persona2','Persona3','Persona4','Persona5','Persona6']
df = pd.DataFrame(data = estudiantes, index= registro)
print(df)

#%%
#Construyendo un df a partir de una matriz 

matriz = np.arange(9).reshape(3,3)
df1 = pd.DataFrame(matriz) 
print(df1)

#Reenombrando columnas e indices
df1 = pd.DataFrame(matriz, index = ['uno','dos','tres'], columns=('a','b','c')) 
print(df1)

"""En el caso de diccionarios no se puede modificar el nombre de las colmnas, 
pues ya toma el nombre asignado en el diccionario, por lo que se debe modificar 
directamente el diccionario"""

#%% Construyendo un df a partir de una lista de listas 
df3 = pd.DataFrame([['Hugo','Molina',123,20],['Mario','Lopez',234,18],
              ['Pablo','Carmona',345,23],['Luis','Oca',456]],
             index = ['Alumn1','Alumn2','Alumn3','Alumn4'],
             columns=['Nombre','Apellido','Matricula','Edad'])
print(df3)

#%%ACCEDIENDO A LOS ELEMENTOS DE UN DF

#Accediendo a una columna
print(df3['Nombre'])
print(df3['Edad'])

#Accediendo a más de una columna
print(df3[['Nombre', 'Matricula']])

#Accediendo a registros
df3.loc[['Alumn1','Alumn3']]

#Accediendo a un registro mediante su indice
df3.iloc[0]
df3.iloc[1]

#Accediendo a valores puntuales
print(df3.loc[['Alumn2']] [['Matricula']])
print(df3.loc[['Alumn1','Alumn4']] [['Matricula','Edad']])

#%% OPERACIONES con DF
#Creando un nuevo campo a partir de otros ya existentes
df3['NombreCompleto'] = df3['Nombre'] + " " + df3["Apellido"]
print(df3)

#%% Eliminar columnas
df3.drop("NombreCompleto", axis=1, inplace=False)
print(df3)

df3.drop("NombreCompleto", axis=1, inplace= True)
print(df3)

"""
axis indica donde debe buscar NombreCompleto:
    0 = filas
    1 = columnas
inplace indica si se desea modificar el df original o no:
    False = no modifica el original
    True = si modifica el original
Por default el inplace está en False para no perder los valores
"""
#%% Indexar numericamente los registros

df3.reset_index(inplace = True)
print(df3)

"""
Lo que hace es indexar de nuevo el df desde 0, sin embargo no borra el nombre
de los registros anteriores, sino que los convierte en una nueva columna.
Recordar la funcion inplace
"""

#Accediendo a valores puntuales despues del reset_index
df3.loc[[0,3],['Nombre','Matricula']]

#%%FILTROS
"""
Muy util a la hora de trabajar con grandes bases de datos 
"""
df3['Edad'] > 20
#Nos devuelve un bool, sin embargo parece más util la sig linea

df3[df3['Edad'] > 20]
#Este si nos devuelve el registro completo

#Si solo necesitamos ciertos campos podemos utilizar lo siguiente
df3[df3['Edad'] >20 ][['Nombre','Matricula','Edad']]
print(df3)

#%%Cambiar el nombre de las columnas
print(df3)
df3.columns = ['Campo1','Campo2','Campo3','Campo4', 'Campo5']
print(df3)

#%%Utilizar un campo como ID 
#En nuestro ejemplo el unico campo que nos sirve como ID es la matricula
df3.index = df3['Campo4']
print(df3)

#%%Agregar un registro
#Separar los datos
NuevoRegistro = "Alumn5, Helena, Gonzales, 888, 22"
NuevoRegistro.split(",")

df3.loc[888]=NuevoRegistro.split(",")
print(df3)

"""
split actua como un separador, en este ejemplo separa todo el str en partes cuando 
encuentra una coma y cada parte es el valor de cada una de las columnas

Cabe resaltar que tanto la edad como la Matricula son datos str por lo que
más adelante se pueden complicar algunas operaciones.Son str porque asi agregamos
el ultimo registro. Más adelante se verá como corregirlo 
"""

print(df3.iloc[-1])

#%%VISUALIZANDO df
#Encabezado
df3.head() #Por default muestra los primeros 5 registros
df3.head(3)

#Tambien puede mostrar los ultimos
df3.tail(2)
df3.head() #Por default muestra los ultimos 5

#%% Resolucion de problemas comunes con los dataframe

#MODIFICANDO EL type

#Si quisieramos calcular el promedio de la edad
df3['Campo5'].mean()
#Marca un error porque la edad del ultimo registo es un str y no un float


"""
ahora si, si queremos hacer operaciones con la edad debemos modificar el tipo
de dato 
"""
#Verificamos que evidentemente es un str
type(df3.iloc[4]['Campo5'])

#Modificando el tipo de dato
df3['Campo5'] = pd.to_numeric(df3['Campo5'], downcast='float')

#Comprobamos se haya cambiado
type(df3.iloc[4]['Campo5'])

#Entonces ahora si podemos calcular la media de la edad 
df3['Campo5'].mean()

#%% Espacios de más a la hora de agregar registros
df3['Campo5'].value_counts()
#Muestra la frecuencia de las edades

#Agregamos un nuevo registro (Esta es una forma más comun de agregar registros)
df3.loc[777] = ['Alumn6','Jose','Lopez','777',30]
print(df3)
df3['Campo3'].value_counts()

#Observar que Gonzales tiene una sangría distinta, eso se debe a que lo agregamos
#Con ese espacio de más, para eso debemos volver desde que agregamos el registro y eliminarlo

#%% SUSTITUCION DE NaN

#Ordenar el df por valores
print(df3)
df3.sort_values(by = 'Campo5', inplace = True, ascending = False)
print(df3)

"""
En ocaciones nuestras bases de datos contienen varios NaN con los que se complica 
trabajar, cuando es un campo numerico es comun es sustituirlos por el valor 
promedio del campo
"""
#Calculamos y guardamos el valor promedio de la edad
edadMedia = df3['Campo5'].mean()
float(edadMedia)

#Sustituimos
df3['Campo5'].fillna(float(edadMedia), inplace = True)
print(df3)

#%%ORDENAR DF
#Si ahora quisieramos ordenar el df por indices
df3.sort_index(ascending = True, inplace = True)
print(df3)

#Ordenando el df con dos parametros
df3.sort_values(by = ['Campo3', 'Campo5'], ascending= [True,False], inplace= True)
print(df3)
#Ordena primero por campo3, si hay repetidos entonces toma el segundo criterio de ordenamiento

#%% Metodos varios
#Filtrar los Registros de los estudiantes que se apelliden Lopez
df3[df3['Campo3'] == 'Lopez']

#Convertir a mayuscular los valores de una columna
df3['Campo2'] = df3['Campo2'].str.upper()
print(df3)

#Mostrar la longitud de un determinado campo
df3['Campo3'].str.len()

#%%AÑADIR REGISTROS Y COLUMNAS

#Agregamos un nuevo registro
df3.loc[999] = ['Alumn7', 'Luisa', 'Gonzales', '999', 23]

#Agregamos un nuevo campo y sus respectivos valores 
df3['Estado']= ['Activo', 'Baja', 'Baja','Graduado', 'Activo', 'Activo', 'Baja']

print(df3)

#%% COLUMNAS DUMMIES
"""
Las variables dummies son variables categoricas y toman valores unicamente 0 y 1
0 = No cumple con la condicion
1 = Cumple con la condicion 
"""
#Creamos la columna dummie
pd.get_dummies(df3['Estado'])

#POdemos PEGAR o agregarla a nuestro Dataframe
Frame = pd.concat([df3,pd.get_dummies(df3['Estado'])], axis=1)
print(Frame)

#Agregamos una nueva colmna a nuestro df
Frame['Fac'] = [4,3,1,4,5,1,8]
Frame['Sexo']= ['0','1','1','1','1','1','0']
print(Frame)
#%%
#Agrupando
"""
No me queda claro la interpretacion del Factor o Fac, sin embargo, se sabe que es 
de vital importancia para la Ciencia de Datos
"""
Frame.groupby('Estado')['Fac'].sum()

Frame.groupby(['Estado', 'Sexo'])['Fac'].sum()

Frame.groupby(['Estado', 'Sexo'])['Fac'].sum()['Activo', '0']

#Resumen
Frame.describe()
Frame['Sexo'].describe()

Frame.info()

#%%
#LECTURA Y ESCRITURA DE CSV
"""
Un archivo CSV (Comma separated values)es un tipo de documento en forma de 
tabla cuyos valores estan separados por comas (,) como su nombre lo indica.
Pueden contener valores de diferente type.   
"""
#Lectura
ejemplo = pd.read_csv("https://raw.githubusercontent.com/AAProgramand/datasets/master/degrees.csv")
ejemplo.head()

#Escritura
#creamos un df 
df = pd.DataFrame({'Nombre':['a','b','c'], 'Número': [1,2,3]})

#Convertimos nuestro df en un csv
df.to_csv("C:/Users/JOliv/OneDrive/Documentos/Python/SciData/DS/primercsv.csv",index=True,header=True,encoding='latin')
#Aqui se agrega la direccion y el nombre con que guardaremos nuestro csv

"""
index es un booleano para saber si imprimir o no los índices
header es un booleano para saber si imprimir o no los nombres de los campos
encoding es un string que permite usar la codificación del "idioma" que se usaré. 
Por default es "UTF-8"; se recomienda tenerlo en "latin" para poder usar acentos.
"""

#%%
#CONCATENACION

df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']})
print(df1)


df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
                    'B':['B4','B5','B6','B7'],
                    'C':['C4','C5','C6','C7'],
                    'D':['D4','D5','D6','D7']})
print(df2)

df3 = pd.DataFrame({'A':['A8','A9','A10','A11','A12'],
                    'B':['B8','B9','B10','B11','B12'],
                    'C':['C8','C9','C10','C11','C12']})
print(df3)

#Concatenado vertical
df_columnas = pd.concat([df1,df2,df3], axis=0)
df_columnas

#
df_columnas = pd.concat([df1,df2,df3], axis=0, keys=['df1','df2','df3'])
df_columnas

df_columnas.loc['df2']
df_columnas.loc['df2'].iloc[1]

#Concatenacion Horizontal
dfHorizontal = pd.concat([df1,df2,df3], axis = 1, keys=['df1','df2','df3'])
print(dfHorizontal)

#Si queremos modificar los indices de una tabla
df3.index=[2,5,3,4,10]
print(df3)

#Sin embargo eso modificaria nuestro df a la hora de pegarlo 
dfHorizontal = pd.concat([df1,df2,df3], axis = 1, keys=['df1','df2','df3'])
print(dfHorizontal)

#%% JOINS

izquierda = pd.DataFrame({'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3'],
                    'C':['C0','C1','C2','C3'],
                    }, index=['clv0','clv1','clv2','clv3'])
print(izquierda)

derecha = pd.DataFrame({'D':['D0','D1','D2','D3','D4'],
                        'E':['E0','E1','E2','E3','E4']},
                       index=['clv0','clv2','clv1','clv5','clv6'])
print(derecha)

#Creamos una nueva columna en cada uno de los df
izquierda['col_joinIzq']= izquierda.index
derecha['col_joinDer']= derecha.index

#%%
# METODOS de los JOINS
#Inner Join (intercepcion)
joinInt= izquierda.join(derecha.set_index(['col_joinDer']), on=['col_joinIzq'], how='inner')
print(joinInt)
#Nos muestra los registros de los id (col_join) que coinciden en ambos df

#Lo podemos ver como conjuntos o sets de la siguiente forma
set(izquierda['col_joinIzq']).intersection(set(derecha['col_joinDer']))

#Modificamos el df derecha
derecha = pd.DataFrame({'D':['D0','D1','D2','D3','D4','F4'],
                        'E':['E0','E1','E2','E3','E4','G5']},
                       index=['clv0','clv2','clv1','clv5','clv6', 'clv1'])

#Con la modificacion a derecha, podemos notar que el id clv1 está repetido.¿que sucede aqui?
joinInt_modif= izquierda.join(derecha.set_index(['col_joinDer']), on=['col_joinIzq'], how='inner')
print(joinInt_modif)
#Muestra ambos registros de clv1

#Ahora que pasaría si tuvieramos columnas de nombres iguales
#Modificamos izquierda
izquierda = pd.DataFrame({'D':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3'],
                    'C':['C0','C1','C2','C3'],
                    }, index=['clv0','clv1','clv2','clv3'])
print(izquierda)

join0 = izquierda.join(derecha.set_index(['col_joinDer']),on=['col_joinIzq'],how='inner' )
print(join0)
#Nos marca un error por que no pueden haber dos columnas del mismo nombre
#Se puede corregir con suffix, el cual añade un sufijo a la columna repetida 
join0 = izquierda.join(derecha.set_index(['col_joinDer']),on=['col_joinIzq'],how='inner',rsuffix='der' )
print(join0)
#%%
join_izquierdo = izquierda.join(derecha.set_index(['col_joinDer']), on=['col_joinIzq'], how='left', rsuffix='der')
print(join_izquierdo)


join_derecho = derecha.join(izquierda.set_index(['col_joinIzq']),on=['col_joinDer'], how='right', rsuffix='izq')
print(join_derecho)


join_completo=izquierda.join(derecha.set_index(['col_joinDer']),on=['col_joinIzq'],how='outer',lsuffix='der') 
print(join_completo)