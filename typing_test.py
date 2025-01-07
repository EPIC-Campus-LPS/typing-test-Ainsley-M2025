import time

print("Type as fast as you can.")

timer_start = time.time()

typing = input("Type here:")

timer_finish = time.time()

calcamalations = timer_finish - timer_start

print(f"\nYou took {calcamalations: .2f}")
