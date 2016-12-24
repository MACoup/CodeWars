def get_middle(s):
    if len(s) > 2:
        if len(s) % 2 != 0:
            return s[(len(s)-1)/2]
        else:
            return s[(len(s)/2) -1:(len(s)/2)+1]
    else:
        return s

if __name__ == '__main__':
    print get_middle("test")
    print get_middle('testing')
    print get_middle('middle')
    print get_middle('A')
    print get_middle('of')
