import requests
import json
import time


API_KEY="f239b7ff-7cdb-464a-abf0-cfb2c1c7e287"
SUMMONER_BY_NAME="https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/"
STATS="https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/"

class APIRequester:
    def __init__(self, playersFile=""):
        self.key = API_KEY
        self.players = []
        self.playersFile = playersFile
        self.jsonFileName = "lol-"+playersFile
        self.outfile = open(self.jsonFileName, 'w')

    def api_summonerIdByName(self, summonerName):
        apiRequest=SUMMONER_BY_NAME+summonerName+"?api_key="+self.key
        r = requests.get(apiRequest)
        result = None
        try:
            result = str(r.json()[summonerName.replace(" ", "").lower()]["id"])
        except Exception, e:
            print "Key Error while getting summoner id by name"
            return None
        return result

    def api_stats(self, summonerId):
        if not summonerId:
            return None
        apiRequest=STATS+summonerId+"/ranked?season=SEASON2016&api_key="+self.key
        r = requests.get(apiRequest)
        try:
            _ = r.json()["champions"]
        except Exception, e:
            print "Key Error while requesting stats api"
            return None
        for champion in r.json()["champions"]:
            if champion["id"] == 0:
                return champion["stats"]
        return None

    def writeToFile(self):
        playersData = []
        with open(self.playersFile, 'r') as pFile:
            playersData = pFile.readlines()
        for playerData in playersData:
            player, prevRank, curRank = playerData.strip().split(",")
            print "=====Parsing summoner: {}, prevRank: {}, curRank: {}".format(player, prevRank, curRank)
            stats = self.api_stats(self.api_summonerIdByName(player))
            if not stats:
                print "\t!!!API request for summoner: {} failed".format(player)
                continue
            stats["prevRank"] = int(prevRank)
            stats["curRank"] = int(curRank)
            self.players.append(stats)
            time.sleep(3)
        json.dump(self.players, self.outfile)
        self.outfile.close()

    #need to be run after the write to the file is complete or before its run
    def readFromFile(self):
        readJson = None
        with open(self.jsonFileName, "r") as infile:
            readJson = json.loads(infile.read())
        return readJson
