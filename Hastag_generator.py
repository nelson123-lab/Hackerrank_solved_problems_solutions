def generate_hashtag(s):
    if len(s) == 0:
        return False
    else:
        p = []
        lst = s.split(" ")
        for i in lst:
            if len(i) == 0:
                pass
            else:
                i = i.lower()
                p.append(i.capitalize())
        final_word = "".join(p)
    if len(final_word) >=140:
        return False
    return '#'+final_word

print(generate_hashtag('codewars  is  nice'))