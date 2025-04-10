from typing import override
import random

class Participant:
    
    def __init__(self, name, country):
        self.name = name
        self.country = country
        
    def __str__(self):
        return f'El participante {self.name} esta representando a {self.country}'
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Participant):
            return self.name == other.name and self.country == other.country
        return False


    def __hash__(self) -> int:
        return hash((self.name, self.country))
    

class Olimpics:
    """A class that manages Olympic events and participants.
    
    This class handles the organization of Olympic events, including managing
    participants, their registrations, and event operations.
    """
    
    def __init__(self):
        self.events = []
        self.participants = {}
        self.events_results = {}
        self.country_results = {}
        
    #registro de eventos deportivos
    def register_event(self):
        event = input('Introduce el nombre del evento deportivo: ')
        
        if event in self.events:
            print(f'El evento {event} ya está registrado')
        else:
            self.events.append(event)
            self.participants[event] = []  # Inicializar lista de participantes para el nuevo evento
            print(f'Evento {event} registrado correctamente')
    
    #registro de participantes
    def register_participant(self):
        if not self.events:
            print('No hay eventos registrados. Por favor, registra uno primero.')
            return
        
        name = input('Introduce el nombre del participante: ')
        country = input('Introduce el país del participante: ')
        participant = Participant(name, country)
          
        print('Eventos Disponibles: ')
        for index, event in enumerate(self.events):
            print(f'{index + 1} - {event}')
          
        try:
            event_choice = int(input('Selecciona el número del evento para asignar al participante: ')) - 1
            
            if 0 <= event_choice < len(self.events):
                event = self.events[event_choice]
                
                if event not in self.participants:
                    self.participants[event] = []
                
                if participant in self.participants[event]:
                    print(f'El participante {name} de {country} ya está registrado en el evento {event}')
                else:
                    self.participants[event].append(participant)
                    print(f'El participante {name} de {country} se ha registrado en el evento deportivo {event}')
            else:
                print('Selección de evento deportivo no válido. El participante no se ha registrado')
        except ValueError:
            print('Por favor, introduce un número válido para seleccionar el evento')
            
    #simulacion de eventos
    def simulate_events(self):
        if not self.events:
            print('No hay eventos registrados. Por favor, registra uno primero')
            return
            
        for event in self.events:
            if len(self.participants[event]) < 3:
                print(f'No hay participantes suficientes para simular el evento {event}')
                continue
            
            event_participants = random.sample(self.participants[event], 3)
            random.shuffle(event_participants)
            gold, silver, bronze = event_participants
            
            self.events_results[event] = [gold, silver, bronze]
            
            self.update_country_results(gold.country, 'gold')
            self.update_country_results(silver.country, 'silver')
            self.update_country_results(bronze.country, 'bronze')
            
            print(f'Simulación del evento: {event}')
            print(f'Oro: {gold.name} ({gold.country})')
            print(f'Plata: {silver.name} ({silver.country})')
            print(f'Bronce: {bronze.name} ({bronze.country})')
        
    #resultado por paises        
    def update_country_results(self, country, medal):
        if country not in self.country_results:
            self.country_results[country] = {'gold': 0, 'silver': 0, 'bronze': 0}
        self.country_results[country][medal]
        
    #crear el informe
    def show_report(self):
        print('Informe juegos olimpicos')
        
        if self.events_results:
            for event, winners in self.events_results.items():
                print(f'Evento: {event}')
                print(f'Oro: {winners[0].name} ({winners[0].country})')
                print(f'Plata: {winners[1].name} ({winners[1].country})')
                print(f'Bronce: {winners[2].name} ({winners[2].country})')
        else:
            print('No hay resultados de eventos')
            
        if self.country_results:
            for country, medals in sorted(self.country_results.items(), key=lambda x: (x[1]['gold'], x[1]['silver'], x[1]['bronze']), reverse=True):
                print(f'{country}: Oro {medals["gold"]}, Plata {medals["silver"]}, Bronce {medals["bronze"]}')
        else:
            print('No hay medallas registradas')
            
#instancias
olympics = Olimpics()


print('Simulador de Juegos olimpicos')

while True:
    
    print()
    
    print('1. Registro de eventos')
    print('2. Registro de participantes')
    print('3. Simulación de eventos')
    print('4. Creación de informes')
    print('5. Salir del programa')

    option = input('Selecciona una acción: ')
    
    match option:
        case '1':
            olympics.register_event()
        case '2':
            olympics.register_participant()
        case '3':
            olympics.simulate_events()
        case '4':
            olympics.show_report()
        case '5':
            print('Saliendo del simulador...')
            break
        case _: #caso par defecto
            print('Opción inválida. Por Favor, selecciona una nueva')
