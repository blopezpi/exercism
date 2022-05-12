from typing import List

ordinals = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh",
            "eighth", "ninth", "tenth", "eleventh", "twelfth"]

gifts = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves, ",
    "three French Hens, ",
    "four Calling Birds, ",
    "five Gold Rings, ",
    "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ",
    "eight Maids-a-Milking, ",
    "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ",
    "eleven Pipers Piping, ",
    "twelve Drummers Drumming, "
]


def recite(start_verse, end_verse) -> List[str]:
    song = []
    for i in range(start_verse-1, end_verse):
        verse = ""
        verse += f'On the {ordinals[i]} day of Christmas my true love gave to me: '
        if i == 0:
            verse += "".join(list(reversed(gifts[0:i+1])))
        else:
            verse += "".join(list(reversed(gifts[1:i+1])))
            verse += f'and {gifts[0]}'
        song.append(verse)
    return song
