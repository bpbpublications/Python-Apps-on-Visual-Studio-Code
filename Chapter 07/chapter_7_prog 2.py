import time
import threading as th

def cal_square(list_num):
   print("CALCULATING SQUARE OF NUMBERS: ")
   for i in list_num:
      time.sleep(1) #wait for a second
      print('square: ', i**2)

def cal_cube(list_num):
   print("CALCULATING CUBE OF NUMBERS: ")
   for i in list_num:
      time.sleep(1) #wait for a second
      print('cube: ',i**3)

#Main calling
num = [0,5,10,15,20,25,30]
thread1 = th.Thread(target = cal_square,args=(num,))
thread2 = th.Thread(target = cal_cube,args=(num,))
# creating two threads here t1 & t2
thread1.start()
thread2.start()
# starting threads at the same time
thread1.join()  #making main thread to wait
thread2.join()  #making main thread to wait
print("I am from Main, expecting both the threads to have terminated by now")