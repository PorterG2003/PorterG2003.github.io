import numpy as np
from scipy import optimize

class Neural_Network(object):
    def __init__(self, Lambda=0):
        #Define HyperParameters
        self.inputLayerSize = 2
        self.outputLayerSize = 1
        self.hiddenLayerSize = 3

        #Weights (Parameters)
        self.W1 = np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize, self.outputLayerSize)

        #Regularization Parameter:
        self.Lambda = Lambda

    def forward(self, X):
        #Propagate inputs through network
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3)
        return yHat

    def sigmoid(self, z):
        #Apply sigmoid activation function
        return 1/(1+np.exp(-z))

    def sigmoidPrime(self, z):
        #Derivative of Sigmoid function
        return np.exp(-z)/((1+np.exp(-z))**2)

    def costFunction(self, X, y):
        #Compute cost for given X,y, use weights already stored in class.
        self.yHat = self.forward(X)
        J = 0.5*sum((y-self.yHat)**2)/X.shape[0] + (self.Lambda/2) * (sum(self.W1**2)+sum(self.W2**2))
        return J

    def costFunctionPrime(self, X, y):
        #Compute derivative with respect to W1 and W2
        self.yHat = self.forward(X)

        delta3 = np.multiply(-(y-self.yHat), self.sigmoidPrime(self.z3))
        dJdW2 = np.dot(self.a2.T, delta3)/X.shape[0] + self.Lambda*self.W2

        delta2 = np.dot(delta3, self.W2.T)*self.sigmoidPrime(self.z2)
        dJdW1 = np.dot(X.T, delta2)/X.shape[0] + self.Lambda*self.W1

        return dJdW1, dJdW2

    def getParams(self):
        #Get W1 andW3 Rolled into vector:
        params = np.concatenate((self.W1.ravel(), self.W2.ravel()))
        return params

    def setParams(self, params):
        #Set W1 and W2 using single parameter vector:
        W1_start = 0
        W1_end = self.hiddenLayerSize*self.inputLayerSize
        self.W1 = np.reshape(params[W1_start:W1_end], (self.inputLayerSize, self.hiddenLayerSize))
        W2_end = W1_end + self.hiddenLayerSize*self.outputLayerSize
        self.W2 = np.reshape(params[W1_end:W2_end], (self.hiddenLayerSize, self.outputLayerSize))

    def computeGradients(self, X, y):
        dJdW1, dJdW2 = self.costFunctionPrime(X, y)
        return np.concatenate((dJdW1.ravel(), dJdW2.ravel()))

    def computeNumericalGradient(N, X, y):
        paramsInitial = N.getParams()
        numgrad = np.zeros(paramsInitial.shape)
        perturb = np.zeros(paramsInitial.shape)
        e = 1e-4

        for p in range(len(paramsInitial)):
            #Set perturbation vector
            perturb[p] = e
            N.setParams(paramsInitial + perturb)
            loss2 = N.costFunction(X, y)

            N.setParams(paramsInitial - perturb)
            loss1 = N.costFunction(X, y)

            #Compute Nemerical Gradient:
            numgrad[p] = (loss2 - loss1) / (2*e)

            #Return the value we changed back to zero:
            perturb[p] = 0

        #Return Params to original value:
        N.setParams(paramsInitial)

        return numgrad

class trainer(object):
    def __init__(self, N):
        #Make Local reference to network:
        self.N = N

    def callbackF(self, params):
        self.N.setParams(params)
        self.J.append(self.N.costFunction(self.X, self.y))
        self.testJ.append(self.N.costFunction(self.testX, self.testY))

    def costFunctionWrapper(self, params, X, y):
        self.N.setParams(params)
        cost = self.N.costFunction(X, y)
        grad = self.N.computeGradients(X,y)

        return cost, grad

    def train(self, trainX, trainY, testX, testY):
        #Make an internal variable for the callback function:
        self.X = trainX
        self.y = trainY

        self.testX = testX
        self.testY = testY

        #Make empty list to store training costs:
        self.J = []
        self.testJ = []

        params0 = self.N.getParams()

        options = {'maxiter': 200, 'disp' : True}
        _res = optimize.minimize(self.costFunctionWrapper, params0, jac=True, method='BFGS',
                                 args=(trainX, trainY), options=options, callback=self.callbackF)

        self.N.setParams(_res.x)
        self.optimizationResults = _res

def main():
    # X = (hours sleeping, hours studying), y = Score on test
    trainX = np.array(([3,5], [5,1], [10,2], [6,1.5]), dtype=float)
    trainY = np.array(([75], [82], [93], [70]), dtype=float)

    testX = np.array(([4, 5.5], [4.5, 1], [9, 2.5], [6, 2]), dtype=float)
    testY = np.array(([70], [89], [85], [75]), dtype=float)

    trainX = trainX/np.amax(trainX, axis=0)
    trainY = trainY/100 #Max test score is 100

    testX = testX/np.amax(trainX, axis=0)
    testY = testY/100 #Max test score is 100

    NN = Neural_Network(Lambda=0.0001)

    cost1 = NN.costFunction(trainX,trainY)
    dJdW1, dJdW2 = NN.costFunctionPrime(trainX, trainY)

    scalar = 3
    NN.W1 = NN.W1 + scalar*dJdW1
    NN.W2 = NN.W2 + scalar*dJdW2
    cost2 = NN.costFunction(trainX,trainY)

    dJdW1, dJdW2 = NN.costFunctionPrime(trainX, trainY)
    NN.W1 = NN.W1 - scalar*dJdW1
    NN.W2 = NN.W2 - scalar*dJdW2
    cost3 = NN.costFunction(trainX, trainY)

    #numgrad = NN.computeNumericalGradient(trainX, trainY)
    grad = NN.computeGradients(trainX, trainY)
    #print(np.linalg.norm(grad-numgrad)/np.linalg.norm(grad+numgrad))

    T = trainer(NN)
    T.train(trainX, trainY, testX, testY)


main()
