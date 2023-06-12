import numpy as np
import pandas as pd 
import sys

class Classifier:
    def __init__(self, filepath): 
        self.df = None
        self.train(filepath)

    def train(self, filepath):
        self.df = pd.read_csv(filepath, delim_whitespace=True, header=None, engine="python")

    def test(self, instance):
        min = sys.float_info.max
        closestNeighbor = -1
        npDf = self.df.to_numpy()

        temp = npDf[instance][1::]
        for index, row in enumerate(npDf):
            if (index != instance):
                distance = np.linalg.norm(row[1::] - temp)
                if distance < min:
                    min = distance
                    closestNeighbor = row[0]

        return closestNeighbor
