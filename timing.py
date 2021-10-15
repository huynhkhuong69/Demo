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
        print("Total time", end - start)
 
    return wrapper

def print_time():
    time.sleep(2)
   
print_time = calculate_time(print_time)

print_time()

 
