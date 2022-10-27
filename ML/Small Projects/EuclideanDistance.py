import math

#formats points into lists
def point2list(point):
    newnum = ""
    temporary = []
    for char in point:
        if char.isdigit():
            newnum += char
        elif len(newnum) != 0:
            temporary.append(int(newnum))
            newnum = ""
    return temporary

#puts the inputs into the formula
def EuclideanDistance(point1, point2, dimensions):
    i = 0
    for x in range(dimensions):
        i += (point1[x] - point2[x]) ** 2
    return str(math.sqrt(i))

def main():
    print()
    print("Welcome to the Euclidean Distance Program!")
    print()
    dimensions = int(input("Enter the amount of dimensions: "))
    units = input("Enter the units you are using: ")
    print()
    point1 = input("Enter the location of the first point: ") + "."
    point2 = input("Enter the location of the second point: ") + "."

    point1 = point2list(point1)
    point2 = point2list(point2)

    print()
    print("The distance between your points is", EuclideanDistance(point1, point2, dimensions) + units + ".")

main()
