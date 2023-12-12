from sklearn.neighbors import KNeighborsClassifier #Selecting algorithm
from sklearn.model_selection import train_test_split #Selecting model
from sklearn.datasets import  load_digits
from sklearn.metrics import  accuracy_score
digits = load_digits()
x = digits.data
y = digits.target
x_test, x_train, y_test, y_train = train_test_split(x, y, test_size=0.2,random_state=46)
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train,y_train)
print(knn.predict(x_train))
v=knn.predict(x_test)
result=accuracy_score(y_test,v)
print("Accuracy",result)
