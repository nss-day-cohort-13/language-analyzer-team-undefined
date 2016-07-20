import unittest
import main
import textblob
from lexicons.behavior_lexicon import behaviorDict
from lexicons.domain_lexicon import domainDict

class TestMessage(unittest.TestCase):

    def test_initial_message_values(self):
        text = "Main courses were good, but the desserts were too sweet."
        message = main.Msg(text)

        self.assertIsInstance(message.domains, list)
        self.assertIsInstance(message.behaviors, list)
        self.assertIsInstance(message.sentiments, list)

        self.assertEqual(message.word_count, 12)
        self.assertListEqual(message.words, ["Main", "courses", "were", "good", ",", "but", "the", "desserts", "were", "too", "sweet", "."])

    def test_add_msg_behavior(self):
        message = main.Msg("a")
        self.assertListEqual(list(), message.behaviors)
        message.add_msg_behavior("happy")
        self.assertListEqual(["happy"], message.behaviors)

    def test_add_msg_sentiment(self):
        text = "Main courses were good, but the desserts were too sweet."
        message = main.Msg(text)
        self.assertEqual(str(message.sentiments), "[Sentiment(polarity=0.4055555555555555, subjectivity=0.5277777777777778)]")

    def test_add_msg_domain(self):
        message = main.Msg("a")
        self.assertListEqual(list(), message.domains)
        message.add_msg_domain("happy")
        self.assertListEqual(["happy"], message.domains)


class TestAnalyze(unittest.TestCase):

    def test_analyze_sentiment(self):
        text = "Main courses were good, but the desserts were too sweet."
        analyze = main.Analyze()
        sentiment_test = analyze.analyze_sentiment(text)
        self.assertEqual(str(sentiment_test), 'Sentiment(polarity=0.4055555555555555, subjectivity=0.5277777777777778)')

    def test_analyze_behavior(self):
        analyze = main.Analyze()
        text = "The main courses were good, but the desserts were too sweet."
        message = main.Msg(text).words
        behaviors = analyze.analyze_behavior(message)
        self.assertListEqual(behaviors, ["encouragement", "encouragement"])

    def test_analyze_domain(self):
        analyze = main.Analyze()
        text = "The main courses were good, but the desserts were too sweet."
        message = main.Msg(text).words
        domains = analyze.analyze_domain(message)
        self.assertListEqual(domains, ["behavioral",])


class TestLexicons(unittest.TestCase):

    def test_behaviorDict_is_dictionary(self):
        self.assertIsInstance(behaviorDict, dict)

    def test_behaviorDict_contains_key(self):
        self.assertIn(('cautious', 'hopeful', 'prone', 'fearful', 'scared', 'fear', 'blessing'), behaviorDict)

    def test_behaviorDict_contains_value(self):
        self.assertEqual(behaviorDict[('cautious', 'hopeful', 'prone', 'fearful', 'scared', 'fear', 'blessing')], 'passive')

    def test_domainDict_is_dictionary(self):
        self.assertIsInstance(domainDict, dict)

    def test_domainDict_contains_key(self):
        self.assertIn(('date', 'day', 'time', 'minute', 'today', 'night', 'moment', 'year'), domainDict)

    def test_domainDict_contains_value(self):
        self.assertEqual(domainDict[('date', 'day', 'time', 'minute', 'today', 'night', 'moment', 'year')], "time")


if __name__ == '__main__':
    unittest.main()
