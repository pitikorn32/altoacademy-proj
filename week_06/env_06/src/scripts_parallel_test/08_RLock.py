import threading

# Using Lock
lock = threading.Lock()


def factorial_with_lock(n):
    if n == 1:
        return 1

    # Acquiring the lock
    lock.acquire()

    # Recursively calling the function
    result = n * factorial_with_lock(n - 1)

    # Releasing the lock
    lock.release()

    return result


# Using RLock
rlock = threading.RLock()


def factorial_with_rlock(n):
    if n == 1:
        return 1

    # Acquiring the lock
    rlock.acquire()

    # Recursively calling the function
    result = n * factorial_with_rlock(n - 1)

    # Releasing the lock
    rlock.release()

    return result


# Testing
try:
    print("Using Lock:")
    print(factorial_with_lock(5))  # This will cause a deadlock
except RuntimeError as e:
    print("Error:", e)

print("\nUsing RLock:")
print(factorial_with_rlock(5))  # This will work properly
