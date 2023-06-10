import multiprocessing


def worker_function(number):
    print(
        f"Number {number} processed by Process id: {multiprocessing.current_process().pid}"
    )


def main():
    # Numbers to be processed
    numbers = range(0, 100)

    # Create a multiprocessing Pool
    pool = multiprocessing.Pool(processes=2)

    # Map numbers to the worker_function
    pool.map(worker_function, numbers)

    # Map numbers to the worker_function in parallel (order not guaranteed)
    # - faster than map function above (ordered)
    # - but not guaranteed to be in order
    # pool.imap(worker_function, numbers)
    # pool.imap_unordered(worker_function, numbers)

    # .map(func, iterable): This method applies the function func to each item in the iterable
    # and returns the results in the same order as the input.
    # It blocks until all tasks are completed and returns a list containing the results.
    # The order of the results corresponds to the order of the input items.

    # .imap(func, iterable): This method is similar to .map(),
    # but it returns an iterator that yields the results as they become available.
    # It doesn't block until all tasks are completed and doesn't return a list immediately.
    # Instead, you can iterate over the returned iterator to process the results incrementally as they are produced.
    # The order of the results corresponds to the order of the input items.

    # .imap_unordered(func, iterable): This method is also similar to .map(),
    # but it returns an iterator that yields the results as they become available,
    # without preserving the order of the input items.
    # The order of the results is determined by the order of completion of the tasks, which may vary.
    # It allows you to process the results incrementally,
    # similar to .imap(), but without strict ordering guarantees.

    # Close the pool
    pool.close()

    # Wait for all processes to finish
    pool.join()


if __name__ == "__main__":
    main()
