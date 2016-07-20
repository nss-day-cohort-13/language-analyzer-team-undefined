from textblob import TextBlob
from textblob.tokenizers import WordTokenizer

class Msg:
    '''
    Creating a new instance of Msg automatically parses the text and adds the sentiment, behavior, and domain analysis to the text.
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

    def tokenize_text(self, block):
        '''
        Runs the text string through Text Blobs tokenizer updates the words list and word count
        '''
        tokenizer = WordTokenizer()
        token = tokenizer.tokenize(block)
        self.words = token
        self.word_count = len(token)

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
        pass

    def analyze_domain(self, word_list):
        '''
        Query's domain lexicon to find the domains exhibited in the text
        '''
        pass
