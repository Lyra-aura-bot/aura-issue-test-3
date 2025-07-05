def trim_spaces(s):
    # Bug: Only trims leading spaces, not trailing
    i = 0
    while i < len(s) and s[i] == ' ':
        i += 1
    return s[i:]