import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

#Importamos el archivo que vamos a analizar los datos
file_path='/Users/Usuario/Desktop/Cosas de universidad/logica de programacion/Final/housing.csv'
data = pd.read_csv(file_path,usecols=['longitude','latitude','median_house_value'])
data=data.dropna()
print(data)


#Especificamos 'longitud' como el eje X, 'latitud' como en el eje Y y 'median_house_value' como el atributo 'hue'
sns.scatterplot(data=data,x='longitude',y='latitude',hue='median_house_value')
plt.show()

#Creamos una instancia de StandardScaler para la normalizacion de caracteristicas
scaler=StandardScaler()
data_scaled=scaler.fit_transform(data)

#Calculamos los puntajes de silueta para diferentes valores de la K (numero de los grupos o clusters)
silhouette_scores=[]

for k in range(2,11):
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(data_scaled)
    score=silhouette_score(data_scaled,kmeans.labels_)
    silhouette_scores.append(score)

#Graficamos los puntajes de silueta para diferentes valores de K
plt.plot(range(2,11),silhouette_scores,marker='o')
plt.xlabel('Numero de Clusters(k)')
plt.ylabel('Coeficientes de Silueta')
plt.title('Coeficiente de Silueta para diversos valores de K')
plt.show()

#Establecemos el numero de los grupos K en 2
k=2

kmeans=KMeans(n_clusters=k,init='k-means++',random_state=42)
kmeans.fit(data_scaled)

#Obtenemos los grupos clusters y los centroides
labels=kmeans.labels_
centroids=kmeans.cluster_centers_

#Mostramos el greafico de dispersion 
plt.scatter(data_scaled[:, 0],data_scaled[:, 1],c=labels, s=50, cmap='viridis')
plt.scatter(centroids[:,0],centroids[:,1],marker='X',s=200,c='red')
plt.xlabel('longitud')
plt.ylabel('latitud')
plt.title('Centroides de los grupos obtenidos de los k-means')
plt.figure()
plt.show()
