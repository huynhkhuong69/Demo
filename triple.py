 #decorator function
def tripler(func):        
    def wrapper():
        print("You're now Decorated")
        func()				# this function is used on three times
        func()				# this function is used on three times	
        func()				# this function is used on three times
    return wrapper

#define another function
def decorate_me():
    print("This is python!")
    
decorated = tripler(decorate_me)
decorated()
