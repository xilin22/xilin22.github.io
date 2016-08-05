# class it up
'''
Pseudocode:
1. make a class
2. create meathod withinin class that all objects can do
3. create some objects
4. store the objects inside an empty list
5. loop through the list printing out the attributes and calling the methods inside the class
6 use an index variable to loop throught the list.

'''

class Fairytale_Character():
	def __init__(self, chara_type, color, species, where_they_live, weapon):
		self.chara_type = chara_type
		self.color = color
		self.species = species
		self.where_they_live = where_they_live
		self.weapon = weapon

	def power(self):
		print("Magic!!!")

	def doing_job(self):
		print("Doing some fairytale job thing.")

	def get_better_weapon(self, new_weapon):
		self.weapon = new_weapon
		print("Got new weapon: " + new_weapon)

dragon = Fairytale_Character("dragon", "green", "magical reptiles", "caves", "fire breath")
wizard = Fairytale_Character("wizard", "purple", "magical humans", "basement", "magic wands")

characters = []
characters.append(dragon)
characters.append(wizard)

index = 0

for character in characters:
	print(index)
	print(characters[index])
	print(character.chara_type)
	print(character.color)
	print(character.species)
	print(character.where_they_live)
	print(character.weapon)
	Fairytale_Character.power(characters[index])
	Fairytale_Character.doing_job(characters[index])
	input1 = input("Pick new weapon: ")
	Fairytale_Character.get_better_weapon(characters[index], input1)
	index += 1
