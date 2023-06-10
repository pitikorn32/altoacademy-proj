# Naming a Process
import multiprocessing
import time


def foo():
    # if process child wants to know which is the parent process, it must use this statement
    name = multiprocessing.current_process().name
    print("Starting %s \n" % name)
    time.sleep(3)
    print("Exiting %s \n" % name)


if __name__ == "__main__":
    process_with_name = multiprocessing.Process(name="foo_process", target=foo)
    process_with_name.daemon = True
    process_with_default_name = multiprocessing.Process(target=foo)
    process_with_name.start()
    process_with_default_name.start()
    process_with_name.join()
    process_with_default_name.join()
