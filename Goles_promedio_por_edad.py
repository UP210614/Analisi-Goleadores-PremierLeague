import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo Excel
archivo_excel = "Libro1.xlsx"
datos_excel = pd.read_excel(archivo_excel)

# Agrupa por edad y calcula el promedio de goles
promedio_goles_por_edad = datos_excel.groupby('Edad')['Goles'].mean().reset_index()

# Grafica el promedio de goles por edad
plt.figure(figsize=(12, 6)).canvas.manager.set_window_title('Goles_promedio_por_edad')
plt.bar(promedio_goles_por_edad['Edad'], promedio_goles_por_edad['Goles'], color='red')
plt.xlabel('Edad')
plt.ylabel('Promedio de Goles')
plt.title('Promedio de Goles por Edad')
plt.xticks(rotation=45, ha='right')  # Rotar etiquetas del eje x para mayor claridad
plt.show()
