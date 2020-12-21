"""Detect languages used in bulletins"""

import os
from collections import defaultdict

import langid
import pycountry

langid.set_languages(['fr', 'nl']) # forcing one of these languages

lang_dict = defaultdict(int)

root = "../data/txt/"
txts = os.listdir(root)
print(f"{len(txts)} TXT files found")

for txt in sorted(txts):
    txt = open(os.path.join(root, txt), encoding='utf-8').read()
    txt_length = len(txt)
    if txt_length > 11:
        lang, conf = langid.classify(txt)
        lang_dict[lang] += 1
    else:
        print(f"{txt} contains only {txt_length} characters, treating as unknown")
        lang_dict['n/a'] += 1

sorted_lang = sorted(lang_dict.items(), key=lambda kv: kv[1], reverse=True)

for lang_code, nb_docs in sorted_lang:
    language = pycountry.languages.get(alpha_2=lang_code)
    try:
        lang_name = language.name
    except AttributeError:
        lang_name = language
    print(f"{lang_name}\t{nb_docs}")
