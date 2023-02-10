
def merge_numbers(a, b):
    a_ones = a % 10
    a_tens = a // 10
    b_ones = b % 10
    b_tens = b // 10
    return a_tens * 1000 + a_ones * 100 + b_tens * 10 + b_ones