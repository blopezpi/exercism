import re


def abbreviate(words):
    words = re.sub(r'[_-]', " ", words)
    return "".join([word[0].upper() for word in words.split()])
