import threading

def print_square(number):
    print(f'Cube {number * number}')

def print_cube(number):
    print(f'Cube {number * number * number}')

if __name__ == '__main__':
    t1 = threading.Thread(target = print_square, args = (10,))
    t2 = threading.Thread(target = print_cube, args = (10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
