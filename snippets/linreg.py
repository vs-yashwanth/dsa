from sklearn import linear_model
import pandas as pd
import numpy as np
def main():    

    
    data = pd.read_csv(r'C:\Users\Yashwanth\Downloads\lr\bike_sharing_data.txt')
    print(data)
    m=data.Population.values.size
    X = (data.Population).values.reshape((m,1))
    X= np.append(np.ones((m,1)),X,axis=1)
    
    y = data.Profit.values.reshape((m,1))
    
    theta=np.zeros((2,1))
    theta,costs=grad(X,y,theta,0.01,2000)
    print(theta)
def grad(X,y,theta,alpha,n):
    m=len(y)
    costs=np.zeros((n,1))
    
    for i in range(n):
       
        del_theta=(alpha/m)*(np.dot(X.transpose(),(np.dot(X,(theta))-y)))
        theta-=del_theta
        costs[i]= cost(X,y,theta)
    return theta,costs
def cost(X,y,theta):
    m=len(y)
    d=(1/(2*m))*np.sum((X.dot(theta)-y)**2)
    return d
    
main()