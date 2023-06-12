from Validator import Validator
from Classifier import Classifier

file = input("Welcome to our evluation function. Please enter the number of the dataset you would like to test: \n1. Small test dataset \n2. Large test dataset\n")

if file == "1":
    filepath = "data/small-test-dataset.txt"
elif file == "2":
    filepath = "data/large-test-dataset-1.txt"
else:
    print("Invalid input\n")
    quit()

n = input("Please enter the number of features you would like to test: ")

features = []
print("\n\nPlease input the features followed by enter")
for i in range(int(n)):
    curr = input()
    features = features + [int(curr)]

print("Running k-fold cross validation")

validator = Validator()
accuracy = validator.validate(features, filepath)

print("The file", filepath, "has an accuracy of", accuracy, "when tested with features:", features)
