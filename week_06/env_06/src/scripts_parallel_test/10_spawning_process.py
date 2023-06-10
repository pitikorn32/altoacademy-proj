import multiprocessing


def run_fn(i):
    print(f"called function in process: {i}")


if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=run_fn, args=(i,))
        processes.append(p)
        p.start()
        p.join()
