import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='a'
)

# GENERATORS

# Even number generator from 0 to N
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

# Fibonacci generator to N
def fibonacci_up_to(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


# ITERATORS

# Iterator for reverse output of list elements
class ReverseListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.lst[self.index]

# Iterator for even numbers from 0 to N
class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current
        self.current += 2
        return result


# DECORATORS

# Decorator for logging arguments and results
def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Decorator for exception handling
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Exception in {func.__name__}: {e}", exc_info=True)
            return None
    return wrapper


# EXAMPLES

if __name__ == "__main__":
    print("Even number generator up to 20:")
    for num in even_numbers(20):
        print(num, end=" ")
    print("\n")

    print("Fibonacci generator up to 999:")
    for num in fibonacci_up_to(999):
        print(num, end=" ")
    print("\n")

    print("Iterator for a reverse list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:")
    for item in ReverseListIterator([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        print(item, end=" ")
    print("\n")

    print("Iterator of even numbers up to 50:")
    for number in EvenIterator(40):
        print(number, end=" ")
    print("\n")

    print("Logging decorator test:")
    @log_decorator
    def add(a, b):
        return a + b

    add(5, 3)
    print("Check 'app.log' for logged information.\n")

    print("Exception handling decorator test:")
    @exception_handler
    def divide(a, b):
        return a / b

    print("divide(10, 2):", divide(10, 2))  # OK
    print("divide(10, 2):", divide(10, 0))  # Division by zero
    print("Check 'app.log' for errors.\n")
