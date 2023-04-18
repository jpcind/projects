#-------------------------------------------------------------------------
# AUTHOR: Joey Cindass
# FILENAME: perceptron.py
# SPECIFICATION: calculating perceptron and MLP accuracy
# FOR: CS 4210- Assignment #4
# TIME SPENT: 3 hours
#-----------------------------------------------------------*/
import sklearn.linear_model
#IMPORTANT NOTE: YOU HAVE TO WORK WITH THE PYTHON LIBRARIES numpy AND pandas to complete this code.

#importing some Python libraries
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier #pip install scikit-learn==0.18.rc2 if needed
import numpy as np
import pandas as pd

n = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0]
r = [True, False]

df = pd.read_csv('optdigits.tra', sep=',', header=None) #reading the data by using Pandas library

X_training = np.array(df.values)[:,:64] #getting the first 64 fields to form the feature data for training
y_training = np.array(df.values)[:,-1]  #getting the last field to form the class label for training

df = pd.read_csv('optdigits.tes', sep=',', header=None) #reading the data by using Pandas library

X_test = np.array(df.values)[:,:64]    #getting the first 64 fields to form the feature data for test
y_test = np.array(df.values)[:,-1]     #getting the last field to form the class label for test

higher_acc1 = 0
higher_acc2 = 0

for i in n:  # iterates over n

    for j in r:  # iterates over r


        # iterates over both algorithms
        # -->add your Pyhton code here

        # single = sklearn.linear_model.Perceptron(alpha=i, shuffle=j)
        # multi = sklearn.neural_network.MLPClassifier(alpha=i, shuffle=j)


        for k in range(len(n)*len(r)):  # iterates over the algorithms



            # Create a Neural Network classifier
            # if Perceptron then
            #    clf = Perceptron()    #use those hyperparameters: eta0 = learning rate, shuffle = shuffle the training data, max_iter=1000
            # else:
            #    clf = MLPClassifier() #use those hyperparameters: activation='logistic', learning_rate_init = learning rate,
            #    hidden_layer_sizes = number of neurons in the ith hidden layer,
            #                           shuffle = shuffle the training data, max_iter=1000
            # -->add your Pyhton code here

            # if Perceptron:
            #     clf = Perceptron(eta0=i, shuffle=j, max_iter=1000)
            # else:
            #     clf = MLPClassifier(activation='logistic', learning_rate_init=i, shuffle=j, max_iter=1000)

            # clf = Perceptron(eta0=i, shuffle=j, max_iter=1000)
            clf = Perceptron(eta0=i, shuffle=j, max_iter=1000)
            clf2 = MLPClassifier(activation='logistic', learning_rate_init=i, shuffle=j, max_iter=1000)


            # Fit the Neural Network to the training data

            clf.fit(X_training, y_training)
            clf2.fit(X_training, y_training)


            # make the classifier prediction for each test sample and start computing its accuracy
            # hint: to iterate over two collections simultaneously with zip() Example:
            # for (x_testSample, y_testSample) in zip(X_test, y_test):
            # to make a prediction do: clf.predict([x_testSample])
            # --> add your Python code here
            correct_counter1 = 0
            correct_counter2 = 0
            for (x_testSample, y_testSample) in zip(X_test, y_test):

                pred = clf.predict([x_testSample])[0]
                pred2 = clf2.predict([x_testSample])[0]
                if pred == y_testSample:
                    correct_counter1 += 1
                if pred2 == y_testSample:
                    correct_counter2 += 1
            acc = correct_counter1 / len(X_test)
            acc2 = correct_counter2 / len(X_test)
            if acc > acc2:
                if higher_acc1 < acc:
                    higher_acc1 = acc
                    print("Highest Perceptron accuracy so far: {}, Parameters: learning rate: {}, shuffle={}".format(
                        higher_acc1, i, j))
            else:
                if higher_acc2 < acc2:
                    higher_acc2 = acc2
                    print("Highest MLP accuracy so far: {}, Parameters: learning rate: {}, shuffle={}".format(
                        higher_acc2, i, j))

            # if higher_acc < acc:
            #     higher_acc = acc
            #     print("Highest Perceptron accuracy so far: {}, Parameters: learning rate: {}, shuffle={}".format(higher_acc, i, j))


            # check if the calculated accuracy is higher than the previously one calculated for each classifier.
            # If so, update the highest accuracy
            # and print it together with the network hyperparameters
            # Example: "Highest Perceptron accuracy so far: 0.88, Parameters: learning rate=0.01, shuffle=True"
            # Example: "Highest MLP accuracy so far: 0.90, Parameters: learning rate=0.02, shuffle=False"
            # --> add your Python code here











