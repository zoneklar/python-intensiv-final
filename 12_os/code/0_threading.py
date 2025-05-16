"""
Threading in Python
"""

import time
import threading
from queue import Queue  # threadsafe queue


def fn(identifier: int, q: Queue):
    """Schlafende funktion."""
    print(f"I am {identifier}")
    time.sleep(2)  # blockiert den Thread
    print(f"I am {identifier}, i am finished")
    q.put(f"{identifier} ist fertig.")


if __name__ == "__main__":
    threads = []
    q = Queue()  # Kommunikation zwischen Threads

    for i in range(3):
        t = threading.Thread(target=fn, args=(i, q))
        t.start()
        threads.append(t)

    [t.join() for t in threads]
    print("Hier gehts weiter...")
    while not q.empty():
        print(q.get())
