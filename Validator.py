from Classifier import Classifier 
import pandas as pd 
import numpy as np 

class Validator:
    def __init__(self):
        pass

    def validate(self, features, dataset):
        if features == []:
            return 0

        classifier = Classifier(dataset)

        temp = classifier.df[features].copy()

        normalized_df = (temp-temp.mean())/temp.std()
        classifier.df = pd.concat([classifier.df.iloc[:, 0], normalized_df], axis=1)

        incorrect = 0
        npDf = classifier.df.to_numpy()

        for index, row in enumerate(npDf):
            if (classifier.test(index) != row[0]):
                incorrect += 1 

        # print(incorrect, len(classifier.df))
        return (len(npDf) - incorrect) / len(npDf)
