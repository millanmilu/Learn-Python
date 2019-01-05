class ClassName(object):
	college="East clg"#class  shared by all instances
	"""docstring for ClassName"""
	def __init__(self,name): #instance variable unique to each instance
		super(ClassName, self).__init__()
		self.name=name

d=ClassName("Millan")
print(d.name)
print(d.college) #share by all classname

		