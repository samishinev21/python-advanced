def concatenate(*words, **corrections):
    result = ""

    for word in words:
        result += word

    for word, correction in corrections.items():
        result = result.replace(word, correction)
    return result

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java ="Java"))