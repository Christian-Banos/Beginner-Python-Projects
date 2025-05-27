import json

mi_archivo = 'persona.json'

try:
    with open(mi_archivo, 'r') as ar:
        personas = json.load(ar)
        print(personas)
except FileNotFoundError:
    personas = []

# Nuevas personas
nueva_persona = {
    'nombre': 'Josefa',
    'edad': 19,
    'ciudad': 'Murcia'
}

personas.append(nueva_persona)

with open(mi_archivo, 'w') as f:
    json.dump(personas, f, indent=4)

with open(mi_archivo, 'r') as f:
    contenido = json.load(f)
    print(contenido)