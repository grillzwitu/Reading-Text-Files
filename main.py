# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here

    with open(filename) as file:
        file_content = file.read()

    return file_content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    word_dict = {}

    split_text = text.replace(',','').replace('?', '').replace('.', '').split()

    for word in split_text:

        if word in word_dict:
            count = word_dict[word]
        else:
            count = 0

        word_dict[word] = count + 1

    print(word_dict)

    return word_dict


count_words()
