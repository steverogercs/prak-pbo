class Character:

    def __init__(self, name: str, attack: int, defense: int, health: int) -> None:
        self.__name = name
        self.__attack = attack
        self.__defense = defense
        self.__health = health

    def get_name(self) -> str:
        return self.__name

    def get_attack(self) -> int:
        return self.__attack

    def get_defense(self) -> int:
        return self.__defense

    def get_health(self) -> int:
        return self.__health

    def set_health(self, health: int) -> None:
        self.__health = health
        if self.__health < 0:
            self.__health = 0

    def __sub__(self, other) -> int:
        print(f'Attacking ... Done.')

        if isinstance(other, int):

            if other > self.__defense:
                self.__health -= (other - self.__defense)
                return self.__health

            return self.__health
        if isinstance(other, Hero):
            if other.get_attack() > self.__defense:
                self.__health -= (other.get_attack() - self.__defense)
                return self.__health

            return self.__health

    def __add__(self, value: int) -> int:
        return self.__attack + value

    def __str__(self) -> str:
      
        return f'Health {self.__name} sekarang tinggal {self.__health}.'

class Hero(Character):
    
    def __init__(self, name: str, attack: int, defense: int, health: int, mana: int) -> None:
        super().__init__(name, attack, defense, health)
        self.__mana = mana
        self.__skills = {
            'fire': 30,
            'water': 30,
            'earth': 30,
            'wind': 30,
            'lightning': 30
        }

    def get_mana(self) -> int:
        return self.__mana
      
    def set_mana(self, mana: int) -> None:
        self.__mana = mana
      
    def get_skill(self, skill: str) -> int:
        
        if self.__mana >= self.__skills[skill]:
            self.__mana -= self.__skills[skill]
      
        return 0

    def set_skill(self, skill: str, value: int) -> None:
        self.__skills[skill] = value
      
    def __str__(self) -> str:
    
        return f'Health dan mana {self.get_name()} sekarang tinggal {self.get_health()} dan {self.__mana}.'

def main() -> None:
    hero = Hero(name='Ma Chao', attack=20, defense=10, health=100, mana=100)

    monster = Character(name='Zhou Yun', attack=10, defense=10, health=100)

    monster - (hero + hero.get_skill('fire'))
    monster - hero
    print(monster)
    print(hero)

if __name__ == '__main__':

    main()