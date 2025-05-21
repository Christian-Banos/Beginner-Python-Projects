import json

archivo = 'persona.json'

# Leer el contenido existente o empezar con una lista vacía
try:
    with open(archivo, 'r') as f:
        personas = json.load(f)
except FileNotFoundError:
    personas = []

# Nuevas personas
nueva_persona = {
    'nombre': 'Maria',
    'edad': 30,
    'ciudad': 'Barcelona'
}

persona_dos = {
    'nombre': 'Chris',
    'edad': 35,
    'ciudad': 'Madrid'
}

# Añadir ambas personas
personas.extend([nueva_persona, persona_dos])

# Guardar en el archivo (una sola vez)
with open(archivo, 'w') as f:
    json.dump(personas, f, indent=4)

# Mostrar el contenido actualizado
with open(archivo, 'r') as f:
    contenido = json.load(f)
    print("Contenido del archivo:")
    for persona in contenido:
        print(persona)

#agregar nueva persona
nueva_persona3 = {
    'nombre': 'Laura',
    'edad': 28,
    'ciudad': 'Valencia'
}

personas.append(nueva_persona3)

#guardar lista actualizada
with open(archivo, 'w') as ar:
    json.dump(personas, ar, indent=4)
    
#mostrar el nuevo contenido
with open(archivo, 'r') as f:
    contenido = json.load(f)
    print('Nueva persona agregada correctamente:')
    for persona in contenido:
        print(persona)