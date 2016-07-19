import unittest
import main

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
        pass

    def test_add_msg_sentiment(self):
        pass

    def test_add_msg_domain(self):
        pass


class TestAnalyze(unittest.TestCase):

    def test_analize_sentiment(self):
        pass

    def test_analize_behavior(self):
        pass

    def test_analize_domain(self):
        pass





if __name__ == '__main__':
    unittest.main()
