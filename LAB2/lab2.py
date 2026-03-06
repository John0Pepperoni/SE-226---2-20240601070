# Task 1
dsmvalue = None
dsmtemp = None

print("Please enter a positive integer greater than 9:")
dsmvalue = int(input())
while dsmvalue <= 9:
    print("Invalid input.Please enter a positive integer greater than 9:")
    dsmvalue = int(input())

dsmtemp = dsmvalue
print(str(dsmtemp), end=" ")
while dsmtemp > 9:
    dsmsum = 0
    while dsmtemp > 0:
        dsmsum = dsmsum + dsmtemp % 10
        dsmtemp = dsmtemp // 10

    dsmtemp = dsmsum
    print("-> " + str(dsmsum), end=" ")

print()

# Task 2
fbvalue = None
fbcount = 1
print("Please enter a positive integer between 1 and 100:")
fbvalue = int(input())
while fbvalue < 1 or fbvalue > 100:
    print("Invalid input. Please enter a positive integer between 1 and 100:")
    fbvalue = int(input())

fizzSteps = 0
buzzSteps = 0
fizzBuzzSteps = 0

while fbcount <= fbvalue:
    if fbcount % 7 == 0:
        print("(" + str(fbcount) + " is skipped)")
        fbcount+=1
        continue

    if fbcount % 3 == 0:
        if fbcount % 5 == 0:
            print("FizzBuzz")
            fizzBuzzSteps += 1
        else:
            print("Fizz")
            fizzSteps += 1
    elif fbcount % 5 == 0:
        print("Buzz")
        buzzSteps += 1
    else:
        print(fbcount)

    fbcount+=1

print("----- Summary -----")
print("Fizz count: " + str(fizzSteps))
print("Buzz count: " + str(buzzSteps))
print("FizzBuzz count: " + str(fizzBuzzSteps))

print()


# Task 3

pat = None
print("Please enter a number between 3 and 9:")
pat = int(input())
while pat < 3 or pat > 9:
    print("Invalid input. Please enter a number between 3 and 9:")
    pat = int(input())

i = 1
while i <= 2*pat-1:
    k = pat - abs(pat-i)
    for j in range(1, k+1):
        print(j, end="")
    print()
    i+=1
    if i < 1:
        break


