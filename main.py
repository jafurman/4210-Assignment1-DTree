# -------------------------------------------------------------------------
# AUTHOR: Joshua Furman
# FILENAME: dTree.py or main.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to
# work here only with standard dictionaries, lists, and arrays

# importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv

db = []
X = []
Y = []

# reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
            print(row)

# transform the original categorical training features into numbers and add to the 4D array X. For instance Young =
# 1, Prepresbyopic = 2, Presbyopic = 3 so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]] --> add your Python code here

for row in db:
    xDataRow = []
    for i, value in enumerate(row):
        if i == 0:
            xDataRow.append(1 if value == 'Young' else 2 if value == 'Prepresbyopic' else 3)
        elif i == 1:
            xDataRow.append(1 if value == "Myope" else 2)
        elif i == 2:
            xDataRow.append(1 if value == 'No' else 2)
        elif i == 3:
            xDataRow.append(1 if value == 'Reduced' else 2)
    X.append(xDataRow)

# transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1,
# No = 2, so Y = [1, 1, 2, 2, ...]
for row in db:
    Y.append(1 if row[-1] == 'Yes' else 2)

# fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X, Y)

# plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes', 'No'], filled=True,
               rounded=True)
plt.show()
