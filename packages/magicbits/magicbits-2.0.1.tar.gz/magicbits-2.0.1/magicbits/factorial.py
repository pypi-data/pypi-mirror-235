import threading

def factorial(n):
    if n<=1 :
        return 1
    result = n * factorial(n-1)
    print(result)
    return result
def main():
    print("Starting factorial calculation ....")
    t = threading.Thread(target = factorial , args=(4,))
    t.start()
    t.join()
    print("Calculation ended successfully!!")

if __name__ == '__main__':
    main()
