def tripler(func):

"""The decorate_func() will pass the message "This is Python!" into the func 
as an argument, then  the func() were used 3 times in the inner_fuc
"""
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
