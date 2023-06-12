from Node import Node 
from Classifier import Classifier
from Validator import Validator
import numpy 
import pandas as pd


filepath = None
option = input("welcome to our 170 project 2!\nTo select a filepath, please enter a number:\n1. Sample small dataset from part 1\n2. Sample large dataset from part 1\n3. Our own small dataset\n4. Our own large dataset\nType any other integer to quit :+)\nPlease enter a number:\n")
if option == "1": 
    filepath = "data/small-test-dataset.txt"
elif option == "2": 
    filepath = "data/large-test-dataset-1.txt"
elif option == "3": 
    filepath = "data/CS170_Spring_2023_Small_data__95.txt"
elif option == "4": 
    filepath = "data/CS170_Spring_2023_Large_data__95.txt"
else: 
    print("Invalid input\n")
    quit()
node = Node([], filepath)

option = input("please select the desired option for search:\n1. Forward selection\n2. Backward elimination\nType anything else to quit :+)\nPlease enter a number:\n")
if option == "1": 
    node.forwardSelection()
if option == "2": 
    node.backwardElimination()
else: 
    print("Invalid input\n")
    quit()