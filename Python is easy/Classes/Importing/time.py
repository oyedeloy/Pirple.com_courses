import time

current_time = time.process_time()
print("hello")
past_time = time.process_time()
print(current_time)
print(past_time - current_time)
