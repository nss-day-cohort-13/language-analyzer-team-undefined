# from textblob import TextBlob
# from textblob.sentiments import NaiveBayesAnalyzer
# from textblob.tokenizers import SentenceTokenizer
# from textblob.tokenizers import WordTokenizer
# from textblob.taggers import NLTKTagger
# from textblob.taggers import PatternTagger

from messages import messages

from lexicons.behavior_lexicon import *

# def code():

uniqueSet = set()


def chopMessages():
    # for entry in messages:
    #     word = entry["message"].split()
        
    #     if word != ',' and word != '.':
    #         uniqueSet.update(word)

    # print(uniqueSet)



    # msg = TextBlob("I expect to see some awesome Trello boards")
    # print(msg.sentiment)

    # analyzer = NaiveBayesAnalyzer()
    # print(analyzer.analyze("It was the best of times, it was the worst of times."))

    # tokenizer = WordTokenizer()
    # token = tokenizer.tokenize("It was good for a time, it was the worst of times. It was very beautifully made")
    # tagger = PatternTagger()
    # print(tagger.tag("It was good for a time, it was the worst of times. It was very beautifully made"))

    # wordPool = set()

    # wordPool = (sorted(tagger.tag(uniqueSet), key=lambda x: x[1]))
    # print(wordPool)

    # for tup in wordPool:
        # if (tup[1] != 'POS' and tup[1] != ',' and tup[1] != '.' and tup[1] != "\"" and tup[1] != ")" and tup[1] != ":"):
        #     print(tup)
        # if (tup[1] == 'JJ' or tup[1] == 'JJS' or tup[1] == 'RB' or tup[1] == 'VBN'):
            # print('\'{0}\''.format(tup[0]))
            # pass


    # print("nouns here")

    # for tup in wordPool:
    #     if (tup[1] == 'NN' or tup[1] == "NNS"):
    #         pass
            # print('\'{0}\''.format(tup[0]))
            # print(tup)

    # print(behaviorDict)

    response = input("Please enter behavior search string: ")

    for key in behaviorDict:
        if response in key:
            print(behaviorDict[key])
    # next(v for k, v in behavior_dict if 'positive' in k)



if __name__ == '__main__':
    chopMessages()

# import code
# code.interact(local=locals())