def myFunc(e):
	return len(e)

cars =["ford","BMW","Vw"]
cars.sort(reverse =True ,key=myFunc)
print(cars)	