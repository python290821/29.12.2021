

#a = int(input('enter number:'))

# try except [catch] finally
def get_int(msg):
    while True:
        try:
            return int(input(msg))
            #if a < 0:
                #raise ValueError('cannot insert negative')
        except LookupError: # tel aviv
            #print(e)
            print('wrong input. please enter int')
        except ValueError: # ramat gan
            print('value error')
        except: # Israel
            print('unknown error')

print('wallllaaaaaaaaaaaa')
int1 = get_int('Please enter first number: ')
int2 = get_int('Please enter second number: ')