'''
Creating Pokemons!
'''

class Pokemon():
    '''
    Abstract class, only serves as base class
    Creates the Pokemon base class
    '''
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f'{self.name} {self.name}'

class Pikachu(Pokemon):

    def attack(self):
        return 'Thunderbolt'

p = Pikachu('Pika')

print(p.speak())
print(p.attack())