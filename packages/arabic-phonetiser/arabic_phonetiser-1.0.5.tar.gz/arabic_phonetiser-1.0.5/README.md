# Arabic Phonetiser

## Introduction

This package is a Python library for phonetising Arabic text, with a focus on dialects like the Iraqi dialect. It is a fork of Nawar Halabi's [Arabic-Phonetiser](https://github.com/nawarhalabi/Arabic-Phonetiser), but differs in that it is simplified and includes characters commonly used in Arabic dialects.

## Features

- **Simplified Phonetisation**: The phonetisation process has been simplified.

- **Support for Additional Arabic Characters**: This package extends the standard Arabic character set to include characters that are specific to various Arabic dialects, such as the Iraqi dialect. These additional characters are:
    - Buckwalter: `u'C'`, Arabic Script: 'چ'
    - Buckwalter: `u'G'`, Arabic Script: 'گ'
    - Buckwalter: `u'P'`, Arabic Script: 'پ'
    - Buckwalter: `u'V'`, Arabic Script: 'ڤ'
    - Buckwalter: `u'ı'`, Arabic Script: 'ـ', known as Taweel, used here as a vowel. Pronunciation is similar to 'ı' in Turkish.
    - Buckwalter: `u'L'`, Arabic Script: 'ڵ'
    - Buckwalter: `u'O'`, Arabic Script: 'ۆ'
    - Buckwalter: `u'e'`, Arabic Script: 'ێ'

    
- **Utilizes the [arabic-buckwalter-transliteration](https://github.com/hayderkharrufa/arabic-buckwalter-transliteration/tree/main) package for supporting these new characters.**

## Installation

```bash
pip install arabic-phonetiser
```

## Usage

Here is a simple example:

```python
import arabic_phonetiser

arabic_text = "أگُلّـچْ يَبـنْتي وأَسَمْعـچْ يَچَنْتي"
phon_text = arabic_phonetiser.arabic_to_phonemes(arabic_text)
print(phon_text)
```

Output:

```
< a G u0 ll ı C + y a b ı n t ii0 + uu0 < a s a m E ı C + y a C a n t ii0
```

## License

This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License. The original work is by Nawar Halabi. For the full license text, please see the LICENSE file in the repository.

## Acknowledgements

This work is a fork of [Nawar Halabi's Arabic-Phonetiser](https://github.com/nawarhalabi/Arabic-Phonetiser). Special thanks to Nawar Halabi for the original work.
