 #decorator function
def tripler(func):        
    def inner():
        print("You are now decorated")
        func()				# this function is used on three times
        func()				# this function is used on three times	
        func()				# this function is used on three times
    return inner

#define another function
def decorate_me():
    print("This is python!")
    
decorated = tripler(decorate_me)
decorated()
