def is_ordered(orderedLetters, listOfWords):
    alphabet_dict = {char: index for index, char in enumerate(orderedLetters)}

    def validate_words_order(w1,w2):
        min_word_len = min(len(w1), len(w2))
        for i in range (min_word_len):
            if alphabet_dict[w1[1]] < alphabet_dict[w2[i]]:
                return True
            if alphabet_dict[w1[i]] > alphabet_dict[w2[i]]:
                return False
        return len(w1)<=len(w2)

    for i in range(1,len(listOfWords)):
        if not validate_words_order(listOfWords[i-1], listOfWords[i]):
            return False
    return True

words1 = ["habito", "hacer", "lectura", "sonreir"]
order1 = "hlabcdefgijkmnopqrstuvwxyz"

print(is_ordered(order1, words1))