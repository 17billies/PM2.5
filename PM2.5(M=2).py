#M=2
import numpy as np 
import matplotlib.pyplot as plt 
import math
import time

#calculate the runtime of the program
start_time = time.time()

#read the data which X features has add a new line 1 so means X_0
dataT=np.genfromtxt('data_T.csv',delimiter=',')
dataX=np.genfromtxt('data_X.csv',delimiter=',')

#split the data into training set and the testing set
def train_test_split(X,Y,test_size):
    X_train=X[:math.floor(len(X)*(1-test_size))]
    Y_train=Y[:math.floor(len(Y)*(1-test_size))]
    X_test=X[math.floor(len(X)*(1-test_size)):]
    Y_test=Y[math.floor(len(Y)*(1-test_size)):]
    return X_train, X_test, Y_train, Y_test

#hypothesis function(M=2):
def hypothesis(theta,X):
    value=0
    for i in range(0,18):
        value+=theta[i]*X[i]
    for i in range(1,18):
        for j in range(1,i+1):
            value+=theta[i+17]*X[i]*X[j]
    return value

#calculate the cost function
def square_error(theta,X,T):
    sqr_error=0
    for i in range(0,len(X)):
        sqr_error+=(hypothesis(theta,X[i])-T[i])**2
    return sqr_error/len(X)/2

#gradient descent
def gradient_descent(X,T,theta,learning_rate,iteration):
    N=len(X)
    cost_function=[]
    for i in range(iteration):
        theta_grad=[0]*len(theta)
        for j in range(0,N):
            for k in range(0,len(theta)):
                if k<len(X[0]):
                    theta_grad[k]+=(1/N)*(hypothesis(theta,X[j])-T[j])*X[j,k]
                else:
                    for m in range(1,18):
                        for n in range(1,m+1):
                            theta_grad[k+17]+=(1/N)*(hypothesis(theta,X[j])-T[j])*X[j,m]*X[j,n]
        for l in range(0,len(theta)):
            theta[l]-=learning_rate*theta_grad[l]
        cost_function.append(square_error(theta,X_train,T_train))
    return theta,cost_function

#rmse
def rmse(y1,y2):
    error=0
    for i in range(len(y1)):
        error+=(y1[i]-y2[i])**2
    return math.sqrt(error/len(y1))

#setting the parameter
learning_rate=0.00001
theta=[0]*171
iteration=2000

#split the dataset into training dataset and testing dataset
X_train,X_test,T_train,T_test = train_test_split(dataX,dataT, test_size = 0.2)
#train:876 test:220

#the initial weight value and the final weight value
print("Initial state:")
print("theta=",theta)
print("Running for the method of gradient descent")
theta,cost_function=gradient_descent(X_train,T_train,theta,learning_rate,iteration)
print("Final state:")
print("theta=",theta)

#plot the cost function versus iteration times
for i in range(0,len(cost_function)):
    plt.plot(i,cost_function[i],'b.')
plt.title("cost function versus iteration times")
plt.xlabel("iteration times")
plt.ylabel("cost function")
plt.show()

#plot the value of the model predict and the actual model (train part)
x=np.arange(0,len(X_train))
y=[]
for i in range(0,len(X_train)):
    y.append(hypothesis(theta,X_train[i]))
plt.plot(x,y,color='red',lw=1.0,ls='-',label="training_predict_value")
plt.plot(x,T_train,color='blue',lw=1.0,ls='-',label="target_value")
plt.text(0,1,"RMSE=%.3lf" %(rmse(T_train,y)))
plt.xlabel("the nth data")
plt.ylabel("PM2.5")
plt.title("Linear regression (M=1) training")
plt.legend()
plt.show()

#plot the value of the model predict and the actual model (test part)
x=np.arange(0,len(X_test))
y=[]
for i in range(0,len(X_test)):
    y.append(hypothesis(theta,X_test[i]))
plt.plot(x,y,color='red',lw=1.0,ls='-',label="testing_predict_value")
plt.plot(x,T_test,color='blue',lw=1.0,ls='-',label="target_value")
plt.text(0,1,"RMSE=%.3lf" %(rmse(T_test,y)))
plt.xlabel("the nth data")
plt.ylabel("PM2.5")
plt.title("Linear regression (M=1) testing")
plt.legend()
plt.show()

#the runtime of the program
end_time=time.time()
print("the runtime of this program:%.3lf" %(end_time-start_time))