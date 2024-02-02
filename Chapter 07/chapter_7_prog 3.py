
import threading as thread
import time

global val #Shared value
val = 0

def Reader():
    global val
    time.sleep(0.2)
    print('Reader is Reading Shared Value: val=', val)

def Writer():
    global val
    print('Writer is increasing value of val by 1!')
    time.sleep(0.2)
    val += 1              #Write on the shared value
    print('Writing done: val =',val)
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