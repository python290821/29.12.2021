
# try - else
try:
    int1_safe = int(input('Enter number (i dont trust you): '))
except ValueError as e:
    print(e)
else:
    # out of try scope, but still execute finally after me ...............
    int2_unsafe = int(input('Enter number (i trust you): '))
    ################################
finally: # will always be executed
    print('thank you for your cooperation')










