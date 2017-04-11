"""Generate markov text from text files."""


from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()
    # print contents
    return contents

# contents = open_and_read_file("gettysburg.txt")


def make_chains(text_string):
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
    for i in range(len(words) - 2):

        bigram = (words[i], words[i + 1])
        next_word = words[i + 2]

        # If key does not exist in dictionary, add the (key, value) pair
        # to chains.
        if bigram not in chains:
            chains[bigram] = [next_word]
        else:
            chains[bigram].append(next_word)

    return chains

# print make_chains(contents)


def make_text(chains):
    """Returns text from chains."""

    words = []

    # Getting first tuple to initialize our string
    keys = list(chains)
    link = choice(keys)

    for word in link:
        words.append(word)

    # Use the last two words in words as the new key
    while (words[-2], words[-1]) in chains:
        new_value = chains[(words[-2], words[-1])]

        words.append(choice(new_value))

    return " ".join(words)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
