import random

class Pokemon:
    def __init__(self, nome, tipo, hp, ataque):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.ataque = ataque
    
    def atacar(self, outro_pokemon):
        dano = random.randint(1, self.ataque)
        outro_pokemon.hp -= dano
        print(f"{self.nome} atacou {outro_pokemon.nome} e causou {dano} de dano!")

def batalha(pokemon1, pokemon2):
    print(f"Batalha entre {pokemon1.nome} ({pokemon1.tipo}) e {pokemon2.nome} ({pokemon2.tipo})!")
    while pokemon1.hp > 0 and pokemon2.hp > 0:
       
        pokemon1.atacar(pokemon2)
        if pokemon2.hp <= 0:
            print(f"{pokemon2.nome} foi derrotado! {pokemon1.nome} venceu a batalha!")
            break
        
        
        pokemon2.atacar(pokemon1)
        if pokemon1.hp <= 0:
            print(f"{pokemon1.nome} foi derrotado! {pokemon2.nome} venceu a batalha!")
            break


pokemons = [
    Pokemon("Pikachu", "Elétrico", 100, 20),
    Pokemon("Charmander", "Fogo", 120, 18),
    Pokemon("Bulbasaur", "Planta", 110, 22),
    Pokemon("Squirtle", "Água", 105, 19)
]


pokemon1, pokemon2 = random.sample(pokemons, 2)


batalha(pokemon1, pokemon2)
