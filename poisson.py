import math

def poisson(k, lam):
    return (math.exp(-lam) * (lam ** k)) / math.factorial(k)



# Assumption: testing that the inputs are valid means:
# 1. k is a natural number
# 2. lambda is strictly positive

# Either use try/except or write the following assumption:
#   Assumption: the user is assumed to input numbers only.

def main():
    k_string = input()
    lam_string = input()
    try:
        k = int(k_string)
        lam = float(lam_string)
        ok_numbers = True
    except:
        ok_numbers = False

    if ok_numbers and k >= 0 and lam > 0:
        print(poisson(k, lam))
    else:
        print("invalid parameters")

main()
