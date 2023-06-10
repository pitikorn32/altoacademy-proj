import multiprocessing


class MyProcess(multiprocessing.Process):
    def run(self):
        print(f"called run method in {self.name}")


if __name__ == "__main__":
    process = []

    for i in range(5):
        p = MyProcess()
        process.append(p)
        p.start()
        p.join()
