from Validator import Validator
import random 
import pandas as pd

class Node: 
    def __init__(self, _features, filepath): 
        self.features = _features
        self.children = []
        self.score = -1
        self.filepath = filepath
        df = pd.read_csv(filepath, delim_whitespace=True, header=None, engine="python")
        self.possibleFeatures = df.shape[1] - 1
        self.evaluate(filepath)


    def evaluate(self, filepath): 
        # returns integer 
        # self.score = random.uniform(0, 100)
        valid = Validator()
        self.score = valid.validate(self.features, filepath)

    def returnScore(self):
        return self.score
    
    def addFeature(self):
        for i in range(1, self.possibleFeatures + 1): 
            if i not in self.features: 
                features = self.features + [i]
                newNode = Node(features, self.filepath)
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
            newNode = Node(newFeatures, self.filepath)
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
        

  
