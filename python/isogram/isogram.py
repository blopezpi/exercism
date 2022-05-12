import re


def is_isogram(string):
    string = string.lower()
    string = re.sub(r"[^a-z]", "", string.lower())
    return len(set(string)) == len(string)
