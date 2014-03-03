'''
Created on 24/02/2014

@author: chengyu
'''


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# OQrOsQkuiXFH5dUrCKHfvg
# 7pF6PH6PFGeBLlAHsxMbTGinw2bfYIw4aF6vwWsLok
# 781737260-uJejBgaVA8NDGxj6oipjlp6K7fl89fvQdJQS6357
# TZUCXTGg2SRBplHPaTs0aht2gGIsIwaRX1v6hBRSfJrzj

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="OQrOsQkuiXFH5dUrCKHfvg"
consumer_secret="7pF6PH6PFGeBLlAHsxMbTGinw2bfYIw4aF6vwWsLok"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="781737260-uJejBgaVA8NDGxj6oipjlp6K7fl89fvQdJQS6357"
access_token_secret="TZUCXTGg2SRBplHPaTs0aht2gGIsIwaRX1v6hBRSfJrzj"


positiveEmoticons = ":),:-),:),:D,=)"
negativeEmoticons = ":(, :-(, : ("

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
This is a basic listener that just prints received tweets to stdout.

"""
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


class FileOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
This is a basic listener that just prints received tweets to stdout.

"""
    def __init__(self, fileName):
        self.outPutFile = open(fileName,"w")
    
    def on_data(self, data):
        self.outPutFile.write(data+'\n')
    
    def recordStream(self, features):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)
        stream.filter(track=features)



        


if __name__ == '__main__':
    l = FileOutListener('positiveTweetsForTrainingBig')
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
 
    stream = Stream(auth, l)
#     stream.filter(track=[positiveEmoticons])
    stream.filter(track=[positiveEmoticons])

    

