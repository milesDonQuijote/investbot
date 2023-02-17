def is_clock(txt):
    return len(txt) == 5 and ':' in txt and txt[:2].isdigit() and txt[3:].isdigit()
