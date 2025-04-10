'''
With this exercise we have to get the ranking with the countries with the highest number of medals using web scraping
'''

import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

url = "https://elpais.com/deportes/resultados/juegos-olimpicos/medallero/"

try:
    page = requests.get(url, timeout=5)
    page.raise_for_status()  # Esto verificará si hay errores HTTP
except requests.exceptions.RequestException as e:
    print('Error al abrir la pagina', {e})
    exit()
    
# Verificamos si obtuvimos contenido
if not page.content:
    print('No se obtuvo contenido de la página')
    exit()

#Parseamos el html y lo guardamos en una variable
soup = BeautifulSoup(page.text, 'html.parser')

#buscanmos el div correspondiente para extraer su contenido
content = soup.find('table', {'class' : 'tabla-datos table-hover table-striped medallero'})
if not content:
    print('No se encontró la tabla de medallero')
    exit()
    
tablero = []
for fila in content.find_all('tr'):
    # Extraemos el texto de cada celda (td) en la fila
    datos_fila = [celda.text.strip() for celda in fila.find_all(['td', 'th'])]
    if 'Total' in datos_fila: # Solo añadimos filas que tengas datos
        tablero.append(' | '.join(datos_fila))
    else:
        # Intentamos convertir el total (ultima columna) a número
        try:
            total = int(datos_fila[-1])
            if total > 0: # solo añadimos si el total es mayor que 0
                tablero.append(' | '.join(datos_fila))
        except ValueError:
            continue # Si no podemos convertir a número, saltamos la fila
print('\n'.join(tablero))

# Crear DataFrame con los top 5 países
df = pd.DataFrame({
    'País': [fila.split(' | ')[0] for fila in tablero[1:6]],
    'Medallas': [int(fila.split(' | ')[-1]) for fila in tablero[1:6]]
})
print("\nTop 5 países en formato tabla:")
print(df)

# Convertir datos a arrays para visualización
paises = np.array([fila.split(' | ')[0] for fila in tablero[1:6]])  # Top 5 países
medallas = np.array([int(fila.split(' | ')[-1]) for fila in tablero[1:6]])  # Sus medallas

# Crear gráfica de barras
plt.figure(figsize=(10, 6))
plt.bar(paises, medallas)
plt.title('Top 5 Países por Medallas Olímpicas')
plt.xticks(rotation=45)
plt.show()
