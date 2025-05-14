"""
Dank GIL bringt Threading bei CPU-bound Prozessen keinen Vorteil
"""

import time
import threading


def cpu_bound_task():
    count = 0
    for i in range(30**5):
        count += 1


# MIT THREADING
start = time.perf_counter()
t1 = threading.Thread(target=cpu_bound_task)
t2 = threading.Thread(target=cpu_bound_task)
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
