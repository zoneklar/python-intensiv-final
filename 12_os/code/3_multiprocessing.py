"""
Mehrere Prozesse parallel laufen lassen.
"""

import os
import time
import multiprocessing


def cpu_bound_task():
    print("Prozess ID:", os.getpid())
    count = 0
    for _ in range(30**5):
        count += 1


if __name__ == "__main__":

    # MIT Multiprocessing
    start = time.perf_counter()
    t1 = multiprocessing.Process(target=cpu_bound_task)
    t2 = multiprocessing.Process(target=cpu_bound_task)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end = time.perf_counter()

    print(f"Hat gedauert: {end - start: .2f}")

    # OHNE THREADING
    start = time.perf_counter()
    cpu_bound_task()
    cpu_bound_task()
    end = time.perf_counter()
    print(f"Hat gedauert: {end - start: .2f}")
