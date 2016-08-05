class Band_Member():
	
	def __init__ (self, name, band_name, eye_color, instrument, age, swoon_worthy):
		self.name = name
		self.band_name = band_name
		self.eye_color = eye_color
		self.instrument = instrument
		self.age = age
		self.swoon_worthy = swoon_worthy

	def sing(self):
		print("La la la la!")

	def gets_older(self):
		self.age += 1
		print(self.age)

	def learns_new_instrument(self, para_instrument):
		self.instrument = para_instrument

	def is_swoon_worthy():
		if self.eye_color == "green" and self.swoon_worthy:
			print("Oh Baby")
		else:
			print("meh")

harry = Band_Member("Harry Styles", "One Direction", "green", "voice", 22, True)

harry.learns_new_instrument("guitar")

louis = Band_Member("Louis Tomlinson", "One Direction", "blue", "voice", 24, True)

one_direction = []
one_direction.append(harry)
one_direction.append(louis)

for member in one_direction:
	print(member.name)
	print(member.band_name)
	member.sing()