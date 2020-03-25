from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()

iris = datasets.load_iris()
# split dataset
train_data, test_data, train_labels, test_labels = train_test_split(iris.data, iris.target, test_size=0.2)
clf.fit(train_data, train_labels)
prior = np.zeros(3)
for i in range(3):
    count = len(train_labels[train_labels == i])
    total_count = len(train_labels)
    prior[i] = count / total_count
print('------------prior----------------')
print(prior)

train_labels = train_labels[:, np.newaxis]
combine = np.concatenate((train_data, train_labels), axis=1)
frame = pd.DataFrame(combine)
frame.columns = ['length of sepals', 'width of sepals', 'length of petals', 'width of petals', 'category']
data_mean = frame.groupby("category").mean()
data_variance = frame.groupby("category").var()
print('-----------------data_mean--------------------')
print(data_mean)
print('-----------------data_variance--------------------')
print(data_variance)


# Create a function that calculates p(x | y):
def p_x_given_y(x, mean_y, variance_y):
    # Input the arguments into a probability density function
    p = 1 / (np.sqrt(2 * np.pi * variance_y)) * np.exp((-(x - mean_y) ** 2) / (2 * variance_y))

    # return p
    return p


predict_label = clf.predict(test_data)

# Posterior P(Cj |X)
posterior = np.zeros([test_data.shape[0], 3])
print("--------------------------posterior--------------------------")
for i in range(test_data.shape[0]):
    for j in range(3):
        first_f = p_x_given_y(test_data[i][0], data_mean.iloc[j, 0], data_variance.iloc[j, 0])
        second_f = p_x_given_y(test_data[i, 1], data_mean.iloc[j, 1], data_variance.iloc[j, 1])
        third_f = p_x_given_y(test_data[i, 2], data_mean.iloc[j, 2], data_variance.iloc[j, 2])
        forth_f = p_x_given_y(test_data[i, 3], data_mean.iloc[j, 3], data_variance.iloc[j, 3])
        posterior[i, j] = prior[j] * first_f * second_f * third_f * forth_f

print(posterior)
# Posterior

print('---------------Posterior--------------')
yprob = clf.predict_proba(test_data)
print(yprob)
# Performance Evaluation:
estimated_y_label = np.argmax(posterior, axis=1)
print(estimated_y_label, '----------------------------')
# Performance Evaluation2 :
correct_number = (predict_label == test_labels).sum()
total_number = predict_label.shape[0]
accuracy = correct_number / total_number
print("the correct number is ", correct_number)
print("the accuracy is ", accuracy)
