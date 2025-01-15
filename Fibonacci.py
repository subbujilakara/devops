class Fibonacci:
    def __init__(self):
        self.prev = 0  
        self.curr = 1  
        self.sum_even_fibs = 0
        self.even_fib_count = 0

    def next_fibonacci(self):
        
        next_fib = self.prev + self.curr
        self.prev = self.curr
        self.curr = next_fib
        return next_fib

    def sum_even_fibonacci(self, limit):
        
        while self.even_fib_count < limit:
            fib = self.next_fibonacci()
            if fib % 2 == 0:
                self.sum_even_fibs += fib
                self.even_fib_count += 1
        return self.sum_even_fibs


def main():
    fib = Fibonacci()
    even_fib_sum = fib.sum_even_fibonacci(100)
    print(f"The sum of the first 100 even Fibonacci numbers is: {even_fib_sum}")


if __name__ == "__main__":
    main()


The sum of the first 100 even Fibonacci numbers is: 18604921145
