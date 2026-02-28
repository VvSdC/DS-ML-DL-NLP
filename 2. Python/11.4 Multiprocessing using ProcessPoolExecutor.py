# Multiprocessing using ProcessPoolExecutor

'''
When to use ProcessPoolExecutor?

CPU-bound tasks (heavy computations, data processing, numerical simulations, image/video processing)

Each process has its own Python interpreter and memory space, bypassing the GIL. This allows true parallel execution on multiple CPU cores.
'''

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(2)
    return f"Square of {number} is {number**2}"


def multiprocessing(numbers):
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number,numbers)
    for result in results:
        print(result)

def sequential(numbers):
    for number in numbers:
        print(square_number(number))

if __name__ == "__main__":
    numbers = [1,2,3,4,5,6,7]

    print("Starting sequential execution ....")
    time1 = time.time()
    sequential(numbers)
    finished_time = time.time() - time1
    print(f"Sequential execution completed in {finished_time}") # Took around 14 seconds

    print("\nStarting execution using ProcessPoolExecutor ....")
    time2 = time.time()
    multiprocessing(numbers)
    finished_time = time.time() - time2
    print(f"Multiprocessing execution completed in : {finished_time}") # Took around 6.2 seconds