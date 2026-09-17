
def naturals_from_two():
    n = 2
    while True:
        yield n
        n = n + 1

def some_divides(primes, i):
    for p in primes:
        if  i % p == 0: # i is divisible by p
            return True
    return False

def primes():
    found_primes = []
    for i in naturals_from_two():
        if some_divides(found_primes, i):
            pass
        else:
          found_primes.append(i)
          yield i

for i in primes():
    print (i)


    # def every_other(generator):
    # flag = True
    # for n in generator:
    #     flag = not flag
    #     if flag:
    #         yield n

