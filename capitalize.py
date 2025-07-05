def capitalize_words(s):
    words = s.split(' ')
    capitalized = []
    for word in words:
        if word:
            capitalized.append(word[0].upper() + word[1:])
        else:
            capitalized.append('')
    return ' '.join(capitalized)
