import time

#decorator function
def calculate_time(func):
    """The decorator will calculate the the time will run the function"""
    #inner function can use the outer function
    def wrapper():

        #store start time
        #time.time() to get the current time in seconds
        start = time.time()

        #calling 
        func()

        #store end time
        end = time.time()

        #print total time
        print(end - start)
 
    return wrapper

def print_time():
    print("Total time")
    

 
