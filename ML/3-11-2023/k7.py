from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score,classification_report
from sklearn.model_selection import  train_test_split
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt

data = load_breast_cancer()
x = data.data
y = data.target
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=40)
tree = DecisionTreeClassifier(max_depth=2)
tree.fit(x_train,y_train)
plt.figure(figsize=(15, 10))
plot_tree(tree, filled=True, feature_names=data.feature_names, class_names=data.target_names)
plt.show()
print(tree.predict(x_test))
v = tree.predict(x_test)
result = accuracy_score (y_test,v)
report = classification_report (y_test, v)
print("Accuracy score",result)
print("Classificatio report", report)



