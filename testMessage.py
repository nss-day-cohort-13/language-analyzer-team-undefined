import unittest
import main
import textblob

class TestMessage(unittest.TestCase):

    def test_initial_message_values(self):
        text = "Main courses were good, but the desserts were too sweet."
        message = main.Msg(text)

        self.assertIsInstance(message.domains, list)
        self.assertIsInstance(message.behaviors, list)
        self.assertIsInstance(message.sentiments, list)

        self.assertEqual(message.word_count, 12)
        self.assertListEqual(message.words, ["Main", "courses", "were", "good", ",", "but", "the", "desserts", "were", "too", "sweet", "."])

    def test_tokenize_text(self):
        # new instance of class Msg created with arbitrary value 'a'
        # to test the functionality of its tokenize_text method
        message = main.Msg('a')
        text = "Main courses were good, but the desserts were too sweet."
        test_token = message.tokenize_text(text)
        self.assertListEqual(test_token, ["Main", "courses", "were", "good", ",", "but", "the", "desserts", "were", "too", "sweet", "."])
        self.assertEqual(len(test_token), 12)

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

    def test_analize_sentiment(self):
        text = "Main courses were good, but the desserts were too sweet."
        analyze = main.Analyze()
        sentiment_test = analyze.analyze_sentiment(text)
        self.assertEqual(str(sentiment_test), 'Sentiment(polarity=0.4055555555555555, subjectivity=0.5277777777777778)')

    def test_analize_behavior(self):
        analyze = main.Analyze()
        text = "The main courses were good, but the desserts were too sweet."
        message = main.Msg(text).words
        behaviors = analyze.analyze_behavior(message)
        self.assertListEqual(behaviors, ["encouragement", "encouragement"])

    def test_analize_domain(self):
        analyze = main.Analyze()
        text = "The main courses were good, but the desserts were too sweet."
        message = main.Msg(text).words
        domains = analyze.analyze_domain(message)
        self.assertListEqual(domains, ["behavioral",])


if __name__ == '__main__':
    unittest.main()
