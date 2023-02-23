# -------------------------------------------------------------------------
# AUTHOR: Joey Cindass
# FILENAME: decision_tree_2
# SPECIFICATION: decision tree algorithm train algorithm
# FOR: CS 4210- Assignment #2
# TIME SPENT: 3 hours
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to
# work here only with standard dictionaries, lists, and arrays

# importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:
    dbTraining = []
    X = []
    Y = []

    # reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:  # skipping the header
                dbTraining.append(row)

    # transform the original categorical training features to numbers and add to the 4D array X.
    # For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3 so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    # --> add your Python code here X =
    for i in range(len(dbTraining)):
        temp_list = []
        for j in range(len(dbTraining)):
            if j == 0:
                if dbTraining[i][j] == 'Young':
                    temp_list.append(1)
                elif dbTraining[i][j] == 'Presbyopic':
                    temp_list.append(2)
                else:
                    temp_list.append(3)
            if j == 1:
                if dbTraining[i][j] == 'Myope':
                    temp_list.append(1)
                else:
                    temp_list.append(2)
            if j == 2:
                if dbTraining[i][j] == 'Yes':
                    temp_list.append(1)
                else:
                    temp_list.append(2)
            if j == 3:
                if dbTraining[i][j] == 'Normal':
                    temp_list.append(1)
                else:
                    temp_list.append(2)
        X.append(temp_list)

    # transform the original categorical training classes to numbers and add to the vector Y.
    # For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    # --> add your Python code here Y =
    for i in range(len(dbTraining)):
        if dbTraining[i][len(dbTraining[i]) - 1] == 'Yes':
            Y.append(1)
        else:
            Y.append(0)

    # loop your training and test tasks 10 times here
    correct_preds = 0
    total_preds = 0

    for i in range(10):
        # fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
        clf = clf.fit(X, Y)

        # read the test data and add this data to dbTest
        # --> add your Python code here
        # dbTest =
        dbTest = []
        X2 = []
        Y2 = []

        with open("contact_lens_test.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0:
                    dbTest.append(row)

        for i in range(len(dbTest)):
            temp_list = []
            for j in range(len(dbTest)):
                if j == 0:
                    if dbTest[i][j] == 'Young':
                        temp_list.append(1)
                    elif dbTest[i][j] == 'Presbyopic':
                        temp_list.append(2)
                    else:
                        temp_list.append(3)
                if j == 1:
                    if dbTest[i][j] == 'Myope':
                        temp_list.append(1)
                    else:
                        temp_list.append(2)
                if j == 2:
                    if dbTest[i][j] == 'Yes':
                        temp_list.append(1)
                    else:
                        temp_list.append(2)
                if j == 3:
                    if dbTest[i][j] == 'Normal':
                        temp_list.append(1)
                    else:
                        temp_list.append(2)
            X2.append(temp_list)

        for i in range(len(dbTest)):
            if dbTest[i][len(dbTest[i]) - 1] == 'Yes':
                Y2.append(1)
            else:
                Y2.append(0)


            # transform the features of the test instances to numbers following the same strategy done during
            # training, and then use the decision tree to make the class prediction. For instance:
            # class_predicted = clf.predict([[3, 1, 2, 1]])[0]
            # where [0] is used to get an integer as the predicted class label so that
            # you can compare it with the true label
            # --> add your Python code here
            predictions = []
            for i in X2:
                class_predicted = clf.predict([i])[0]
                predictions.append(class_predicted)


        # compare the prediction with the true label (located at data[4]) of the test instance to start
        # calculating the accuracy.
        # --> add your Python code here
        total_preds += len(Y2)
        for i in range(len(Y2)):
            if Y2[i] == predictions[i]:
                # total_pred += 1
                correct_preds += 1


    # find the average of this model during the 10 runs (training and test set)
    # --> add your Python code here
    accuracy = correct_preds / total_preds

    # print the average accuracy of this model during the 10 runs (training and test set).
    # your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    # --> add your Python code here
    print("Final accuracy for {}: {} ".format(ds, accuracy))
