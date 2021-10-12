import time

def calculate_time(self):

    #store start time
    start = time.time()
    time.sleep(2)

    #store end time
    end = time.time()

    #print total time
    print("Total time ", end - start)

calculate_time()

