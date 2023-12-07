import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo Excel
archivo_excel = "Libro1.xlsx"
datos_excel = pd.read_excel(archivo_excel)

# Agrupa por pierna dominante y calcula el promedio total de goles
promedio_goles_por_pierna = datos_excel.groupby('Pierna dominante')['Goles'].mean().reset_index()

# Grafica el promedio total de goles por pierna dominante
plt.figure(figsize=(8, 5)).canvas.manager.set_window_title('Goles_promedio_por_pierna_dominante')
plt.bar(promedio_goles_por_pierna['Pierna dominante'], promedio_goles_por_pierna['Goles'], color='green')
plt.xlabel('Pierna dominante')
plt.ylabel('Promedio Total de Goles')
plt.title('Promedio Total de Goles por Pierna Dominante')
plt.show()
