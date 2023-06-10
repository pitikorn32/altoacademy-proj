import threading


def function(i):
    print("function called by thread %i\n" % i)
    return


if __name__ == "__main__":
    threads = []
    num_threads = 20
    for idx, i in enumerate(range(500)):
        t = threading.Thread(target=function, args=(i,))
        threads.append(t)

        # Start threads and wait for all to finish
        if (idx + 1) % num_threads == 0:
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            threads = []
