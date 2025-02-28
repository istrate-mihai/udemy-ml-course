from multiprocessing import Process
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'Square {i * i}')

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f'Cube: {i * i * i}')

if __name__ == '__name__':
    p1 = Process(target = square_numbers)
    p2 = Process(target = cube_numbers)
    t = time.time()

    # start the process
    p1.start()
    p2.start()

    # wait for the process to complete
    p1.join()
    p2.join()

    finished_time = t - time.time()
    print(finished_time)
