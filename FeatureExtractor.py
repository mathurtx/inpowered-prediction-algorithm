
# coding: utf-8

# In[ ]:

import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

class FeatureExtractor:
    
    def __init__(self):
        self.name = "FeatureExtractor"
        self.X = []
        
    def authorEventsRatioReader(self,filename):
        authorEventsRatio = pd.read_csv(filename,delimiter=",")
        authorEventsRatioDict = authorEventsRatio.to_dict()
        return authorEventsRatioDict
    
    def authorFinder(self,authorId):
        authorEventsRatioReader('AuthorEventsRatio.csv')
        if authorEvents in authorEventsRatioDict.keys():
            value = authorEventsRatioDict[authorId]
            self.X.append(value)
    
    def topicFinder(self,summary,ldaTopicSet):
        summaryOverlap = []
        le = clf = joblib.load('lda.pkl') 
        tempList = summary.split(" ")
        topicReduced = " ".join([str(val) for val in tempList if val in label_encoder_list])
        if topicReduced != '':
            summaryOverlap.append(topicReduced)
        self.X.append(le.transform(summaryOverlap))
        
    def similarityFinder(self,summary):
        #vectorizer = joblib.load("vectorizer.pk")
        #tfidf = vectorizer.transform(summary)
        #self.X.append(tfidf)
	return 1
        
    def addAuthorId(authorId):
        self.X.append(authorId)

