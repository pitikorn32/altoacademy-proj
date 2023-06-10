import time
import threading
import multiprocessing
import math


# A heavy CPU-bound function - calculating factorial of a large number
def calculate_factorial(number):
    math.factorial(number)


# The large number for which factorial will be calculated
large_number = 20000
# The number of times the factorial will be calculated
n_calculations = 10


def main():
    # Sequential processing
    start_time = time.time()
    for _ in range(n_calculations):
        calculate_factorial(large_number)
    end_time = time.time()
    print("Sequential processing took: {:.6f} seconds".format(end_time - start_time))

    # ----------------------------------------

    # Multi-threading
    start_time = time.time()
    threads = []

    for _ in range(n_calculations):
        thread = threading.Thread(target=calculate_factorial, args=(large_number,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    print("Multi-threading took: {:.6f} seconds".format(end_time - start_time))

    # ----------------------------------------

    # Multi-processing
    start_time = time.time()
    processes = []

    for _ in range(n_calculations):
        process = multiprocessing.Process(
            target=calculate_factorial, args=(large_number,)
        )
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    end_time = time.time()
    print("Multi-processing took: {:.6f} seconds".format(end_time - start_time))


if __name__ == "__main__":
    main()
