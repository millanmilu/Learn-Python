class prod:
	def __init__(self,value):
		self.value =value
	def __call__(self,other):	#__call__ is a function 
		return self.value *other

x =prod(2)
print(x(2))
print(x(6))		