import re

list_count = 0


def create_list(how_many, sentence, list_count):
    if list_count == 1:
        return f"<ul><li>{sentence}</li>"
    elif list_count == how_many:
        return f"<li>{sentence}</li></ul>"
    else:
        return f"<li>{sentence}</li>"


def italic_bold_word(line):
    line = re.sub(r'__([a-zA-Z0-9\s]+)__', r'<strong>\1</strong>', line)
    line = re.sub(r'_([a-zA-Z0-9\s]+)_', r'<em>\1</em>', line)
    return line


def parse(markdown):
    lines = markdown.split('\n')
    res = ""
    list_count = 0
    for line in lines:
        if line.startswith("#"):
            counter = line.count("#", 0, line.find(" "))
            replace_line = line.replace("#", "", counter).replace(" ", "", 1)
            res += f"<h{counter}>{replace_line}</h{counter}>"
        if re.search(r'^[A-Z_]', line):
            parr = line
            parr = italic_bold_word(parr)
            parr = f"<p>{parr}</p>"
            res += parr
        if line.startswith("*"):
            list_count += 1
            how_many = sum(1 for line in lines if re.search(r'^\*', line))
            parr = create_list(how_many,
                               line.replace('* ', '', line.find(" ")),
                               list_count)
            parr = italic_bold_word(parr)
            res += parr

    return res
