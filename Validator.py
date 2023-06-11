from Classifier import Classifier 
from Node import Node 
import pandas as pd 
import numpy as np 

class Validator:
    def __init__(self):
        pass

    def validate(self, features, dataset):
        classifier = Classifier(dataset)

        temp = classifier.df[features].copy()

        normalized_df = (temp-temp.mean())/temp.std()
        classifier.df = pd.concat([classifier.df.iloc[:, 0], normalized_df], axis=1)

        incorrect = 0
        print("loop")
        for index, row in classifier.df.iterrows():
            if (classifier.test(index) != row[0]):
                incorrect += 1 

        print(incorrect, len(classifier.df))
        return incorrect / len(classifier.df)
