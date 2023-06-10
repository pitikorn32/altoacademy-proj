import multiprocessing
import time


def run_fn():
    process_name = multiprocessing.current_process().name
    print(f"print from {process_name}")
    time.sleep(1)
    print(f"{process_name} end")


if __name__ == "__main__":
    p = multiprocessing.Process(
        name="Terminate-Process",
        target=run_fn,
    )
    print("start the process")

    p.start()
    print(f"start the process {p} status {p.is_alive()}")

    p.terminate()
    print(f"terminate the process {p} status {p.is_alive()}")

    p.join()
    print(f"join the process {p} status {p.is_alive()}")
