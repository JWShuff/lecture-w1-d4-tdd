# return a list object
# should contain 100 elements
# "Fizz" output for multiples of 3
# "Buzz" output for multiple of 5
# "Fizzbuzz" for multiples of both 3 and 5
# otherwise output the number

# loop though number `1-100`
# determine output
# add output to list
# finally, return list

import time

def fizz_buzz():
    return fizz_buzz_N(100)

def fizz_buzz_N(N):
    return blah_yah_generic_N(N, "Fizz", "Buzz", "Fizzbuzz")

def blah_yah_generic_N(N, 
    multiple_of_three_output, 
    multiple_of_five_output, 
    multiple_of_both_output):
    
    fizz_buzz_list = []
    # populating our list with 100 items
    for n in range(1, N+1):
        if n % 3 == 0 and n % 5 == 0:
            fizz_buzz_list.append(multiple_of_both_output)
        elif n % 3 == 0:
            fizz_buzz_list.append(multiple_of_three_output)
        elif n % 5 == 0:
            fizz_buzz_list.append(multiple_of_five_output)
        else:
            fizz_buzz_list.append(n)

    # return list
    return fizz_buzz_list
