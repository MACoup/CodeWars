def double_char(s):
    new_s = []
    return ''.join([(l*2) for l in s])


if __name__ == '__main__':
    print double_char("String")
