from rank_predictor import Predictor as Predictor
from features import featureExtractor as FeatureExtractor

def main():
    # 1) Get Data from LOL API 
    # TODO : import relevant modules and pull data as json format

    X = [] # list of dictionaries
    Y = [] # list of values
    #features = X[0].keys() # list of feature names in string. 
    #TODO: Make sure X[0] has all attrs as keys. Else, add a manual list of all feature names

    X = [
    {u'totalPhysicalDamageDealt': 3488663, u'totalTurretsKilled': 52, u'totalSessionsPlayed': 74, u'totalAssists': 651, u'totalDamageDealt': 6379287, u'mostChampionKillsPerSession': 18, u'killingSpree': 159, u'totalPentaKills': 0, u'mostSpellsCast': 0, u'totalDoubleKills': 29, u'maxChampionsKilled': 18, u'totalQuadraKills': 1, u'totalDeathsPerSession': 367, u'totalSessionsWon': 39, u'totalGoldEarned': 773400, u'totalTripleKills': 3, u'totalNeutralMinionsKilled': 626, u'maxTimeSpentLiving': 1652, u'rankedPremadeGamesPlayed': 0, u'rankedSoloGamesPlayed': 0, u'maxLargestCriticalStrike': 1935, u'totalChampionKills': 321, u'maxNumDeaths': 12, u'totalMinionKills': 8349, u'totalMagicDamageDealt': 2661657, u'totalHeal': 335855, u'normalGamesPlayed': 0, u'maxLargestKillingSpree': 11, u'totalUnrealKills': 0, u'maxTimePlayed': 2795, u'totalDamageTaken': 1562841, u'botGamesPlayed': 0, u'totalSessionsLost': 35, u'totalFirstBlood': 0},
{u'totalPhysicalDamageDealt': 25352467, u'totalTurretsKilled': 341, u'totalSessionsPlayed': 454, u'totalAssists': 4560, u'totalDamageDealt': 45458680, u'mostChampionKillsPerSession': 18, u'killingSpree': 1179, u'totalPentaKills': 0, u'mostSpellsCast': 0, u'totalDoubleKills': 165, u'maxChampionsKilled': 18, u'totalQuadraKills': 4, u'totalDeathsPerSession': 2161, u'totalSessionsWon': 239, u'totalGoldEarned': 5179999, u'totalTripleKills': 19, u'totalNeutralMinionsKilled': 16068, u'maxTimeSpentLiving': 2584, u'rankedPremadeGamesPlayed': 0, u'rankedSoloGamesPlayed': 0, u'maxLargestCriticalStrike': 1864, u'totalChampionKills': 2187, u'maxNumDeaths': 14, u'totalMinionKills': 33286, u'totalMagicDamageDealt': 16667479, u'totalHeal': 2975599, u'normalGamesPlayed': 0, u'maxLargestKillingSpree': 14, u'totalUnrealKills': 0, u'maxTimePlayed': 3761, u'totalDamageTaken': 11292612, u'botGamesPlayed': 0, u'totalSessionsLost': 215, u'totalFirstBlood': 0}
    ]
    Y = [13, 16]
    features = X[0].keys()




    # 2) Filter and add features
    f_extractor = FeatureExtractor(features)
    f_extractor.feedData(X, Y)

    X, Y = f_extractor.separateXY(f_extractor.data)
    print X
    print Y
    predictor = Predictor(X, Y)
    predictor.setLearner('svm')
    predictor.learn()
    print predictor.predict(X)

    featuresToRemove = [] # list of features to remove. Let's eyeball it
    unaryFeatures = [] #example : ('averagekills', 'newfeaturename', lambda a: math.pow(a, 2))
    binaryFeatures = [] #example : ('averagekills', 'averagedeaths', 'newname',lambda a, b : a*b)
    """
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
    """

if __name__ == "__main__":
    main()