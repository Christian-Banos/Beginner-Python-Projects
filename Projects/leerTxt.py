#contador con espacios
contador = 0

with open('leet.txt') as archivo_objeto:
    lineas = archivo_objeto.read().strip()
    for letra in range(0, len(lineas)):
         contador += 1

print('contador con espacios', contador)

#contador solo de letras


def contador(archivo):
    contador_letras = 0
    
    with open(archivo) as new_archivo:
        letras = new_archivo.read().strip()
        for letra in letras:
            if letra.isalpha():
                contador_letras += 1
    return contador_letras

print('contador de letras', contador('leet.txt'))