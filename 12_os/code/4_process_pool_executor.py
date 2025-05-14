from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Queue, Pipe


def fn(a, b):
    return a + b


if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        r = executor.map(fn, range(10), range(10))
        print(list(r))
