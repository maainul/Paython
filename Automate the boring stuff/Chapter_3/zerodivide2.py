def spam(divideby):
    try:
        return 42/divideby
    except ZeroDivisionError:
        print('Error.Invalid Argument')
print(spam(12))
print(spam(0))
print(spam(1))
