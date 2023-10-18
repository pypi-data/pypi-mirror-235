import threading

def SquareAndCube():
    t1 = threading.Thread(target = lambda x: print(f'Cube: {x**3}') , args=(5,))
    t2 = threading.Thread(target = lambda x: print(f'Square: {x**2}'), args=(5,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!!")

if __name__ == '__main__':
    SquareAndCube()
