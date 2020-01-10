import re
import MeCab
import mojimoji


def tokenize(sentence: str, tagger: MeCab.Tagger, stopwords: list,
             target_parts_of_speech: list) -> list:
    sentence = re.sub(r'https?://[\w/:%#\$&\?~\.=\+\-]+', '', sentence)

    tokenized_sentence = []
    regex = re.compile(r'\d')
    regax_one = re.compile(r"^\w$")
    try:
        for chunk in tagger.parse(sentence).splitlines()[:-1]:
            (surface, feature) = chunk.split('\t')
            if feature.startswith(target_parts_of_speech):
                if surface not in stopwords:
                    if not regex.search(surface) and not regax_one.search(
                            surface):
                        word = word_normiraze(surface)
                        tokenized_sentence.append(word)
    except Exception:
        return []

    return tokenized_sentence


def word_normiraze(word: str) -> str:
    word = word.lower()
    word = mojimoji.han_to_zen(word, ascii=False, digit=False)
    word = mojimoji.zen_to_han(word, kana=False)

    return word
