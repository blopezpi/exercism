import re
from typing import Dict
from collections import Counter


def count_words(sentence) -> Dict[str, int]:
    sentence = re.findall('[a-z0-9]+(?:\'[a-z])?', sentence.lower())
    count = Counter(sentence)
    return dict(count)
