from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

clf = GaussianNB()

iris = datasets.load_iris()
# Cross Validation:
train_data, test_data, train_labels, test_labels = train_test_split(iris.data, iris.target, test_size=0.2)
clf.fit(train_data, train_labels)
print('----------------------')
# mean and standard deviation
print(clf.theta_)
print(clf.sigma_)
# Priori
print(clf.class_prior_)
print(clf.class_count_)
print('----------------------------')

predict_label = clf.predict(test_data)

print(predict_label)
print(test_labels)
# Posterior
print('---------------Posterior--------------')
yprob = clf.predict_proba(test_data)
print(yprob)
# Performance Evaluation:
correct_number = (predict_label == test_labels).sum()
print(predict_label == test_labels)
total_number = predict_label.shape[0]
print("----------------")
accuracy = correct_number / total_number
print("the correct number is ", correct_number)
print("the accuracy is ", accuracy)
# print((clf.predict(test_data)!=test_labels).sum)
