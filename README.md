# THIS PROJECT is ARCHIVED!

This project is no longer maintained by the author.
No additional support is provided.

If you're still interested in the Papago's translation service, plz follow the direction below:

https://developers.naver.com/docs/papago/papago-nmt-overview.md

---

# pypapago [![codecov](https://codecov.io/gh/Beomi/pypapago/branch/master/graph/badge.svg)](https://codecov.io/gh/Beomi/pypapago)

Unofficial python wrapper for [papago translate service](https://papago.naver.com).

## Install

```bash
pip install -U pypapago
```

## Usage

### Basic usage (English to Korean)

```python
from pypapago import Translator

translator = Translator()

result = translator.translate('I am GROOT')
print(result) # 나는 그루트다
```

### Set Source/Target Language

```python
from pypapago import Translator

translator = Translator()

result = translator.translate(
    '카카오는 파파고를 좋아해',
    source='ko',
    target='en',
)
print(result) # Kakao likes papago.
```

#### Supported Language Codes

Code | Desc 
--|--
ko | Korean
en | English
ja | Japanese
zh-CN | Chinese
zh-TW | Chinese traditional
es | Spanish
fr | French
vi | Vietnamese
th | Thai
id | Indonesia


### Bulk Translation

Parallel bulk translation with Multiprocessing.

```python
from pypapago import Translator

translator = Translator()

result = translator.bulk_translate(['apple', 'banana'])
print(result) # ['사과', '바나나']
```

You can also set how many workers to run manually.

(The more workers make your code faster but requires more system resources.)

Default to CPU Cores (HyperThreading = x2)

- ex) Run with 2cores

```python
from pypapago import Translator

translator = Translator()

result = translator.bulk_translate(
    ['apple', 'banana'], 
    workers=2
)
print(result) # ['사과', '바나나']
```

### Verbose output

If you need raw result from papago API, you can set `verbose` to `True`.

```python
from pypapago import Translator

translator = Translator()

result = translator.translate('I am GROOT', verbose=True)
print(result) # RAW JSON Result
#{'delay': 400,
# 'delaySmt': 400,
# 'dict': {'items': [{'entry': '<b>I</b>',
# ...
# 'translatedText': '나는 그루트다'}
#}
```

Detail results may change.
