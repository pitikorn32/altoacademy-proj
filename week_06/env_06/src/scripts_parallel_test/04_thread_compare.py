import time
import threading
import multiprocessing
import requests


# A dummy function that simulates downloading data from a URL
def download_from_url(url):
    _ = requests.get(url)


# List of example urls to download
urls = ["https://google.com" for _ in range(20)]


def main():
    # Sequential processing
    start_time = time.time()
    for url in urls:
        download_from_url(url)
    end_time = time.time()
    print("Sequential processing took: {:.6f} seconds".format(end_time - start_time))

    # ----------------------------------------

    # Multi-threading
    start_time = time.time()
    threads = []

    for url in urls:
        thread = threading.Thread(target=download_from_url, args=(url,))
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

    for url in urls:
        process = multiprocessing.Process(target=download_from_url, args=(url,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    end_time = time.time()
    print("Multi-processing took: {:.6f} seconds".format(end_time - start_time))


if __name__ == "__main__":
    main()
