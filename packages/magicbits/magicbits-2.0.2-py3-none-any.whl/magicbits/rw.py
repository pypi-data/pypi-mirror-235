import threading
readers = 0
mutex = threading.Semaphore(1)
resource = threading.Semaphore(1)
read_try = threading.Semaphore(1) # It is a semaphore,used to (only one at a time)

def reader():
    global readers
    read_try.acquire()
    mutex.acquire()
    readers+=1
    if readers == 1:
        resource.acquire()
    mutex.release()
    read_try.release()
    print("Reading resources .....")
    mutex.acquire()
    readers-=1
    if readers == 0 :
        resource.release()
    mutex.release()

def writer ():
    resource.acquire()
    print("Writing Resource....") 
    resource.release()


if __name__ == '__main__':
    readers_thread = []
    writer_thread = [] 

    for _i in range(3):
        readers_thread.append(threading.Thread(target=reader))
        writer_thread.append(threading.Thread(target=writer))
    for t in readers_thread + writer_thread:
        t.start()
    for t in readers_thread + writer_thread:
        t.join()

    print("All readers and writers are done.")        
