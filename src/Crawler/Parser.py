'''
Created on 25/02/2014

@author: chengyu
'''



import demjson
import json

class TweetParser(object):
    
    def parseJsonString(self,jsonString):
        return demjson.decode(jsonString)
    
    def parseJsonStrings(self, jsonStrings, limit=0):
        returnList = []
        count = 0
        for jsonObject in jsonStrings:
            decodedJsonObject = demjson.decode(jsonObject)
            returnList.append(decodedJsonObject)
            count += 1
            if limit != 0 and count > limit :
                break
            
        return returnList
    
    def parseJsonStringsInFile(self, fileName, limit=0):
        file = open(fileName,"r")
        jsonStrings = []
       
        while True:
            jsonString = file.readline()
            
            if jsonString=="":
                break
            elif jsonString != "\n":
                jsonStrings.append(jsonString)
            
        jsonObjects = self.parseJsonStrings(jsonStrings)
        
        return jsonObjects
    
    def onlineParseFileToFile(self, inputJsonFileName, outputFileName, keys = ['created_at', 'id', 'text', 'lang']):
        inputFile = open(inputJsonFileName, "r") 
        outputFile = open(outputFileName, "w")
        
        while True:
            jsonString = inputFile.readline()
            
            try: 
                if jsonString=="":
                    break
                elif jsonString != "\n":
                    oldJsonObject = self.parseJsonString(jsonString)
                    newJsonDict = {}
                    for key in keys:
                        if oldJsonObject.__contains__(key):
                            newJsonDict[key] = oldJsonObject[key]
            except Exception as e:
                print e
                print "throw : " + jsonString 
            
            outputFile.write( json.dumps(newJsonDict)+"\n" )
            
    

if __name__ == '__main__':
    tweetParser = TweetParser()
    tweetParser.onlineParseFileToFile("/Users/chengyu/Documents/python/data/negativeTweetsForTraining", "/Users/chengyu/Documents/python/data/negativeSentimentTweetsInfo")
    
                    
                    
        
    
# if __name__ == '__main__':
#     tweetParser = TweetParser()
#     jasonObjects = tweetParser.parseJsonStringsInFile("positiveMiniSample")
#     
#     for jasonObject in jasonObjects:
#         print jasonObject['created_at'] + " "

                
                
        