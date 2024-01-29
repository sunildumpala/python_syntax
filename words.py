def print_upper_words(words_list, must_start_with):
    """
      For an array of words, print them in uppercase, only if they begin with a letter in must_start_with list.
    """
    for word in words_list:
        if word[0] in must_start_with:
            print(word.upper())

print_upper_words(["hello","hey", "goodbye", "yo", "yes"], {"h", "y"})
