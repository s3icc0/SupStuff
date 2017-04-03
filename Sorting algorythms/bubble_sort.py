# Bubble sort function

def bubblesort(list):
    i = len(list) - 1

    while i > 0:
        j = 0
        while j < i:
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
            else:
                j += 1
            for k in list:
                print(k, end=', ')
        i -= 1

    for k in list:
        print(k, end=', ')


# function defined in case we need to see the output for debugging purposes
def bubblesortdebug(list):
    i = len(list) - 1

    while i > 0:
        j = 0
        while j < i:
            print('\nIs {} > {}'.format(list[j], list[j + 1]))
            if list[j] > list[j + 1]:
                print('Switch')
                list[j], list[j + 1] = list[j + 1], list[j]
            else:
                print('Don\'t Switch')
            j += 1
            for k in list:
                print(k, end=', ')
            print()
        print('END OF ROUND')
        i -= 1

    print()
    for k in list:
        print(k, end=', ')
    print()
