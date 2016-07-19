import unittest

class TestMessage(unittest.TestCase):

    def test_initial_message_values(self):
        text = "Main courses were good, but the desserts were too sweet."
        message = Msg(text)

        self.assertIsInstance(message.domains, list)
        self.assertIsInstance(message.behaviors, list)
        self.assertIsInstance(message.sentiments, list)

        self.assertEqual(message.word_count, 12)
        # self.assertEqual(message.char_count, 56)
        self.assertListEqual(message.words, ["Main", "courses", "were", "good", ",", "but", "the", "desserts", "were", "too", "sweet", "."])
