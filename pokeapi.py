import requests
import random 

class Pokemon():
    def __init__(self, name):
        self.name = name
        self.types = {}
        self.abilities = {}
        self.weight = 0
        self.height = 0
        self.image = None
        self.moves = []
        self.poke_api_call()
        
    def poke_api_call(self):
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}")
        if r.status_code == 200:
            pokemon = r.json()
        else:
            print(f"Please check your pokemon name spelling and try again: {r.status_code}")
            
        self.name = pokemon['name']
        self.types = [type_['type']['name'] for type_ in pokemon['types']]
        self.abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
        self.weight = pokemon['weight']
        self.height = pokemon['height']
        self.image = pokemon['sprites']['front_default']
        print(f'{self.name.title()}\'s data has been updated to your pokedex.')
        self.moves = [move['move']['name'] for move in pokemon['moves']]
        

    def __repr__(self):
        return f'You caught a {self.name}'
    
   
dragonite = Pokemon('dragonite')



class Move_Tutor(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.move_list = []
        
    def teach_move(self):
        id_num = random.randint(0, 444)
        r = requests.get(f'https://pokeapi.co/api/v2/move/{id_num}/')
        if r.ok:
            move = r.json()
            move_name = move['name']
            if move_name in self.moves:
                self.move_list.append(move_name)
                print(f'{self.name.title()} has now learned {move_name}')
            else:
                print(f"{self.name.title()} cannot learn {move_name}")

        return self.move_list
    

dragonite = Move_Tutor('dragonite')
dragonite.teach_move()
print(dragonite.move_list)
dragonite.teach_move()
print(dragonite.move_list)
dragonite.teach_move()
print(dragonite.move_list)
dragonite.teach_move()
print(dragonite.move_list)
dragonite.teach_move()
print(dragonite.move_list)
dragonite.teach_move()
print(dragonite.move_list)