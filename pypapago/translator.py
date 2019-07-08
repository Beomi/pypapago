import base64
import re
import requests
from multiprocessing import Pool, cpu_count
from functools import partial
from tqdm.auto import tqdm


class Translator:
    """
    Main Translator Class
    """

    def __init__(self, regex_pattern=None, headers=None):
        self.regex_pattern = re.compile(regex_pattern or '[가-힣]+')
        self.headers = headers or {
            'device-type': 'pc',
            'origin': 'https://papago.naver.com',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ko',
            'authority': 'papago.naver.com',
            'pragma': 'no-cache',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko)\
                           Chrome/75.0.3770.100 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'accept': 'application/json',
            'cache-control': 'no-cache',
            'x-apigw-partnerid': 'papago',
            'referer': 'https://papago.naver.com/',
            'dnt': '1',
        }
        self.SECRET_KEY = 'rlWxMKMcL2IWMPV6ImUwMWMwZWFkLWMyNDUtNDg2YS05ZTdiLWExZTZmNzc2OTc0MyIsImRpY3QiOnRydWUsImRpY3REaXNwbGF5Ijoz'
        self.QUERY_KEY = '0,"honorific":false,"instant":false,"source":"{source}","target":"{target}","text":"{query}"}}'

    @staticmethod
    def string_to_base64(s):
        """
        Generate Base64 Encoded string
        :param s: Origin Text (UTF-8)
        :return: B64 encoded text (B64, still UTF-8 string)
        """
        return base64.b64encode(s.encode('utf-8')).decode('utf-8')

    def translate(self, query, source='en', target='ko', verbose=False):
        """
        Main Translate function
        :param query: Original Text to translate
        :param source: Source(Original) text language [en, ko]
        :param target: Target text language [en, ko]
        :param verbose: Return verbose json data. Default: False
        :return: Translated text
        """
        data = {
            'data': self.SECRET_KEY + self.string_to_base64(
                self.QUERY_KEY.format(source=source, target=target, query=query)
            )
        }
        response = requests.post('https://papago.naver.com/apis/n2mt/translate', headers=self.headers, data=data)
        if not verbose:
            return response.json()['translatedText']
        return response.json()

    def bulk_translate(self, queries, source='en', target='ko', workers=None, verbose=False):
        """
        Call Translate function in parallel
        :param queries: List of query texts
        :param source: Source(Original) text language [en, ko]
        :param target: Target text language [en, ko]
        :param workers: Python multiprocessing workers. Default: vCPU cores
        :param verbose: Return verbose json data. Default: False
        :return: List of translated texts
        """
        with Pool(workers or cpu_count()) as pool:
            result = list(tqdm(pool.imap(
                func=partial(self.translate, source=source, target=target, verbose=verbose),
                iterable=queries
            ), total=len(queries)))
            pool.close()
            pool.join()
            return result
