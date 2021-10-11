#decorator function
def tripler(func):

"""The decorate_func() will pass the message "This is Python!" into the func 
as an argument, then  the func() were used 3 times in the inner_fuc
"""
# func() is used 3 times
	def inner_func():
		print("Decorate Message!")
		func()
		func()
		func()
	return inner_func

#define another function
def decorate_func():
	print("This is Python!")

# pass the decorate_func as an argument
decorated = triple(decorate_func)
decorated()
