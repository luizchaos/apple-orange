from sklearn import tree

# index
plain = 1
irregular =0
apple = 1
orange = 0

# weight and surface of the fruits
data = [[150,plain],
        [130,plain],
        [180,irregular],
        [160,irregular],
        [190,irregular],
        [140,plain]]

result = [apple, apple, orange, orange, orange, apple]

clf = tree.DecisionTreeClassifier()

clf.fit(data, result)

# user inputs
weight = input("Weight: ")

surface = input("Surface(plain or irregular): ")

if surface == "plain":
    surface = 1
else:
    surface = 0

# trying to predict the fruit
userResult = clf.predict([[weight, surface]])

#  printing result
if userResult == 1:
    print("Apple")
else:
    print("Orange")