import Iterator
import Generator
# 1. Создайте итератор (обьект класса), который будет возвращать числа фибоначчи
my_iter = Iterator.Iterator(10)

for i in my_iter:
    print(i)
print("*" * 100)

# 2. Создайте генератор (функцию), который будет возвращать числа фибоначчи
my_generator = Generator.Fibonacci_Generator(10)

for i in my_generator:
    print(i)
print("*" * 100)