'''
### Implementing multi-processing

When to use multi-processing?
- CPU bound tasks (heavy CPU usage like data processing etc)
- Parallel execution (Using multiple cores of CPU)
'''

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        print(f"Square of {i} is {i*i}")
        time.sleep(1.5)  # Simulate heavy work

def cube_numbers():
    for i in range(5):
        print(f"Cube of {i} is {i*i*i}")
        time.sleep(1)  # Simulate heavy work

def run_sequential():
    print("\n--- Sequential Execution ---")
    t = time.time()
    square_numbers()
    cube_numbers()
    finished = time.time() - t
    print(f"Sequential time: {finished:.2f} seconds")

def run_multiprocessing():
    print("\n--- Multiprocessing Execution ---")
    t = time.time()
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    finished = time.time() - t
    print(f"Multiprocessing time: {finished:.2f} seconds")

if __name__ == "__main__":
    run_sequential()  # Took around 12.5 seconds
    run_multiprocessing() # Took around 7.64 seconds