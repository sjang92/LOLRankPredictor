import rank_predictor.Predictor as Predictor
import features.featureExtractor as FeatureExtractor

def main():
    # 1) Get Data from LOL API 
    # TODO : import relevant modules and pull data as json format

    X = [] # list of dictionaries
    Y = [] # list of values
    features = X[0].keys() # list of feature names in string. 
    #TODO: Make sure X[0] has all attrs as keys. Else, add a manual list of all feature names


    # 2) Filter and add features
    f_extractor = FeatureExtractor(features)
    f_extractor.feedData(X, Y)

    featuresToRemove = [] # list of features to remove. Let's eyeball it
    unaryFeatures = [] #example : ('averagekills', 'newfeaturename', lambda a: math.pow(a, 2))
    binaryFeatures = [] #example : ('averagekills', 'averagedeaths', 'newname',lambda a, b : a*b)

    f_extractor.removeFeatures(featuresToRemove)

    for (f_name, new_name, func) in unaryFeatures:
        f_extractor.addUnaryFeature(f_name, new_name, func)

    for (f1, f2, new_name, func) in binaryFeatures:
        f_extractor.addCrossFeature(f1, f2, new_name, func)

    # 3) Cross Validate : 9 to 1
    f_extractor.divideData(10) # divide into 10 chunks

    for i in range(0, 10):
        train, test = f_extractor.getTrainTestData([i])
        train_X, train_Y = f_extractor.separateXY(train)
        test_X, test_Y = f_extractor.separateXY(test)

        predictor = Predictor(train_X, train_Y)
        predictor.setLearner('svm') # only support svm for now
        predictor.learn()

        print predictor.predictAndGetError(test_X, test_Y)


if __name__ == "__main__":
    main()