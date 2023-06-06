def square(num):
    return num * num

square_lambda = lambda num: num * num

assert square(4) == square_lambda(4)
