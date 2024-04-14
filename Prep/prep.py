### Tiago Gomes - COP1000 #1284
### Chapter 7 Prep Assignment
###


import random


def main () :

    pyList = []
    for i in range(0,12) :
        n = random.randint(50,100)
        pyList.append(n)

    print("Here is the list of random integers...")

    for n in pyList :
        print(n, end=" ")

    print('\n')
    
    print(f'The 4th element in the list is {pyList[3]}')
    print(f'The element at index 9 is {pyList[9]}')
    print(f'The smallest element in the list is {min(pyList)}')
       
    sortedList = change_list(pyList)
    
    print(f'change_list has returned this sorted list...')

    for n in sortedList :
        print(n, end=" ")
    
def change_list (pyList) :
    newList = pyList[3:9]

    print(f'The size of the list is now {len(newList)}')

    newList.sort()
    return newList


if __name__ == '__main__':
    main()

    
