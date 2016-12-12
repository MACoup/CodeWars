'''
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.
'''

def isValidWalk(walk):
    point = [0, 0]
    if len(walk) == 10:
        for w in walk:
            if w.lower() == 'n':
                point[1] += 1
            if w.lower() == 's':
                point[1] -= 1
            if w.lower() == 'w':
                point[0] -= 1
            if w.lower() == 'e':
                point[0] += 1
            print point
        if point == [0, 0]:
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    walk_lst = ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's']
    print isValidWalk(walk_lst)
