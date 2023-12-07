import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo Excel
archivo_excel = "Libro1.xlsx"
datos_excel = pd.read_excel(archivo_excel)

# Grafica la relación entre estatura y cantidad de goles
plt.figure(figsize=(10, 6))
plt.scatter(datos_excel['Estatura'], datos_excel['Goles'], color='purple', alpha=0.7)
plt.xlabel('Estatura')
plt.ylabel('Goles')
plt.title('Relación entre Estatura y Cantidad de Goles Anotados')
plt.grid(True)
plt.show()
