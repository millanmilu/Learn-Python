class Animal(object):
	"""docstring for ClassName"""
	def __init__(self,name,legs):
		super(Animal, self).__init__()
		self.name =name
		self.legs = legs
		self.stomach =[]

	def __call__(self,food):	
		self.stomach.append(food)

	def poop(self):
			if len(self.stomach)>0:	
				return self.stomach.pop(0)
	def __str__(self):			
		return ("A animal named %s" %(self.name))

cow =Animal("maa",4)
dog = Animal("Flop",4)

print("We have 2 animals a cow name %s and dog named %s ,both have %s legs" %(cow.name,dog.name,cow.legs))	
print(cow)

cow('gras')
print(cow.stomach)



dog('bone')
dog('beef')
print(dog.stomach)



print(cow.poop())
print(cow.stomach)