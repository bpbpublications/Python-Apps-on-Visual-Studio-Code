from queue import PriorityQueue
from random import random, randint
from threading import Thread
from time import sleep
# generates random numbers
def producer(pqueue):
    print('Producer method is running now')
    # generate value
    for i in range(10):
        # creating work: generating a random number
        value = random()
        # generating a priority
        priority = randint(1, 100)
        print(f"Value = {value} : Priority = {priority}")
        # create tuple with priority and value
        item = (priority, value)
        # adding to the priority queue
        pqueue.put(item)
    # wait for all items to be processed
    pqueue.join()
    # send sentinel value
    pqueue.put(None)
    print('Producer is completed')
# consume the work generated by producer
def consumer(pqueue):
    print('Consumer is now Running')
    # consuming the work
    while True:
        # get a unit of work
        item = pqueue.get()
        # check for stop
        if item is None:
            break
        # block
        sleep(item[1])
        # report

        print(f'\n ==> Consuming : {item}')
        # mark it as processed
        pqueue.task_done()
    # all done
    print('Consumer is completed')
# create the shared queue
pq = PriorityQueue()
# start the producer
producer = Thread(target=producer, args=(pq,))
producer.start()

# start the consumer
consumer = Thread(target=consumer, args=(pq,))
consumer.start()
producer.join()
consumer.join()