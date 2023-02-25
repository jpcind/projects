# -------------------------------------------------------------------------
# AUTHOR: Joey Cindass
# FILENAME: knn.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: 4 hours
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas.
# You have to work here only with standard vectors and arrays

# importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv
db = []

# reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)

# loop your data to allow each instance to be your test set
data_features = []
data_classes = []
for instance in db:
    # print(instance)

    # add the training features to the 2D array X removing the instance that will be used for testing in this iteration.
    # For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    # --> add your Python code here

    # X =

    # transform the original training classes to numbers and
    # add to the vector Y removing the instance that will be used for testing in this iteration.
    # For instance, Y = [1, 2, ,...]. Convert each
    # feature value to float to avoid warning messages
    # --> add your Python code here
    # Y =

    instance_features = []
    for i in range(len(instance)):
        if instance[i] == '-':
            data_classes.append(0)
            continue
        if instance[i] == '+':
            data_classes.append(1)
            continue
        instance_features.append(int(instance[i]))
    data_features.append(instance_features)


    # store the test sample of this iteration in the vector testSample
    # --> add your Python code here
    # testSample =

X_features = []
X_classes = []
Y_features = []
Y_classes = []
for i in range(len(data_features)):
    X_temp = []
    X2_temp = []
    for j in range(len(data_features)):
        if i == j:
            Y_features.append(data_features[j])
            Y_classes.append(data_classes[j])
        else:
            X_temp.append(data_features[j])
            X2_temp.append(data_classes[j])
    X_classes.append(X2_temp)
    X_features.append(X_temp)


# fitting the knn to the data

class_pred_list = []
for i in range(len(Y_features)):
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X_features[i], X_classes[i])

# use your test sample in this iteration to make the class prediction. For instance:
# class_predicted = clf.predict([[1, 2]])[0]
# --> add your Python code here
    class_predicted = clf.predict(Y_features)[0]
    class_pred_list.append(class_predicted)


    # compare the prediction with the true label of the test instance to start calculating the error rate.
    # --> add your Python code here
correct_counter = 0
for i in range(len(class_pred_list)):
    if class_pred_list[i] == Y_classes[i]:
        correct_counter += 1
error_rate = correct_counter/len(class_pred_list)

# print the error rate
# --> add your Python code here
print("Error rate = {}".format(error_rate))
