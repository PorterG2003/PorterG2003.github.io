def delQ(W):
    return W

def GradDesc(W, v):
    for i in range(2):
        W[i] = W[i] - v*delQ(W)[i]
    return W

def check(W):
    for i in delQ(W):
        if i < -0.0001 or i > 0.0001:
            return True
    return False

def main():
    W = [1, 0]
    v = 0.01
    i = 0
    while check(W):
        W = GradDesc(W, v)
        print(W)
        i += 1
        print(i)

main()
