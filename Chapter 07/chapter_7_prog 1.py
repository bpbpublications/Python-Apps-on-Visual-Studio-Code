import threading

def thread_action():
    for x in range(5):
        print("Run by Child Thread...")

thread1 = threading.Thread(target=thread_action)
thread1.start()
#thread1.join()
print("Main Program Thread Here!")