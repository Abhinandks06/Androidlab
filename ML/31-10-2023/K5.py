from sklearn.datasets import load_breast_cancer
from  sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
data = load_breast_cancer()
x = data.data
y = data.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=40)
clf = GaussianNB()
clf.fit(x_train,y_train)
print(clf.predict(x_test))
v = clf.predict(x_test)
result = accuracy_score(y_test, v)
print("Accuracy",result)
