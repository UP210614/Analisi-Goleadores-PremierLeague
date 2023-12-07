import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo Excel
archivo_excel = "Libro1.xlsx"
datos_excel = pd.read_excel(archivo_excel)

# Calcula la cantidad de jugadores por pierna dominante
pierna_dominante_counts = datos_excel['Pierna dominante'].value_counts()

# Crea un gráfico de torta
plt.figure(figsize=(8, 8))
plt.pie(pierna_dominante_counts, labels=pierna_dominante_counts.index, autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue','BLUE'])
plt.title('Proporción de Piernas Dominantes')
plt.show()
