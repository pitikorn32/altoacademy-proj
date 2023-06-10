import time
import threading
import multiprocessing


def square(numbers):
    for number in numbers:
        result = number * number


if __name__ == "__main__":
    # Create a dataset
    data = [i for i in range(100000000)]

    # Sequential Processing
    start_time = time.time()
    square(data)
    end_time = time.time()
    print("Sequential Processing took: {:.6f} seconds".format(end_time - start_time))

    # ----------------------------------------

    # Multi-threading
    start_time = time.time()
    thread1 = threading.Thread(target=square, args=(data[:500000],))
    thread2 = threading.Thread(target=square, args=(data[500000:],))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    end_time = time.time()
    print("Multi-threading took: {:.6f} seconds".format(end_time - start_time))

    # ----------------------------------------

    # Multi-processing
    start_time = time.time()
    process1 = multiprocessing.Process(target=square, args=(data[:500000],))
    process2 = multiprocessing.Process(target=square, args=(data[500000:],))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
    end_time = time.time()
    print("Multi-processing took: {:.6f} seconds".format(end_time - start_time))
