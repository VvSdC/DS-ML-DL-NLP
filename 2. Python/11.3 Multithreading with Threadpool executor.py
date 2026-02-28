# Multi threading using thread pool executor

'''
When to use ThreadPoolExecutor?

I/O-bound tasks (network requests, file I/O, database queries, waiting on APIs)

Threads share memory within the same process, so they're lightweight. The Global Interpreter Lock (GIL) doesn't block I/O operations, making threads efficient for tasks that spend time waiting.
'''

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
    time.sleep(1)
    return f"Number : {number}"

def multithreading(numbers):
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_numbers,numbers)
    for result in results:
        print(result)

def sequential(numbers):
    for number in numbers:
        print(print_numbers(number))

if __name__ == '__main__':
    numbers = [1,2,3,4,5]

    time1 = time.time()
    print("Starting sequential execution ....")
    sequential(numbers)
    finished_time = time.time() - time1
    print(f"Sequential execution completed in : {finished_time}") # Took 5 seconds

    time2 = time.time()
    print("Starting execution using ThreadPoolExecutor ....")
    multithreading(numbers)
    finished_time = time.time() - time2
    print(f"ThreadPoolExecutor execution took : {finished_time}") # Took 2 seconds

