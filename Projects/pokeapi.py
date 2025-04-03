'''
Lista los 151 primeros pokemon
utilizando la pokéAPI
'''
import requests 

pokemon_url = "https://pokeapi.co/api/v2/pokemon?limit=151"
response = requests.get(pokemon_url, timeout=5)

list_pokemon = response.json()['results']

for pokemon in list_pokemon:
    print(f'Nombre: {pokemon['name']}')
    
    