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
    page = requests.get(url)
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