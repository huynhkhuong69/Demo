def tripler(func):
	def inner_func():
		print("Decorate Message!")
		func()
		func()
		func()
	return inner_func

def decorate_func():
	print("This is Python!")

decorated = triple(decorate_func)
decorated()
