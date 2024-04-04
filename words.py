
def print_upper_words(words, must_start_with):
    ''' Pass in a set of words and a set of letters, 
     then print in uppercase words that start with 
     one of the passed in letters.'''
    
    for word in words:
        if word.lower().startswith(must_start_with):
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with=("h", "y"))
print('-----------------')
print_upper_words(['hello', 'world', 'Hi', 'doggie', 'Orange', 'holiday', 'open'], ('h', 'o'))