import string

def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        for i in pin:
            if i not in string.digits:
                return False
                break
            else:
                continue
    else:
        return False
    return True


'''Other solutions'''

def validate_pin2(pin):
    return len(pin) in (4, 6) and pin.isdigit()



if __name__ == '__main__':
    print validate_pin('143')
    print validate_pin('1.23')
