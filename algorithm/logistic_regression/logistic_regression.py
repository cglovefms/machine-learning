# logistic回归
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

def cost_function(theta,input,output):
    h=sigmoid(np.dot(input,theta))
    return np.sum(np.multiply(-output,np.log(h))+np.multiply((output-1),np.log(1-h)))/input.shape[0]

def gradient_desc(input,output):
    alpha=0.02
    max_iter=1000
    featureNo=input.shape[1]
    theta=np.ones(featureNo).reshape(featureNo,1)/featureNo
    iter=0
    cost=[]
    while iter<max_iter:
        h = sigmoid(np.dot(input, theta))
        theta=theta-alpha*np.dot(input.T,h-output)
        cost.append(cost_function(theta,input,output))
        iter +=1
    return theta,cost

def logistic_regression(input,output,x):
    parameter=gradient_desc(input_t,output_t)[0]
    predict=sigmoid(np.dot(x,parameter))


if __name__=='__main__':
    input_t=np.random.random((100,7))
    output_t=np.random.random((100,1))
    parameter_result=gradient_desc(input_t,output_t)[0]
    cost_result=gradient_desc(input_t,output_t)[1]
    print(parameter_result)
    plt.plot(cost_result)