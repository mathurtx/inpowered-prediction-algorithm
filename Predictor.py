
# coding: utf-8

# In[ ]:

import FeatureExtractor

def predictor(model,authorId,summary):
    featureExtractor = FeatureExtractor()
    featureExtractor.authorFinder(authorId)
    featureExtractor.similarityFinder(summary)
    return model.predict(featureExtractor.X)

#
# Currently mocking the functionality
#
def predictormock(model,authorId,summary):
    return "Model Output : 560"
    

