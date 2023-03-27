# -------------------------------------------------------------------------
# AUTHOR: Joey Cindass
# FILENAME: svm.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #3
# TIME SPENT: 3 hours
# -----------------------------------------------------------*/

# IMPORTANT NOTE: YOU HAVE TO WORK WITH THE PYTHON LIBRARIES numpy AND pandas to complete this code.

# importing some Python libraries
from sklearn import svm
import numpy as np
import pandas as pd

# defining the hyperparameter values
c = [1, 5, 10, 100]
degree = [1, 2, 3]
kernel = ["linear", "poly", "rbf"]
decision_function_shape = ["ovo", "ovr"]

# reading the training data by using Pandas library
df = pd.read_csv('optdigits.tra', sep=',', header=None)

# getting the first 64 fields to create the feature training data and convert them to NumPy array
X_training = np.array(df.values)[:, :64]

# getting the last field to create the class training data and convert them to NumPy array
y_training = np.array(df.values)[:, -1]

# reading the training data by using Pandas library
df = pd.read_csv('optdigits.tes', sep=',', header=None)

# getting the first 64 fields to create the feature testing data and convert them to NumPy array
X_test = np.array(df.values)[:, :64]

# getting the last field to create the class testing data and convert them to NumPy array
y_test = np.array(df.values)[:, -1]

# created 4 nested for loops that will iterate through the values of c, degree, kernel, and decision_function_shape
# --> add your Python code here
higher_acc = 0
for i in c:
    for j in degree:
        for k in kernel:
            for l in decision_function_shape:
                correct = 0
                clf = svm.SVC(C=int(i), degree=int(j), kernel=k, decision_function_shape=l)
                clf.fit(X_training, y_training)
                for (x_testSample, y_testSample) in zip(X_test, y_test):
                    pred = clf.predict([x_testSample])[0]
                    if pred == y_testSample:
                        correct += 1
                acc = correct/len(X_test)
                if higher_acc < acc:
                    higher_acc = acc
                    print("Highest SVM accuracy so far: {}, Parameters: C={}, degree={}, "
                          "kernel={}, decision_function_shape={}".format(round(higher_acc, 3),i, j, k, l))



                # Create an SVM classifier that will test all combinations of c, degree, kernel,
                # and decision_function_shape.
                # For instance svm.SVC(c=1, degree=1, kernel="linear", decision_function_shape = "ovo")
                # --> add your Python code here

                # Fit SVM to the training data
                # --> add your Python code here

                # make the SVM prediction for each test sample and start computing its accuracy
                # hint: to iterate over two collections simultaneously, use zip()
                # Example. for (x_testSample, y_testSample) in zip(X_test, y_test):
                # to make a prediction do: clf.predict([x_testSample])
                # --> add your Python code here

                # check if the calculated accuracy is higher than the previously one calculated.
                # If so, update the highest accuracy and print it together
                # with the SVM hyperparameters.
                # Example:
                # "Highest SVM accuracy so far: 0.92, Parameters: a=1, degree=2, kernel= poly, decision_function_shape = 'ovo'"
                # --> add your Python code here




