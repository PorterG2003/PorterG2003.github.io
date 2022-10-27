import random
def main():
    print()

    #makes the list with user input
    lst = []
    print("Enter in the values of your array. When you have entered all values in your array, ")
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
    lst = [(i+1)/(i+1)*random.randint(0, 1000) for i in range(16384)]
    print("Your unsorted array is: " + str(lst))
    input()

    #time to sort
    y = 0
    while y == 0:
        x = 0
        for i in range(len(lst) - 1):
            first = int(lst[i])
            second = int(lst[i + 1])
            if first > second:
                x += 1
                lst.insert(i + 1, lst.pop(i))
                #uncomment lines 54 and 55 to see it sort in real time
                #print(lst)
        #print()
        if x == 0:
            y = 1
    print("Your sorted array is: " + str(lst))

main()
