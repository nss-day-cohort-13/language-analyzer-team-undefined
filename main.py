from textblob import TextBlob
from textblob.tokenizers import WordTokenizer

class Msg:
    def __init__(self, text):
        self.text = text
        self.words = None
        self.word_count = 0
        self.tokenize_text(self.text)

        self.sentiments = list()
        self.behaviors = list()
        self.domains = list()

    def tokenize_text(self, block):
        tokenizer = WordTokenizer()
        token = tokenizer.tokenize(block)
        self.words = token
        self.word_count = len(token)

    def analyze_sentiment(self, word_list):
        pass

    def analyze_behavior(self, word_list):
        pass

    def analyzse_domain(self, word_list):
        pass
