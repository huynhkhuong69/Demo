import time

def calculate_time():
 """The function calculate_time() willcompute the time to run a function.Use time.time() to get time in seconds."""
	start_time = time.time()
	time.sleep(2)
	end_time = time.time()
	print("Total time ", total_time - start_time)
