class Heap:
    def __init__(self):
        # initialize Heap array
        self.heap_array = []

    def display_heap(self):
        #Display the content in 1-D array format
        print(self.heap_array)

    def parent(self, i):
        #formula to get access to the parent
        return (i - 1) // 2

    def insert(self, k):
        self.heap_array.append(k)
        i = len(self.heap_array) - 1
        self.fix_up(i) #move up if required
        #display
        self.display_heap()

    def fix_up(self, i):
        p = self.parent(i)
        #if parent is lower than the child's value then swap
        while p >= 0 and self.heap_array[p] < self.heap_array[i]:
            self.heap_array[p], self.heap_array[i] = self.heap_array[i], self.heap_array[p]
            i = p
            p = self.parent(i)

    def fix_down(self, i):
        '''
        heapify the subtree to manage delete
        :param i: root with node i
        :return: 
        '''
        left = 2 * i + 1 #access to left child
        right = 2 * i + 2 #access to right child
        largest = i
        # If left child is larger than root
        if left < len(self.heap_array) and self.heap_array[left] > self.heap_array[i]:
            largest = left
        # If right child is larger than largest so far
        if right < len(self.heap_array) and self.heap_array[right] > self.heap_array[largest]:
            largest = right
        # If largest is not root
        if largest != i:
            self.heap_array[i], self.heap_array[largest] = self.heap_array[largest], self.heap_array[i]
            self.fix_down(largest)

    def delete(self, i):
        #deleting element at ith position
        n = len(self.heap_array)
        if n == 0:
            return None
        self.heap_array[i], self.heap_array[n - 1] = self.heap_array[n - 1], self.heap_array[i]
        del self.heap_array[n - 1]
        self.fix_down(i)
        self.fix_up(i)
        # display
        self.display_heap()
#Testing the above code
h1=Heap()
h1.insert(50)  #Run 1: [50]
h1.insert(10)  #Run 2: [50, 10]
h1.insert(30)  #Run 3: [50, 10, 30]
h1.delete(1)  #Run 4: [50, 30]
h1.insert(20)  #Run 5: [50, 30, 20]
h1.insert(80)  #Run 6: [80, 50, 20, 30]
h1.delete(2)  #Run 7: [80, 50, 30]
h1.insert(70)  #Run 8: [80, 70, 30, 50]