import numpy as np
import pandas as pd 
import sys 

class Classifier:
    def __init__(self, filepath="/Users/nuharahman/Desktop/170-project2/small-test-dataset.txt"): 
        self.df = None
        self.train(filepath)

    def train(self, filepath):
        df = pd.read_csv(filepath, delim_whitespace=True, header=None, engine="python")
        # df.iloc[0].astype(int)
        self.df = df
    
    def euclideanDistance(self, point1, point2): 
        # assumption: p1 and p2 are numpy arrays 
        # print(point1, point2)

        return np.linalg.norm(point1 - point2)
        


        #  ser.to_numpy()

    def test(self, instance):
        # itereate through df
        # if the row != instance
        #   find min euclideanDistance
        # add later: drop unneeded columns 
        min = sys.float_info.max
        closestNeighbor = -1
        for index, row in self.df.iterrows():
            if (index != instance):
                distance = self.euclideanDistance(row.to_numpy()[1::], self.df.iloc[instance].to_numpy()[1::])
                if distance < min:
                    min = distance
                    closestNeighbor = row[0]

        return closestNeighbor
