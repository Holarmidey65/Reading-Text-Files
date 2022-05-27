# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    text = open(filename)
    content = text.read()
    text.close()
    return content


print(read_file_content('story.txt'))


print('\n')


def count_words(string):
    counts = dict()
    words = string.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


text_file = read_file_content('story.txt')
print(count_words(text_file))
