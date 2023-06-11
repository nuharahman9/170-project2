from Node import Node 
from Classifier import Classifier
from Validator import Validator
import numpy 
import pandas as pd

# n = 4
# node = Node(n, [])

# (node.forwardSelection())

# tempClass = Classifier("/Users/terencemui/Documents/CS170/170-project2/small-test-dataset.txt")
# p1 = tempClass.df.iloc[0].to_numpy()
# p2 = tempClass.df.iloc[1].to_numpy()
# print(type(p1))
# print(tempClass.euclideanDistance(p1, p2))

# print("test")

# print(tempClass.test(3))


# print(tempClass.df)


filepath = "/Users/terencemui/Documents/CS170/170-project2/large-test-dataset-1.txt"
testValid = Validator()
testValid.validate([1, 15, 27], filepath)

# filepath = "/Users/terencemui/Documents/CS170/170-project2/small-test-dataset.txt"
# testValid = Validator()
# testValid.validate([3, 5, 7], filepath)