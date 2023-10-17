import threading

def fibonacci(n):
    fib_sequence = [0,1]
    for i in range(2,n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    print("Fibonacci sequence of length n is : " , fib_sequence)

def main():
    ft=threading.Thread(target=fibonacci,args=(10,))
    ft.start()
    ft.join()
    print("Calculation finished!!")

if __name__ == '__main__' :
    main()
