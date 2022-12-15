def get_least_vowels_word(list_of_words):
    vovels = 'a', 'e', 'o', 'u', 'i'
    if len(list_of_words) < 2 or type(list_of_words) == str:
        print("Invalid Argument. List length must be >= 2, only strings allowed.")
    else:
        dictionary = dict()
        for word in list_of_words:
            i = 0
            for character in word:
                if character in vovels:
                    i = i + 1
            dictionary[word] = i
        values = []
        for word in list_of_words:
            values.append(dictionary[word])
        values.sort()
        for word in list_of_words:
            if dictionary[word] == values[0]:
                biggest = word
        print(biggest, values[0])


list_a = ('madina', 'tolibjonova')
get_least_vowels_word(list_a)