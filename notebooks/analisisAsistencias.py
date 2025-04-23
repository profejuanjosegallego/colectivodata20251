import pandas as pd

#Extraer la informacion
dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")

#Extraer datos basicos de la data ingresada
#print(dataFrameAsistencia.head(100))
#print(dataFrameAsistencia.tail())
#print(dataFrameAsistencia.info())
#print(dataFrameAsistencia.describe())
print(dataFrameAsistencia["estrato"].value_counts().head(2))