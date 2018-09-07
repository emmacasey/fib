def nextFib(a,b):
  return a+b

def evenFibCalculator(n):
    assert type(n) == int, "requires integer input"
    a=0
    b=1
    count=0
    for i in range(2,n):
        next_fib=nextFib(a,b)
        if next_fib % 2 ==0:
            count+=next_fib
        a=b
        b=next_fib

    return count

def evenFibLimitCalculator(n):
    assert type(n) == int, "requires integer input"
    a=0
    b=1
    count=0
    while nextFib(a,b) < n:
        next_fib=nextFib(a,b)
        if next_fib % 2 ==0:
            count+=next_fib
        a=b
        b=next_fib

    return count

def testevenFibCalculator():
    assert evenFibCalculator(7) == 10
    assert evenFibCalculator(10) == 44

def testevenFibLimitCalculator():
    assert evenFibLimitCalculator(13) == 10
    assert evenFibLimitCalculator(35) == 44


testevenFibLimitCalculator()
testevenFibCalculator()
print("done")
