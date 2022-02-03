def format_words(words):
    if words in [[""], [], None]: return ""
    words = list(filter(lambda x: x != "", words))
    return words[0] if len(words) == 1 else " ".join([word + "," for word in words[:-2]] + ["{} and {}".format(words[-2], words[-1])])
