class MyFizzBuzz:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def run(self):
        for value in range(self.start, self.end + 1):
            if value % 3 == 0 and value % 5 == 0:
                print("FizzBuzz")
            elif value % 3 == 0:
                print("Fizz")
            elif value % 5 == 0:
                print("Buzz")
            else:
                print(value)

fb = MyFizzBuzz(1, 100)
fb.run()