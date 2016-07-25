import re
from threading import *
from textblob import TextBlob
from textblob import Word
from textblob.tokenizers import WordTokenizer
from multiprocessing import Pool
from lexicons.behavior_lexicon import *
from lexicons.domain_lexicon import *
from stopwords import ignoredwords # used for ripping out words we wont use







class Msg:
    '''
    Creating a new instance of Msg automatically parses the text and adds the sentiment, behavior
    and domain analysis to the text.
    '''
    def __init__(self, text):
        '''
        Initializes variables on creation of Msg and runs the functions to populate those variables
        '''
        self.word_count = 0
        self.text = text
        self.words = list()
        self.sentiments = list()
        self.behaviors = list()
        self.domains = list()
        self.analysis = str
        self.analyze = Analyze()


    def tokenize_text(self, block):
        '''
        Runs the text string through Text Blobs tokenizer/lemmatizer
        '''
        def lemmatize_word(word):
            w = Word(word)
            return w.lemmatize().lower()
        tokenizer = WordTokenizer()
        token = tokenizer.tokenize(block)

        filtered_words = [word.lower() for word in token if word not in ignoredwords]
        results = list(map(lemmatize_word, filtered_words))
        # pool = Pool(5)
        # results = pool.map(self.lemmatize_word, token)
        # pool.close()
        # pool.join()
        return results

    def add_msg_words(self, token):
        '''
        adds tokenized words list to self.words, and adds the length of self.words to self.word_count
        '''
        self.words = token
        self.word_count = len(token)

    def add_msg_sentiment(self, new_sentiment):
        '''
        adds the sentiment of the text to self.sentiments
        '''
        self.sentiments = new_sentiment

    def add_msg_behavior(self, new_behavior):
        '''
        adds the behavior of the text to self.behavior
        '''
        self.behaviors.extend(new_behavior)

    def add_msg_domain(self, new_domain):
        '''
        adds the domain of the text to self.domain
        '''
        self.domains.extend(new_domain)

    def add_msg_analysis(self, new_analysis):
        '''
        adds text analysis output to self.analysis
        '''
        self.analysis = new_analysis

    def create_analysis_output(self):
        '''
        outputs behavior domains and sentiment analysis
        '''
        output = str()
        output += '\nSentiment:'
        for tup in self.sentiments:
            output += "\n  {0}: {1}".format(tup[0], tup[1])
        output += '\n'
        output += ('\nDomain:')
        for tup in self.domains:
            output += "\n  {0}: {1}".format(tup[0], tup[1])
        output += '\n'
        output += '\nBehavior:'
        for tup in self.behaviors:
            output += "\n  {0}: {1}".format(tup[0], tup[1])
        output += '\n'
        return(output)

    def initialize(self):
        '''
        Runs all tokenize/analysis methods and adds property values to self
        '''
        self.add_msg_words(self.tokenize_text(self.text))
        self.add_msg_sentiment(self.analyze.analyze_sentiment(self.text))
        self.add_msg_behavior(self.analyze.analyze_behavior(self.words))
        self.add_msg_domain(self.analyze.analyze_domain(self.words))
        self.add_msg_analysis(self.create_analysis_output())

class Analyze:
    '''
    Analyze and Msg have a composition relationship.
    This class holds the logic for returning the sentiment, behavior, and domain
    '''
    def analyze_sentiment(self, text):
        '''
        Runs text through Text blob's sentiment analysis
        '''
        raw_sentiment = str(TextBlob(text).sentiment)
        polarity = re.search('polarity=(.+?), ', raw_sentiment).group(1)
        subjectivity = re.search('subjectivity=(.+?)\)', raw_sentiment).group(1)
        polarity = round(float(polarity), 2)
        subjectivity = round(float(subjectivity), 2)
        return [('polarity', polarity), ('subjectivity', subjectivity)]

    def analyze_behavior(self, word_list):
        '''
        Query's behavior lexicon to find the behaviors exhibited in the text
        '''
        resultList = list()
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
        for key in resultDict:
            resultList.append((key, round(resultDict[key] / denominator, 2)))
        return list(reversed(sorted(resultList, key=lambda behavior: behavior[1])))

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
        for key in resultDict:
            resultList.append((key, round(resultDict[key] / denominator, 2)))
        return list(reversed(sorted(resultList, key=lambda domain: domain[1])))
