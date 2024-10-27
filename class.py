#circle class
class circle:
    def __init__(self):
        self.radius = 0
        self.color = ''
        self.pi = 3.14

    def getColor(self):
        return self.color
    
    def getCircumference(self):
        Circumference = self.pi * 2 * self.radius
        return Circumference
    
#player class
class player:
    def __init__(self):
        self.inventory = {}
        self.money = 100
        self.health = 100

    #inventory
    def add_item(self, item, quantity=1):
        self.inventory[item] = self.inventory.get(item, 0) + quantity

    def remove_item(self, item, quantity=1):
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
            if self.inventory[item] == 0:
                del self.inventory[item]

    #money
    def increase_money(self, money):
        self.money += money

    def decrease_money(self, money):
        self.money -= money

    #health
    def decrease_health(self, health):
        self.health -= health
        if self.health <= 0:
            print("dead")

    def increase_health(self, health):
        self.health += health

#catherine class
import time

class catherine:
    def __init__(self):
        self.hobbies = []
        self.friends = {}
        self.energy = 100
        self.skills = {}

    #hobbies
    def add_hobby(self, hobby):
        if hobby not in self.hobbies:
            self.hobbies.append(hobby)
            print(f"added hobby: {hobby}")
        else:
            print(f"hobby '{hobby}' is already on the list")

    #friends
    def make_friend(self, name, trust=0):
        self.friends[name] = trust
        print(f"you are now friends with {name}, trust level currently at: {trust}")

    def add_trust_level(self, name, time_spent):
        if name in self.friends:
            self.friends[name] += time_spent * 5
            print(f"hung out with {name}, trust level is now {self.friends[name]}")
        else:
            print(f"{name} is not a friend yet, make friends with them first")
    
    #skills
    def practice_skill(self, skill, hours):
        if skill in self.skills:
            self.skills[skill] += hours * 2
            self.energy -= hours * 10
            print(f"practiced {skill} for {hours} hours, skill level is now {self.skills[skill]}")
            if self.energy <= 0:
                print("take a break, you don't have anymore energy")
        else:
            print("you have not learnt this skill yet")

    def learn_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
            print(f"added skill: {skill}")
        else:
            print(f"skill '{skill}' is already on the list")

    #recharge energy
    def increase_energy(self):
        while self.energy < 100:
            self.energy = min(100, self.energy + 10)
            print(f"energy increased to {self.energy}")
            if self.energy == 100:
                print("energy is full")
                break
            time.sleep(15 * 60)

    def display_status(self):
        print(f"hobbies: {', '.join(self.hobbies)}")
        print(f"friends: {self.friends}")
        print(f"skills: {self.skills}")
        print(f"energy: {self.energy}")