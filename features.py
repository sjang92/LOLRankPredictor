import numpy
from random import shuffle

class featureExtractor():

    # Example : extractor = featureExtractor(data[0].keys())
    def __init__(self, raw_features):
        self.features = raw_features
        self.data = []
        self.num_data = 0
        self.dimension = len(self.raw_features)
        self.divded_data = []

    """
    Function : feedData
    feed the list of json(python dict) objects that represent the training data
    After calling this function, the extractor has access to the train data in 
    vector format. 
    """
    def feedData(self, X, Y):
        assert len(X) == len(Y), "len of X does not equal len of Y"

        self.num_data = len(X)

        for i in range(0, self.num_data):
            x = X[i]
            y = Y[i]
            new_vector = []

            for feature in self.raw_features:
                new_vector.append(x[feature])

            self.data.append((new_vector, y))

    """
    Adds a new feature from the existing ones according to the func.
    Add the correct value to all data vectors. Pass in lambda
    """
    def addUnaryFeature(self, feature, new_feature, func):
        assert feature in self.features, "such feature does not exist"

        idx = self.features.index(feature)
        self.features.append(new_feature)

        for data in self.data:
            x = data[0]
            x.append(func(x[idx]))

        self.dimension += 1
    """
    Removes a single feature from the existing ones
    """
    def removeSingleFeature(self, feature):
        assert feature in self.features, "such feature does not exist"

        idx = self.features.index(feature)
        self.features.pop(idx)

        for data in self.data:
            x = data[0]
            x.pop(idx)

        self.dimension -= 1
    """
    Removes multiple features from the existing ones
    """
    def removeFeatures(self, feature_list):
        indices = []
        all_exists = True
        for feature in feature_list:
            assert feature in self.features, "feature "+feature+" does not exist"
            indices.append(self.features.index(feature))

        indices.sort(reverse=True)

        for idx in indices:
            self.features.pop(idx)

        for data in self.data:
            x = data[0]
            for idx in indices:
                x.pop(idx)

        self.dimension -= len(indices)
    """
    Adds a new feature from two existing features. Add binary combination
    of the two. Pass in lambda
    """
    def addCrossFeature(self, feature_a, feature_b, new_feature, func):
        assert feature_a in self.features and feature_b in self.features, "such features do not exist"

        idx_a = self.features.index(feature_a)
        idx_b = self.features.index(feature_b)
        self.features.append(new_feature)

        for data in self.data:
            x = data[0]
            x.append(func(x[idx_a], x[idx_b]))
        self.dimension += 1
    """
    Run varianceFiltering to the features. 
    By default, if var_threhold is not passed in, it removes features with zero variance.
    """
    def varianceFilter(self, var_threshold=0):
        return NotImplemented
        #self.data = VarianceThreshold(threshold=var_threshold).fit_transform(self.data)

    """
    Function : getFeatureVector
    Given a json(dictionary) representation of a data, return the vector version
    whose index corresponds to the index of the feature
    vector[i] = x[self.features[i]]
    """
    def getFeatureVector(self, x):
        return NotImplemented

    """
    Function : divideData
    Divides the entire dataset into num_chunks and store them in separate arrays.
    """
    def divideData(self, num_chunks):
        rand_indices = shuffle(range(0, self.num_data))
        num_per_chunk = self.num_data / num_chunks
        rand_lists = [rand_indices[i: i+num_per_chunk] for i in xrange(0, self.num_data, num_per_chunk)]
        # distribute left-overs
        if len(rand_lists) > num_chunks:
            last_chunk = rand_lists[-1]
            for i in range(0, len(last_chunk)):
                rand_lists[i].append(last_chunk[i])
            # Remove the last one once we've distributed its elements
            rand_lists.pop(-1)

        self.divided_data = [None] * len(rand_lists)
        assert len(rand_lists) == num_chunks, "Something is wrong with this function"

        for i in range(0, num_chunks):
            self.divided_data[i] = [self.data[j] for j in rand_lists[i]]

    """
    Function : getTrainTestData

    """
    def getTrainTestData(self, indices):
        train = test = []

        test = self.divided_data[idx]

        for i in indices:
            test.extend(self.divided_data[i])

        rg = [i for i in range(0, len(self.divided_data)) if i not in indices]
        for i in rg:
            train.extend(self.divided_data[i])

        return train, test

    """
    Function : separate XY
    """
    def separateXY(self, data_vector):
        X = Y = []
        for i in range(0, len(data_vector)):
            (x, y) = data_vector[i]
            X.append(x)
            Y.append(y)
        return X, Y