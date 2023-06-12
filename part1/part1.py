from Node import Node

features = input("Welcome to feature selection algorithm \nPlease enter total number of features: ")

alg = input ("\nType the number of the algorithm you would like to run: \n\n1. Forward Selection\n2. Backward Elimination\n")

curr = Node(int(features), [])

if alg == "1":
    curr.forwardSelection()
elif alg == "2":
    curr.backwardElimination()
else:
    print("Invalid input\n")
    quit()