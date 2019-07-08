import unittest
import re

from pypapago import Translator


class TestResponse(unittest.TestCase):
    def setUp(self):
        self.VERBOSE_KEYS = {'srcLangType', 'tarLangType', 'translatedText', 'dict', 'tarDict', 'tlit', 'delay',
                             'delaySmt', 'langDetection'}

    def test_create_instance(self):
        sample_re_pattern = re.compile('w+')
        translator = Translator(headers={'test': 1234}, regex_pattern=sample_re_pattern)
        assert translator.headers == {'test': 1234}
        assert translator.regex_pattern == sample_re_pattern

    def test_default_request(self):
        translator = Translator()
        assert translator.translate('Apple') == '사과'

    def test_verbose_request(self):
        translator = Translator()
        assert set(
            translator.translate('사과', verbose=True, source='ko', target='en').keys()
        ) == self.VERBOSE_KEYS

    def test_bulk_translate(self):
        translator = Translator()
        assert translator.bulk_translate(['apple', 'banana'] * 10) == ['사과', '바나나'] * 10
        # Test again with same Instance object
        assert translator.bulk_translate(['apple', 'banana'] * 10) == ['사과', '바나나'] * 10


if __name__ == '__main__':
    unittest.main()
