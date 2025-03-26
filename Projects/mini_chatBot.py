"""
Un chatbot simple que responde consultas sobre disponibilidad de cervezas.
El usuario puede preguntar por diferentes marcas y el bot responderá si están en stock o no.
"""

respuestas = {
    'guinnes': 'En stock',
    'coors': 'En stock',
    'kelkenny': 'En stock',
    'corona': 'En stock',
    'mahou': 'Fuera de stock',
    'heineken': 'Fuera de stock',
    'estela': 'Fuera de stock'
}

print('Bienvenido al chatbot de cervezas')
print('Escribe "salir" para salir')
print('Que producto estas buscando?')

while True:
    entrada = input('tu: ').lower()
    if entrada == 'salir':
        print('bot: ¡Hasta luego!')
        break
    if entrada in respuestas:
        print('bot:', respuestas[entrada])
    else:
        print('bot: Lo siento, no tenemos esa cerveza en nuestro catálogo')