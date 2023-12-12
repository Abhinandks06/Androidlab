import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
x=np.array([64,75,68,73,78,82,76,85,71,88]).reshape(-1,1)
y=np.array([17,27,15,24,39,44,30,48,19,47])
model=LinearRegression()
model.fit(x,y)
slope=model.coef_[0]
intercept=model.intercept_
print("Slope =",slope)
print("Intercept = ",intercept)
