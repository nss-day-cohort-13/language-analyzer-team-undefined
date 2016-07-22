import main
import unittest
import textblob
from lexicons.behavior_lexicon import behaviorDict
from lexicons.domain_lexicon import domainDict


class TestMessage(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        text = 'The main courses were good, but the desserts were too sweet.'
        self.message = main.Msg(text)
        self.message.initialize()

    def test_initial_message_values(self):
        text = 'The main courses were good, but the desserts were too sweet.'
        message = main.Msg(text)
        self.assertEqual(message.word_count, 0)
        self.assertEqual(message.text, 'The main courses were good, but the ' +
        'desserts were too sweet.')
        self.assertListEqual(message.words, list())
        self.assertListEqual(message.sentiments, list())
        self.assertListEqual(message.behaviors, list())
        self.assertListEqual(message.domains, list())
        self.assertEqual(message.analysis, str)
        self.assertIsInstance(message.analyze, main.Analyze().__class__)

    def test_tokenize_text(self):
        text = 'The main courses were good, but the desserts were too sweet.'
        test_token = self.message.tokenize_text(text)
        self.assertListEqual(test_token, ['The', 'main', 'course', 'were',
        'good', ',', 'but', 'the', 'dessert', 'were', 'too', 'sweet', '.'])
        self.assertEqual(len(test_token), 13)

    def test_add_msg_words(self):
        # new instance of class Msg created with arbitrary value 'a'
        message = main.Msg('a')
        test_words = ['The', 'main', 'course', 'were', 'good', ',', 'but',
        'the', 'dessert', 'were', 'too', 'sweet', '.']
        message.add_msg_words(test_words)
        self.assertEqual(test_words, message.words)
        self.assertEqual(len(test_words), message.word_count)

    def test_add_msg_behavior(self):
        # new instance of class Msg created with arbitrary value 'a'
        message = main.Msg('a')
        test_behaviors = ['cautious', 'hopeful', 'prone']
        message.add_msg_behavior(test_behaviors)
        self.assertListEqual(['cautious', 'hopeful', 'prone'], message.behaviors)

    def test_add_msg_sentiment(self):
        # new instance of class Msg created with arbitrary value 'a'
        message = main.Msg('a')
        test_sentiments = [('polarity', 0.41), ('subjectivity', 0.53)]
        message.add_msg_sentiment(test_sentiments)
        self.assertEqual(test_sentiments, message.sentiments)

    def test_add_msg_domain(self):
        # new instance of class Msg created with arbitrary value 'a'
        message = main.Msg('a')
        test_domains = ['date', 'day', 'time']
        message.add_msg_domain(test_domains)
        self.assertListEqual(['date', 'day', 'time'], message.domains)

    def test_add_msg_analysis(self):
        # new instance of class Msg created with arbitrary value 'a'
        message = main.Msg('a')
        test_analysis = 'this is a test analysis'
        message.add_msg_analysis(test_analysis)
        self.assertEqual(test_analysis, message.analysis)

    def test_create_analysis_output(self):
        expected_output = ('\nSentiment:' +
        '\n  polarity: 0.41' +
        '\n  subjectivity: 0.53' +
        '\n' +
        '\nDomain:' +
        '\n  behavioral: 1.0' +
        '\n' +
        '\nBehavior:' +
        '\n  encouragement: 0.67' +
        '\n  comparison: 0.33' +
        '\n')
        msg_analysis_output = self.message.create_analysis_output()
        self.assertEqual(expected_output, msg_analysis_output)


class TestAnalyze(unittest.TestCase):

    def test_analyze_sentiment(self):
        text = 'The main courses were good, but the desserts were too sweet.'
        message = main.Msg(text)
        analyze = main.Analyze()
        sentiments = analyze.analyze_sentiment(message.text)
        self.assertEqual(sentiments, [('polarity', 0.41), ('subjectivity', 0.53)])

    def test_analyze_behavior(self):
        text = 'The main courses were good, but the desserts were too sweet.'
        message = main.Msg(text)
        message.add_msg_words(message.tokenize_text(message.text))
        analyze = main.Analyze()
        behaviors = analyze.analyze_behavior(message.words)
        self.assertListEqual(behaviors, [('encouragement', 0.67), ('comparison', 0.33)])

    def test_analyze_domain(self):
        text = 'The main courses were good, but the desserts were too sweet.'
        message = main.Msg(text)
        message.add_msg_words(message.tokenize_text(message.text))
        analyze = main.Analyze()
        domains = analyze.analyze_domain(message.words)
        self.assertListEqual(domains, [('behavioral', 1.0)])


class TestLexicons(unittest.TestCase):

    def test_behaviorDict_is_dictionary(self):
        self.assertIsInstance(behaviorDict, dict)

    def test_behaviorDict_contains_key(self):
        self.assertIn(('cautious', 'hopeful', 'prone', 'fearful', 'scared',
        'fear', 'blessing', 'quiet', 'static', 'uninvolved', 'flat', 'idle',
        'patient', 'compliant', 'docile', 'inert', 'latent', 'receptive',
        'resigned', 'stolid', 'Hannah', 'submissive', 'tractable', 'unassertive',
        'indifferent', 'languid', 'stoic', 'apathetic',
        'wish'), behaviorDict)

    def test_behaviorDict_contains_value(self):
        self.assertEqual(behaviorDict[('cautious', 'hopeful', 'prone', 'fearful',
        'scared', 'fear', 'blessing', 'quiet', 'static', 'uninvolved', 'flat',
        'idle', 'patient', 'compliant', 'docile', 'inert', 'latent', 'receptive',
        'resigned', 'stolid', 'Hannah', 'submissive', 'tractable', 'unassertive',
        'indifferent','languid', 'stoic', 'apathetic', 'wish')], 'passive')

    def test_domainDict_is_dictionary(self):
        self.assertIsInstance(domainDict, dict)

    def test_domainDict_contains_key(self):
        self.assertIn(('date', 'day', 'time', 'minute', 'today', 'night', 'moment',
        'year', 'calender', 'clock', 'hour', 'noon', 'midnight', 'afternoon',
        'tonight', 'tomorrow', 'morning', 'week', 'month'), domainDict)

    def test_domainDict_contains_value(self):
        self.assertEqual(domainDict[('date', 'day', 'time', 'minute', 'today',
        'night', 'moment', 'year', 'calender', 'clock', 'hour', 'noon',
        'midnight', 'afternoon', 'tonight', 'tomorrow', 'morning', 'week',
        'month')], 'time')


if __name__ == '__main__':
    unittest.main()
