def spin_words(string):
    words = string.split()
    new_l = []
    for word in words:
        if len(word) >= 5:
            word = word[::-1]
        new_l.append(word)
    return ' '.join([word for word in new_l])

if __name__ == '__main__':
    print spin_words("Welcome")
