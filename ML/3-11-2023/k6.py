from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,classification_report
from sklearn.model_selection import  train_test_split
from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data
y = iris.target
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=40)
tree = DecisionTreeClassifier()
tree.fit(x_train,y_train)
print(tree.predict(x_test))
v = tree.predict(x_test)
result = accuracy_score (y_test,v)
report = classification_report (y_test, v)
print("Accuracy score",result)
print("Classificatio report \n ", report)