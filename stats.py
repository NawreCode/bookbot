def count_words(text: str) -> int:
    return len(text.split())


def count_character_occurences(text: str) -> dict:
    d = {}
    for c in text:
        c = c.lower()
        d[c] = d.get(c, 0) + 1

    return d


def convertor(d: dict) -> list:
    l = []
    for k, v in d.items():
        l.append({"char": k, "num": v})

    l.sort(reverse=True, key=lambda x: x["num"])
    return l
