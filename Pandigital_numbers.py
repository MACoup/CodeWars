'''
Avoid WHILE loops unless absolutely required!!!!
'''


def pow_root_pandigit(val, n, k):
    '''
    The number 169, is the first pandigital square, higher than 100, having its square root, 13, pandigital too.

    The number 1728 is the first pandigital cubic, higher than 1000, having its cubic root, 12, pandigital too.

    Make the function pow_root_pandigit(), that receives three arguments:

    a minimum number, val
    the exponent of the n-perfect powers to search, n
    k, maximum amount of terms that we want in the output
    The function should output a 2D-array with an amount of k pairs of numbers(or an array of an only pair if we have this case). Each pair has a nth-perfect power pandigital higher than val with its respective nth-root that is pandigital, too.
    '''
    pair_lst = []
    for num in xrange(int(val**(1./n)), val):
        if len(pair_lst) == k:
            break
        if is_pandigit(num) == True:
            power_num = num**n
            if power_num > val and is_pandigit(power_num) == True:
                pair_lst.append([num, power_num])
            else:
                continue
        else:
            continue
    return pair_lst

def is_pandigit(num):
    '''
        A pandigital number is one that has its digits from 1 to 9 occuring only once (they do not have the digit 0).
    '''
    num_lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for n in str(num):
        if str(n) not in num_lst:
            return False
        elif str(num).count(str(n)) > 1:
            return False
        else:
            continue
    return True

if __name__ == '__main__':
    print pow_root_pandigit(1750, 3, 5)
