def trim_spaces(s):
    # Bug: Only trims leading spaces, not trailing
    i = 0
    while i < len(s) and s[i] == ' ':
        i += 1
    j = len(s) - 1
    while j >= 0 and s[j] == ' ':
        j -= 1
    return s[i:j+1]