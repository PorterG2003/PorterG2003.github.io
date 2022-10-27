
def updateW(w, y, x, k):
    for i in range(len(x)):
        w[i] = w[i] + y * x[i]
    return w

def updateB(b, y, k):
    return b + y

def indicator(w, x, y, b, k):
    y2 = 0
    for i in range(len(x)):
        y2 += x[i] * w[i]
    y2 += b
    if y > 0 and y2 < 0:
        return True
    if y < 0 and y2 > 0:
        return True
    if (y == 0 ) != (y2 == 0):
        return True
    else:
        return False

def main():
    k = 0

    b = 0
    w = [0, 0]
    x = [[-1, 1], [0, -1], [10,1]]
    y = [1, -1, 1]
    while(indicator(w, x[k], y[k], b, k)):
        for g in range(len(x)):
            if indicator(w, x[k], y[k], b, k):
                print(".")
                w = updateW(w, y[k], x[k], k)
                b = updateB(b, y[k], k)
                k += 1
        k = 0
    print("w = " + str(w))
    print("b = " + str(b))

main()
