# -------------------------------------------------------------------------
# AUTHOR: Joey Cindass
# FILENAME: naive_bayes.py
# SPECIFICATION: Using naive bayes, predict if someone will play tennis given weather conditions
# FOR: CS 4210- Assignment #2
# TIME SPENT: 4 hour
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to
# work here only with standard dictionaries, lists, and arrays

# importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

# reading the training data in a csv file
# --> add your Python code here
db = []
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row[1:])

# transform the original training features to numbers and add them to the 4D array X.
# For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
# --> add your Python code here
# X =
X = []
for i in range(len(db)):
    X_temp = []
    for j in range(len(db[i])):
        ones = ['Sunny', 'Cool', 'Normal', 'Weak']
        twos = ['Overcast', 'Mild', 'High', 'Strong']
        threes = ['Rain', 'Hot']
        if db[i][j] in ones:
            X_temp.append(1)
        elif db[i][j] in twos:
            X_temp.append(2)
        elif db[i][j] in threes:
            X_temp.append(3)
    X.append(X_temp)

# transform the original training classes to numbers and add them to the vector Y.
# For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> add your Python code here
# Y =
Y = []
for i in range(len(db)):
    if db[i][-1] == "Yes":
        Y.append(1)
    else:
        Y.append(0)

# fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

# reading the test data in a csv file
# --> add your Python code here
db2 = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db2.append(row[1:])

# printing the header os the solution
print("Day Outlook  Temperature Humidity Wind    PlayTennis Confidence")

# use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
# --> add your Python code here

X2 = []
for i in range(len(db2)):
    X2_temp = []
    for j in range(len(db2[i])):
        ones = ['Sunny', 'Cool', 'Normal', 'Weak']
        twos = ['Overcast', 'Mild', 'High', 'Strong']
        threes = ['Rain', 'Hot']
        if db2[i][j] in ones:
            X2_temp.append(1)
        elif db2[i][j] in twos:
            X2_temp.append(2)
        elif db2[i][j] in threes:
            X2_temp.append(3)
    X2.append(X2_temp)

conf_list = []
pred_list = []
for instance in X2:
    confidence = clf.predict_proba([instance])[0]
    pred = clf.predict([instance])
    if pred == 1:
        pred_list.append("Yes")
    else:
        pred_list.append("No")
    conf_list.append(confidence.max())

for i in range(len(db2)):
    if conf_list[i] >= 0.75:
        print(f"D{i+15} {db2[i][0]:8} {db2[i][1]:11} {db2[i][2]:8} {db2[i][3]:4}    {pred_list[i]} {conf_list[i]:25}")

