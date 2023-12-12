from sklearn.naive_bayes import GaussianNB #Selecting algorithm
from sklearn.model_selection import train_test_split #Selecting model
from sklearn.datasets import load_iris #Selecting dataset
from sklearn.metrics import accuracy_score , classification_report
iris = load_iris()  #Load the data into iris
x = iris.data  #Add the features to x
y = iris.target #Add the target to y
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=40)
clf = GaussianNB()
clf.fit(x_train,y_train)
print(clf.predict(x_test))
v = clf.predict(x_test)
result = accuracy_score(y_test, v)
report = classification_report(y_test, v)
print("Accuracy",result)
print("Report",report)
