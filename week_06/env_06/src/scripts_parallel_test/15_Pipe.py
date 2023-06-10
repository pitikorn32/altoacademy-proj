import multiprocessing
from time import time
from datetime import datetime
from multiprocessing import Barrier, Lock


def create_items(pipe):
    output_pipe, _ = pipe
    for item in range(10):
        output_pipe.send(item)
    output_pipe.close()


def multiply_items(pipe1, pipe2):
    close, input_pipe = pipe1
    close.close()
    output_pipe, _ = pipe2
    try:
        while True:
            item = input_pipe.recv()
            output_pipe.send(item * item)
    except EOFError:
        output_pipe.close()


if __name__ == "__main__":
    pipe1 = multiprocessing.Pipe(True)
    pipe2 = multiprocessing.Pipe(True)

    process1 = multiprocessing.Process(target=create_items, args=(pipe1,))
    process2 = multiprocessing.Process(target=multiply_items, args=(pipe1, pipe2))

    process1.start()
    process2.start()

    pipe1[0].close()
    pipe2[0].close()

    try:
        while True:
            print(pipe2[1].recv())
    except:
        pass
