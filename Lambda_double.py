def my_fun(n):
	return lambda a:a*n

mydouble = my_fun(2)
print(mydouble(11))	