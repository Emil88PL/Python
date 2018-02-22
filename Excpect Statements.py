def div42by(divdeby):
    try:
        return 42 / divdeby
    except ZeroDivisionError: # no need to specify it will cach all types of error
        print('Error: You tried to devide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
