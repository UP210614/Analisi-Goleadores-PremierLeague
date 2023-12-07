import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo Excel
archivo_excel = "Libro1.xlsx"
datos_excel = pd.read_excel(archivo_excel)

# Agrupa por estatura y calcula el promedio de goles
promedio_goles_por_estatura = datos_excel.groupby('Estatura')['Goles'].mean().reset_index()

# Grafica el promedio de goles por estatura
plt.figure(figsize=(12, 6))
plt.bar(promedio_goles_por_estatura['Estatura'], promedio_goles_por_estatura['Goles'], color='orange')
plt.xlabel('Estatura')
plt.ylabel('Promedio de Goles')
plt.title('Promedio de Goles por Estatura')
plt.xticks(rotation=45, ha='right')  # Rotar etiquetas del eje x para mayor claridad
plt.show()
