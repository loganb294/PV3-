import random



class Character:
    def __init__(self, name, health, min_attack_power, max_attack_power):
        self.name = name
        self.health = health
        self.attack_power = random.randint(min_attack_power, max_attack_power)
        self.defense = min(random.randint(1, self.attack_power - 1), self.attack_power - 1)

    def attack(self, other):
        damage = max(5, random.randint(5, 25) - other.defense)
        other.health = max(0, other.health - damage)
        print(f"{self.name} attacks {other.name} and deals {damage} damage.")

    def defend(self):
        self.defense += 5
        print(f"{self.name} is defending. Defense increased by 5.")

    def heal(self):
        heal_amount = random.randint(10, 20)
        self.health = min(100, self.health + heal_amount)
        print(f"{self.name} heals for {heal_amount} health.")

    def special_attack(self, other):
        damage = max(10, 2 * random.randint(5, 25) - other.defense)
        other.health = max(0, other.health - damage)
        print(f"{self.name} uses a special attack on {other.name} and deals {damage} damage!")



# Set different attack power ranges for each character
player = Character("Player", 100, 15, 25)
enemy = Character("Ricky", 100, 14, 23)


def display_stats(player, enemy):
    print(f"{player.name} Health: {player.health} | Defense: {player.defense} | atk power: {player.attack_power} ")
    print(f"{enemy.name} Health: {enemy.health} | Defense: {enemy.defense} | atk power: {enemy.attack_power} ")

def perform_action(character, action, target=None):
    if action == '1':
        character.attack(target)
    elif action == '2':
        character.defend()
    elif action == '3':
        character.heal()
    elif action == '4':
        character.special_attack(target)
    else:
        print("Invalid choice. Try again.")

def main(player, enemy):
    while player.health > 0 and enemy.health > 0:
        print(f"\n{player.name} Turn:")
        display_stats(player, enemy)
        print("Choose your action:")
        print("1. Attack")
        print("2. Defend")
        print("3. Heal")
        print("4. Special Attack")
        choice = input("Enter your choice (1-4): ")

        perform_action(player, choice, enemy)

        check_for_winner(player,enemy)

        print(f"\n{enemy.name} Turn:")
        enemy_choice = random.choice(['1', '2', '3', '4'])
        perform_action(enemy, enemy_choice, player)

        check_for_winner(player,enemy)

def check_for_winner(player,enemy):
    if player.health <= 0:
        print("\nGame Over!")
        print("You lose!")
    elif enemy.health <= 0:
        print("\nGame Over!")
        print("You win!")


if __name__ == "__main__":
    main(player, enemy)
