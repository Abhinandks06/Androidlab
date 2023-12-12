from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from  sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,accuracy_score
from sklearn.svm import SVC
categories = ['alt.atheism','soc.religion.christian','comp.graphics','sci.med']
twenty_train = fetch_20newsgroups(subset='train',categories=categories,shuffle=True,random_state=42)
vectorizer = TfidfVectorizer()
x_train_tfidf = vectorizer.fit_transform(twenty_train.data)
y_train = twenty_train.target
x_train,x_test,y_train,y_test = train_test_split(x_train_tfidf,y_train,random_state=42,test_size=0.3)
svm_classifier = SVC(kernel='linear',random_state=42)
svm_classifier.fit(x_train,y_train)
prediction = svm_classifier.predict(x_test)
accuracy = accuracy_score(y_test,prediction)
class_report = classification_report(y_test,prediction, target_names=twenty_train.target_names)
print("Accuracy score =", accuracy)
print("Classification report : \n",class_report)

newdata = [
    "i dont know what im typing",
    "error404 not found"
]
x_new_tfidf = vectorizer.transform(newdata)
new_prediction = svm_classifier.predict(x_new_tfidf)
print("New prediction",new_prediction)