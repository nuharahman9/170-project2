import random 
import pandas as pd

class Node: 
    def __init__(self, n, _features): 
        self.features = _features
        self.children = []
        self.possibleFeatures = n
        self.score = -1
        self.evaluate()

    def evaluate(self): 
        # returns random integer 
        self.score = random.uniform(0, 100)

    def returnScore(self):
        return self.score
    
    def addFeature(self):
        for i in range(1, self.possibleFeatures + 1): 
            if i not in self.features: 
                features = self.features + [i]
                newNode = Node(self.possibleFeatures, features)
                self.children.append(newNode)

    def forwardSelection(self): 
        print("Beginning search...")
        accuracy, features = self.forwardSelectionHelper()
        print("The best feature set was", features, "with accuracy", accuracy)

    def forwardSelectionHelper(self):
        self.addFeature()

        if self.children == []:
            return -1, []
        
        bestAccuracy = self.children[0].returnScore()
        bestChild = self.children[0]
        for child in self.children:
            temp = child.returnScore()
            print("Using feature(s)", child.features, ", accuracy is ", temp)
            if (bestAccuracy < temp):
                bestAccuracy = temp
                bestChild = child

        print("The best child to expand was: ", bestChild.features, bestAccuracy)
        
        tempAccuracy, tempFeatures = bestChild.forwardSelectionHelper()

        if (tempAccuracy > bestAccuracy):
            return tempAccuracy, tempFeatures
        else:
            return bestAccuracy, bestChild.features

    def removeFeature(self):
        for i in self.features: 
            newFeatures = list(self.features)
            newFeatures.remove(i)
            newNode = Node(self.possibleFeatures, newFeatures)
            self.children.append(newNode)

    def backwardElimination(self):
        print("Beginning search.")
        self.features = list(range(1, self.possibleFeatures + 1))
        accuracy, features =  self.backwardEliminationHelper()
        print("The best accuracy was ", accuracy, " with features: ", features)

    def backwardEliminationHelper(self):
        self.removeFeature()

        if self.children == []:
            return -1, []
        
        bestAccuracy = self.children[0].returnScore()
        bestChild = self.children[0]
        for child in self.children:
            temp = child.returnScore()
            print("Using feature(s)", child.features, ", accuracy is ", temp)
            if (bestAccuracy < temp):
                bestAccuracy = temp
                bestChild = child

        print("The best child to expand was: ", bestChild.features, bestAccuracy)

        tempAccuracy, tempFeatures = bestChild.backwardEliminationHelper()

        if (tempAccuracy > bestAccuracy):
            return tempAccuracy, tempFeatures
        else:
            return bestAccuracy, bestChild.features
        

  
