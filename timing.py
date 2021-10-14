import time

#decorator function
def calculate_time(func):
    """The decorator will calculate the the time will run the function"""
    #inner function can use the outer function
    def wrapper():

        #store start time
        #time.time() to get the current time in seconds
        start = time.time()

        #calling timer function in the wrapper function
        timer()

        #store end time
        end = time.time()

        #print total time
        print(end - start)
 
    return wrapper

#this function will be call in the wrapper function
#use time.sleep(2) to test
def timer():
    print("Time")
    
#let's decorate timer function
run_timer = calculate_time(timer) 
run_timer()
