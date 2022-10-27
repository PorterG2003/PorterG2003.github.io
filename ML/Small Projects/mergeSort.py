from random import randint

def makeList():
    lst = []
    print("Enter in the values of your list. Press enter to get to the next value.")
    print("When you have entered all values in your list, ")
    print("go to the next value, leave it blank, then press enter.")
    print()
    incheck = 0
    i = 0
    while incheck == 0:
        ii = ""
        if i >= 10:
            if i < 20 or i > 22:
                ii = str(i + 1) + "th"
            elif i % 10 == 0:
                ii = str(i + 1) + "st"
            elif i % 10 == 1:
                ii = str(i + 1) + "nd"
            elif i % 10 == 2:
                ii = str(i + 1) + "rd"
        elif i == 0:
            ii = "1st"
        elif i == 1:
            ii = "2nd"
        elif i == 2:
            ii = "3rd"
        else:
            ii = str(i + 1) + "th"
        newInput = input("Enter the " + ii + " number: ")
        if newInput == "":
            incheck = 1
        elif newInput.isdigit():
            lst.append(newInput)
            i += 1
        else:
            print("That's not a number!")
    print()
    print()
    print("Your list is: " + str(lst))
    print()
    return lst

def mergeSort(lst):
    lst = [[i] for i in lst]
    print(lst)
    while len(lst) > 1:
        for i in lst:
            c = 0
            if lst.index(i) == len(lst)-1:
                k = lst[lst.index(i)-1]
            else:
                k = lst[lst.index(i)+1]
            while len(k) > 0:
                if c == len(i):
                    i.append(k.pop(0))
                elif i[c] > k[0]:
                    i.insert(c, k.pop(0))
                    c += 1
                else:
                    c += 1

            lst.remove(k)
    return lst

def main():
    print()
    print(mergeSort([randint(-1000,1000) for i in range(100000)]))

main()
