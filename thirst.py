ss = ["bella","label","roller"]

word =''.join(ss)
seen = ""

for c in word:
    if c not in seen:
        if word.count(c) >= 3:
            print(f"{c}: {word.count(c)}")
            seen += c