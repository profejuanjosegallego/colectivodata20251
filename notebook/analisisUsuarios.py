import pandas as pd

dataFrameUsuarios=pd.read_excel("./data/usuarios_sistema_completo.xlsx")
# print(dataFrameUsuarios)

#Extraer datos basicos de la data ingresada
# print(dataFrameUsuarios.head(100))
print(dataFrameUsuarios.tail())