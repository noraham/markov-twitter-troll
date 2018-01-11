"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    with open(file_path) as contents:  # using content manager to open and auto-close file
        src_str = contents.read()
    return src_str

#print open_and_read_file("green-eggs.txt")

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
       
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    corpus = text_string.split()
    corpus.append(None)

    size_of_gram = raw_input('Length of n-gram: ')
    size_of_gram = int(size_of_gram)

    for i in range(len(corpus) - size_of_gram):  # iterating over list of source string words
        mlist = []
        for j in range(i, i + size_of_gram):  # iterating over words in sets of size - size_of_gram
            mlist.append(corpus[j])
        dict_key = tuple(mlist)
        
        new_value_var = corpus[i + size_of_gram]
        if dict_key in chains:
            chains[dict_key].append(new_value_var)
        else:
            chains[dict_key] = [new_value_var]
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    keys = chains.keys()  # list of tuples
    n = len(keys[0])
    character_count = 0

    while True:
        random_key = choice(keys)  # selects a tuple
        if random_key[0][0].isupper():  # random text will start with capital letter
            break

    for initial_append in range(n):
        words.append(random_key[initial_append])  # append tuple to list as strings
        character_count += len(random_key[initial_append]) + 1  # the additional 1 is for a space after the word, delete if twitter doesn't count spaces as chars
       

    next_value = choice(chains[random_key])  # picks a random sample from the value list in chains dict
    if chains[random_key] == [None]:  # handles edge case of capital word + end of sentence, early exit condition
        return " ".join(words)
    words.append(next_value)

    counter = 1
    punctuation = [".", "!", "?"]

    while True:
        
        shift_list = []
        for k in range(counter, counter + n):
            shift_list.append(words[k])
        shift_tuple = tuple(shift_list)

        if chains[shift_tuple] == [None]:  # early exit condition if we reach end of text
            break
        if (character_count > 115 and
            (shift_list[n - 1][-1] in punctuation or character_count > 130)):
            break

        another_next_value = choice(chains[shift_tuple])
        words.append(another_next_value)
        character_count += len(another_next_value) + 1

        counter += 1
    # print 'total char count', character_count
    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
