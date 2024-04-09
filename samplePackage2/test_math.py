def add_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is: {result}")
    return result


def compare_numbers(a, b):
    if a > b:
        print(f"{a} is greater than {b}")
    elif a < b:
        print(f"{a} is less than {b}")
    else:
        print(f"{a} is equal to {b}")


def is_even(num):

    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is not an even number")




    # add_numbers(5, 10)
    # compare_numbers(8, 3)
    # is_even(7)
