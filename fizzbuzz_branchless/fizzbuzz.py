import timeit

def branchlessfizzbuzz(value):
    if value == 0:
        return
    for count in range(value):
        ...
        print(
            str(count)*bool((count%3) * (count%5))
            +"fizz"*bool(not(count%3))
            +"buzz"*bool(not(count%5))
            )

def fizzbuzz_recursive(n):
    if n == 0:
        return
    fizzbuzz_recursive(n - 1)
    if n % 3 == 0 and n % 5 == 0:
        ...
        print('FizzBuzz')
    elif n % 3 == 0:
        ...
        print('Fizz')
    elif n % 5 == 0:
        ...
        print('Buzz')
    else:
        ...
        print(n)

def fizzbuzz_norm(n):
    if n == 0:
        return
    for count in range(n):
        if count % 3 == 0 and count % 5 == 0:
            ...
            print('FizzBuzz')
        elif count % 3 == 0:
            ...
            print('Fizz')
        elif count % 5 == 0:
            ...
            print('Buzz')
        else:
            ...
            print(count)

# Recursion has a depth limit of 994 in python.
# The recursion segment should be commmented out for testing hirgher values
starttime_norm = timeit.default_timer()
fizzbuzz_norm(994)
endtime_norm = timeit.default_timer()

starttime_br = timeit.default_timer()
branchlessfizzbuzz(994)
endtime_br = timeit.default_timer()

starttime_rec = timeit.default_timer()
fizzbuzz_recursive(994)
endtime_rec = timeit.default_timer()


print(f"The time for norm is {endtime_norm - starttime_norm}")
print(f"The time for branchless is {endtime_br - starttime_br}")
print(f"The time for recursive is {endtime_rec - starttime_rec}")