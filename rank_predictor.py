from sklearn.svm import SVC


"""
Class : Predictor
==============================================================================
Train
Predict given x values that are array of array of vectors
"""
class Predictor(object):

    # initialize the MMR Predictor
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.classifier = None

    def setLearner(self, learner_name):
        if learner_name == 'svm':
            self.learner = SVC() 

    def learn(self):
        self.learner.fit(self.X, self.Y)

    def predict(self, testX):
        return self.learner.predict(testX)

    def predictAndGetError(self, testX, trueY):
        return self.learner.score(testX, trueY)
