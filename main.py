from textblob import TextBlob
from textblob.tokenizers import WordTokenizer
from lexicons.behavior_lexicon import *
from lexicons.domain_lexicon import *


class Msg:

    '''
    Creating a new instance of Msg automatically parses the text and adds the sentiment, behavior
    and domain analysis to the text.
    '''

    def __init__(self, text):
        '''
        Initializes variables on creation of Msg and runs the functions to populate those variables
        '''
        self.text = text
        self.words = None
        self.word_count = 0
        self.sentiments = list()
        self.behaviors = list()
        self.domains = list()
        self.analyze = Analyze()

        self.tokenize_text(self.text)
        self.add_msg_sentiment(self.analyze.analyze_sentiment(self.text))
        self.add_msg_behavior(self.analyze.analyze_behavior(self.words))
        self.add_msg_domain(self.analyze.analyze_domain(self.words))

    def tokenize_text(self, block):
        '''
        Runs the text string through Text Blobs tokenizer updates the words list and word count
        '''
        tokenizer = WordTokenizer()
        token = tokenizer.tokenize(block)
        self.words = token
        self.word_count = len(token)
        return token

    def add_msg_sentiment(self, new_sentiment):
        '''
        adds the sentiment of the text to self.sentiments
        '''
        self.sentiments.append(new_sentiment)

    def add_msg_behavior(self, new_behavior):
        '''
        adds the behavior of the text to self.behavior
        '''
        self.behaviors.append(new_behavior)

    def add_msg_domain(self, new_domain):
        '''
        adds the domain of the text to self.domain
        '''
        self.domains.append(new_domain)


class Analyze:

    '''
    Analyze and Msg have a composition relationship. This class holds the logic for returning the sentiment, behavior, and domain
    '''

    def analyze_sentiment(self, text):
        '''
        Runs text through Text blob's sentiment analysis
        '''
        return TextBlob(text).sentiment

    def analyze_behavior(self, word_list):

        '''
        Query's behavior lexicon to find the behaviors exhibited in the text
        '''

        resultList = list()

        # for word in word_list:
        #     for key in behaviorDict:
        #         if word in key:
        #             resultList.append(behaviorDict[key])

        denominator = 0

        resultDict = dict()  # Make a temporary dictionary

        for word in word_list:

            for key in behaviorDict:  # test to see if a dictionary entry already exists

                if word in key:  # if word is found in the key

                    denominator += 1

                    # if word exists, update the dictionary to show another occurance of it.
                    if (behaviorDict[key] in resultDict):
                        resultDict[behaviorDict[key]] += 1

                    else:  # if not create one
                        resultDict[behaviorDict[key]] = 1
                        # print(resultDict[behaviorDict[key]])

        for key in resultDict:
            resultList.append((key, round(resultDict[key] / denominator, 4)))

        return resultList

    def analyze_domain(self, word_list):

        '''
        Query's domain lexicon to find the domains exhibited in the text
        '''

        resultList = list()

        denominator = 0

        resultDict = dict()  # Make a temporary dictionary

        for word in word_list:

            for key in domainDict:  # test to see if a dictionary entry already exists

                if word in key:  # if word is found in the key

                    denominator += 1

                    # if word exists, update the dictionary to show another occurance of it.
                    if (domainDict[key] in resultDict):
                        resultDict[domainDict[key]] += 1

                    else:  # if not create one
                        resultDict[domainDict[key]] = 1
                        # print(resultDict[behaviorDict[key]])

        for key in resultDict:
            resultList.append((key, round(resultDict[key] / denominator, 4)))

        # for word in word_list:
        #     for key in domainDict:
        #         if word in key:
        #             resultList.append(domainDict[key])

        return resultList
