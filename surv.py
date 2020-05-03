import numpy as np

class percep():
    def __init__(self, eta = 0.1, num_iter = 50, random_state =1): 
        self.eta = eta 
        self.num_iter = num_iter
        self.random_state = random_state 
    
    def fit(self, X,Y):
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc = 0.0, scale = 0.01, size = 1+ X.shape[1])
        self.errors_= []
        
        for _ in range(self.num_iter):
            errors = 0
            for xi,target  in zip(X,Y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi 
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

def net_input(self,X):
    return np.dot(X, self.w_[1:]) + self.w_[0]

def predict(self,X):
    return np.where(self.net_input(X) >= 0.0, 1, -1)


import pandas as pd 

df = pd.read_csv('https://archive/ics.uci.edu/ml/'machine-learning-databases/iris/iris.data',header = None)