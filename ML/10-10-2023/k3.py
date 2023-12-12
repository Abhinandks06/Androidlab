from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from  sklearn.datasets import load_diabetes
from sklearn.metrics import mean_squared_error
diabetes = load_diabetes()
x = diabetes.data
y = diabetes.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=46)
knn=KNeighborsRegressor(n_neighbors=7)
knn.fit(x_train,y_train)
print(knn.predict(x_test))
v=knn.predict(x_test)
result=mean_squared_error(y_test, v)
print("Mean squard error",result)