import threading
import time

# Without using a lock
counter = 0


def increment_counter():
    global counter
    local_counter = counter
    # simulate some processing
    time.sleep(0.1)
    local_counter += 1
    counter = local_counter


thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Counter without lock: {counter}")

# ------------------------------------------

# Using a lock to prevent data race
counter = 0
lock = threading.Lock()


def increment_counter_with_lock():
    global counter
    lock.acquire()
    try:
        local_counter = counter
        # simulate some processing
        time.sleep(0.1)
        local_counter += 1
        counter = local_counter
    finally:
        lock.release()


thread1 = threading.Thread(target=increment_counter_with_lock)
thread2 = threading.Thread(target=increment_counter_with_lock)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Counter with lock: {counter}")
