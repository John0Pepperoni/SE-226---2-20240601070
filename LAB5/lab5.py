#1
def factorial(x):
    if x == 1: return 1
    if x == 0: return 1

    return x * factorial(x-1)

print(factorial(5))

#2
abs_val = lambda x,i: ((x)**(2*i))/factorial(2*i)

def exp_n(x,n):
    S = 0
    for i in range(0, n):
        if i%2 == 0:
            S += abs_val(x,i)*(1)
        else:
            S += abs_val(x,i)*(-1)

    return S

print("Enter x: " )
x = int(input())
print("Enter n: " )
n = int(input())
print("Result: ", exp_n(x,n), "")

#3

Gn = 0
def calc_sum(r,n):
    """ This function calculates the sum of the series
    on the basis of r and n, and stores the result in global variable Gn"""

    global Gn
    if n < 0: return 1

    Gn = Gn + (r**n)
    calc_sum(r,n-1)
calc_sum(2,4)

print(Gn)