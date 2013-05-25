
def read_file():
    # Read Scrabble word file
    scrabble_words = "/home/tyler/workspace/Scrabble_Cheat/sowpods.txt"
    # Assign word file to a variable
    words = open(scrabble_words, 'r')
    # Read lines from word list
    word_list = words.readlines()
    return word_list

def remove_empty():
# Strip empty space from word list
    new_list = []
    for word in read_file():
        new = word.strip()
        new_list.append(new)
    return new_list
    
def rack_input():
    # Input rack to Scrabble Cheater
    scrabble_rack = raw_input("Enter your scrabble rack (ex. RSTLNEI):")
    # Make sure rack isn't more than seven letters
    if len(scrabble_rack) > 7 or len(scrabble_rack) < 7:
        return "error dude"
    else:
        return scrabble_rack

# track if word matches rack
def test_word(word, rack):
    rack2 = list(rack)
    for letter in word:
        if letter in rack2:
            rack2.remove(letter)
        else:
            
            return False
    return True

# if there is at least 2 matches print it out
def test_rack(all_words,rack):
    test_list = []      
    for word in all_words:
        if test_word(word, rack):
            test_list.append(word.lower())
    return test_list
            
# calculate scores
def calc_scores(valid_words):
    # Scrabble value dictionary
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
              "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
              "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
              "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
              "x": 8, "z": 10}
    top_scores = {}
    score = 0
    for word in valid_words:
        word_str = str(word)
        for letter in word_str:
            score += scores[letter]
        top_scores[word_str] = score
        score = 0
    # sort dictionary highest to lowest
    return top_scores
    
# call main function
def main():
    rack = rack_input()
    all_words = remove_empty()
    valid_words = test_rack(all_words, rack)
    word_scores = calc_scores(valid_words)
    
    print word_scores

main()


    





