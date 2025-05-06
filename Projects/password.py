import random
import string

def generador_de_contraseñas(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password

print('Contraseña generada: ',generador_de_contraseñas(12))


def password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for _ in range(longitud):
        password += random.choice(caracteres)
    
    return password

print('Contraseña dos: ', password(12))