def extract_digits(s):
    if s.isdigit():
        return s

    digits = ""
    for c in s:
        if c.isdigit():
            digits += c

    return digits


data = ["Abc12Xy", "12XY33", "KDKD12", "2334"]

for d in map(extract_digits, data):
    print(d)