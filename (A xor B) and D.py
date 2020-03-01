import numpy as np

# Generating and defining random weights, bias, learning rate for synapses and neurons
w = [np.random.random(), np.random.random(), np.random.random(), np.random.random(), np.random.random()]
bias = 1
lr = 1


# Activation Function
def Sigmoid(x):
    return 1/(1+np.exp(-x))


# Neural Network
def Synopsis(a, b, c, d, e):
    cal = a*w[0] + b*w[1] + c*w[2] + d*w[3] + w[4]*bias
    sig = Sigmoid(cal)
    
    if cal > sig:
        output = 1
    else:
        output = 0
        
    count = 0
    if e != output:
        count += 1
    
    error = e - output
    w[0] += a*error*lr
    w[1] += b*error*lr
    w[2] += c*error*lr
    w[3] += d*error*lr
    w[4] += error*bias*lr
    
    print("a=", a, " b=", b, " c=", c, " d=", d, " e=", e, "(", output, ")", " cal=", cal, " sig=", sig)
    return count


# Training and evaluating the network
epochs=10
for i in range(epochs):
    count = 0
    count += Synopsis(0,0,0,0,0)
    count += Synopsis(0,0,0,1,0)
    count += Synopsis(0,1,1,0,0)
    count += Synopsis(0,1,1,1,1)
    count += Synopsis(1,0,1,0,0)
    count += Synopsis(1,0,1,1,1)
    count += Synopsis(1,1,0,0,0)
    count += Synopsis(1,1,0,1,0)
    print("Total False Result: ", count)
    print()

