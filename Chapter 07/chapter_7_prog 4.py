import threading as thread
import time

global val #Shared value
val = 0
lock = thread.Lock()    #Lock for synchronising access

def Reader():
    global val
    lock.acquire()  # Acquire lock before Reading
    time.sleep(0.2)
    print('Reader is Reading Shared Value: val=', val)
    lock.release()  # Release the lock before Reading

def Writer():
    global val
    lock.acquire()  # Acquire the lock before Writing
    print('Writer is increasing value of val by 1!')
    time.sleep(0.2)
    val += 1              #Write on the shared value
    print('Writing done: val =',val)
    lock.release()  # Release the lock after Writing
    print()


#Driver code
if __name__ == '__main__':
    for i in range(0, 10):
        ThreadA = thread.Thread(target = Reader)
        ThreadA.start()
        ThreadB = thread.Thread(target = Writer)
        ThreadB.start()

ThreadA.join()
ThreadB.join()