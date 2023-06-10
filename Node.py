
import random 

class Node: 
    def __init__(self, n): 
        self.possibleFeatures = n
        self.features = []
        self.neighbors = []

    def evaluate(self): 
        return random.randint() % 100
    
    def addFeature(self):
        for i in range(0, self.possibleFeatures): 
            if i not in self.possibleFeatures: 
                newNode = Node(self.possibleFeatures)
                self.neighbors.push(newNode)
    

    

