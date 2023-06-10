import threading


def function(i):
    print("function called by thread %i\n" % i)
    return


# Improved version
if __name__ == "__main__":
    num_threads = 20
    threads = []

    for i in range(500):
        t = threading.Thread(target=function, args=(i,))
        t.start()
        threads.append(t)

        # Wait for a certain number of threads to finish
        if len(threads) >= num_threads:
            for t in threads:
                t.join()
            threads = []

    # Wait for any remaining threads to finish
    for t in threads:
        t.join()
