import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")

#GRAFICANDO 

#Grafica de Barras
colors=["#28782c","#007249","#00695d","#005f66","#095364","#2f4858"]
plt.figure(figsize=(8,5))
sns.countplot(x='estado',data=dataFrameAsistencia, palette=colors)
plt.title("Cantidad de registros por estado de asistencia")
plt.xlabel("Estado de asistencia")
plt.ylabel("Cantidad de registros")
plt.tight_layout()
plt.show()

#Grafica de Torta
#Mostrar proporciones entre dos columnas del DF (proporcion de estudiantes x medio de transporte)
conteoMedioTransporte=dataFrameAsistencia['medio_transporte'].value_counts()

plt.figure(figsize=(5,5))
plt.pie(
    conteoMedioTransporte,
    labels=conteoMedioTransporte.index,
    autopct='%1.1f%%',
    colors=sns.color_palette("Blues")
)
plt.title("Disitribucion de estudiantes por medio de transporte")
plt.tight_layout()
plt.show()

#Grafico de Barras Agrupadas
#Se aplica cuando hice cruces en el dataframe
conteoEstadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size().unstack(fill_value=0)

conteoEstadoMedioTransporte.plot(
    kind='bar',
    figsize=(10,6),
    color=colors
)
plt.title("Registras por estado de asistencia y medio de transporte")
plt.xlabel("Estado de asistencia")
plt.ylabel("Cantidad de registros")
plt.legend(title="Medio de transporte")
plt.tight_layout()
plt.show()