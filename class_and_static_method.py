class Person:
	TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
	def fullname(self): # instance method
# instance object accessible through self
		return "Full Name :%s %s" % (self.name, self.surname)
	@classmethod
	def allowed_titles_starting_with(cls, startswith): # class method
		#return [t for t in Person.TITLES if t.endswith(endswith)]
# class or instance object accessible through cls
		for t in cls.TITLES:
			if t.startswith(startswith):
				return t

	@staticmethod
	def allowed_titles_ending_with(endswith): # static method
# no parameter for class or instance object
# we have to use Person directly
		return [t for t in Person.TITLES if t.endswith(endswith)]
		# for t in Person.TITLES:
		# 	if t.endswith(endswith):
		# 		return t

jane = Person("Jane", "Smith")
print(jane.fullname())
print(jane.allowed_titles_starting_with("M"))
print(Person.allowed_titles_starting_with("M"))
print(jane.allowed_titles_ending_with("s"))
print(Person.allowed_titles_ending_with("s"))