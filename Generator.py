def Fibonacci_Generator(limit):
    Fibonacci = [1, 1]
    val = 1
    print("Create Generator:")
    print(f"Start {val} -->{Fibonacci}")
    while val < limit:
        Fibonacci.append(Fibonacci[val] + Fibonacci[val - 1])
        val += 1
        yield f"Next  {val} -->{Fibonacci}"


