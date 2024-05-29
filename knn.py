import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

dataframe ='/Users/Usuario/Desktop/Cosas de universidad/logica de programacion/Final/creditos.csv'
data = pd.read_csv(dataframe)
num=data.head(202)

buenos=data[data['cumplio']==1]
malos=data[data['cumplio']==0]
print(malos)
print(buenos)

#Vamos a graficar pagadores vs deudores
plt.scatter(buenos["edad"],buenos["credito"],
            marker="*",s=150,color="purple",
            label="Si pago(clase:1)"
            )
plt.scatter(malos["edad"],malos["credito"],
            marker="*",s=150,color="red",
            label="No pago(clase:0)"
            )
plt.ylabel("Monto del credito")
plt.xlabel("Edad")
plt.legend(bbox_to_anchor=(1,0.2))
#plt.show()

#Peraracion de los datos a Escalar

datos=data[["edad","credito"]]
clase=data["cumplio"]

escalador=preprocessing.MinMaxScaler()
datos=escalador.fit_transform(datos)
print(datos)

#Clasificador de los vecinos cercanos
clasificador=KNeighborsClassifier(n_neighbors=3)
clasificador.fit(datos,clase)

#Aca podemos agregarle mas datos a nuestra base de datos 
#Datos sinténticos de todos los posibles solicitantes
creditos = np.array([np.arange(100000, 600010, 1000)]*43).reshape(1, -1)
edades = np.array([np.arange(18, 61)]*501).reshape(1, -1)
todos = pd.DataFrame(np.stack((edades, creditos), axis=2)[0],
                     columns=["edad", "credito"])

#Escalar los datos
solicitantes = escalador.transform(todos)

#Predecir todas las clases
clases_resultantes = clasificador.predict(solicitantes)

#Código para graficar
buenos = todos[clases_resultantes==1]
malos = todos[clases_resultantes==0]
plt.scatter(buenos["edad"], buenos["credito"],
            marker="*", s=150, color="blue", label="Sí pagará (Clase: 1)")
plt.scatter(malos["edad"], malos["credito"],
            marker="*", s=150, color="green", label="No pagará (Clase: 0)")
plt.ylabel("Monto del crédito")
plt.xlabel("Edad")
plt.legend(bbox_to_anchor=(1, 0.2))
plt.show()