import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo Excel
archivo_excel = "Libro1.xlsx"
datos_excel = pd.read_excel(archivo_excel)

# Crea un histograma de la cantidad de goles
plt.figure(figsize=(10, 6)).canvas.manager.set_window_title('Histograma_frecuencia_de_goles')
plt.hist(datos_excel['Goles'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Goles')
plt.ylabel('Frecuencia')
plt.title('Histograma de Goles')
plt.show()
