def single_root_words(root_word, *other_words):
    same_word = []
    other_words = list(other_words)
    for i in range(len(other_words)):
        word = other_words[i]
        if root_word.lower() in word.lower():
            same_word.append(word)
        elif word.lower() in root_word.lower():
            same_word.append(word)
    print(same_word)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
