from Node import Node 
from Classifier import Classifier
import numpy 

# n = 4
# node = Node(n, [])

# (node.forwardSelection())

tempClass = Classifier()
p1 = tempClass.df.iloc[0].to_numpy()
p2 = tempClass.df.iloc[1].to_numpy()
# print(type(p1))
# print(tempClass.euclideanDistance(p1, p2))

print(tempClass.test(3))


# print(tempClass.df)