import random

def guess(secret_number):
    numero_intentos = 10
    guess_number = None  
    
    while numero_intentos > 0:
        guess_number = int(input('Introduce el numero que crees que es correcto: '))  
        if secret_number == guess_number:
            print('Congratulations. WIN 😊')
            return  # Exit the function 
        else:
            print('Numero incorrecto, vuelve a intentarlo')
            print('Número demasiado alto' if guess_number > secret_number else 'Número demasiado bajo')
            numero_intentos -= 1
            print(f'Te quedan {numero_intentos} intentos')
    
    print('Perdiste 😒')  # Print this message if out of attempts

# Generate the secret number and call the function
secret_number = random.randint(1, 10)
guess(secret_number)