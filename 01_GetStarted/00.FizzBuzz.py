number = range(1,100)
# here 3 is Fizz and 5 is buzz

for x in number:
    if(x%15==0): # Divisible to 3 and 5
        print(f"{x} Fizz Buzz")
    elif (x%3==0):
        print(f"{x} fizz")
        continue
    elif (x%5==0):
        print(f"{x} Buzz")
        continue
    else:
        print(x)