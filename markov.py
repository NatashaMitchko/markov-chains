"""Generate markov text from text files."""


from random import choice
from sys import argv


def open_and_read_file(file_paths):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    long_string = ''
    for file_path in file_paths:
        contents = open(file_path).read()
        long_string += contents
    # print contents
    return long_string


def make_chains(text_string, n):
    """Takes input text as string; returns dictionary of markov chains.

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
    """

    chains = {}

    words = text_string.split()

    # For i up to the length - input:n, grab the ith to the i+nth (exclusive)
    # values of words, casts to a tuple and uses that tuple as a key in
    # dictionary.
    i = 0
    while i < (len(words) - n):
        ngram = tuple(words[i:n+i])
        next_word = words[i + n]
        i += 1

        # If key does not exist in dictionary, add the (key, value) pair
        # to chains.
        if ngram not in chains:
            chains[ngram] = [next_word]
        else:
            chains[ngram].append(next_word)

    return chains


def make_text(chains):
    """Returns text from chains."""

    words = []

    # Get a random key from a list of keys within the dictionary
    link = choice(chains.keys())

    # for word in link:
    #     words.append(word)

    # Add key ("link") to list of words.
    words.extend(link)

    # While the key exists in the dictionary, grab random value at the key.
    # Add to word list and update link to include the random value.
    # i.e. (word1, word2, word3) + word4
    while link in chains:
        word = choice(chains[link])
        words.append(word)
        link = tuple(list(link[1:]) + [word])

    # Use the last two words in words as the new key
    # while (words[len(words)], words[len(words)-1]) in chains:
    #     new_value = chains[(words[-2], words[-1])]
    #     words.append(choice(new_value))

    return " ".join(words)


input_path = argv[1:]  # We don't want to pass in this script as a string

# # Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# # Get a Markov chain
chains = make_chains(input_text, 3)

# # Produce random text
random_text = make_text(chains)

print random_text
