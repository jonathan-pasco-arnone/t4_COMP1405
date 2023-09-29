""" Analysis methods program """

# Created by: Jonathan Pasco-Arnone and Aidan Lalonde-Novales
# Created on: September 2023

file_contents = []

def load(str):
    """ Parses the file into a list of words"""
    # Starts by removing the other file contents from this files list
    file_contents.clear()

    full_file = open("./T4-Resources/" + str, "r", encoding="utf8")

    word = ""
    for character in full_file.read():
        if character == " ":
            file_contents.append(word)
            word = ""
        else:
            word += character

def commonword(list):
    """ Returns the most common word in the file out of the words in the given list """
    word_count = []
    # Organizes the quantities of each word into a list
    for index, item in enumerate(list):
        word_count.append(0)
        for value in file_contents:
            if value == item:
                word_count[index] += 1

    # Checks which quantity is the highest
    highest_index = 0
    for index, value in enumerate(word_count):
        if word_count[highest_index] < word_count[index]:
            highest_index = index

    # If the file is empty or the words are not in the file
    if word_count[highest_index] == 0:
        return "None"
    else:
        return list[highest_index]

def commonpair(str):
    """ Finds the most common word to follow an inputted string """
    # This 2D list holds each word that appears after the string entered followed by the
    # number of occurrences that word makes after the string
    word_count = []
    index = 0
    # Organizes the quantities of each word into a list
    for index, value in enumerate(file_contents):

        # If the index is the last value in the list then there is no word after it so there is no reason to check for one
        if index == (len(file_contents) - 1):
            break

        if value == str:
            # Checks if the word was added to the word count list
            word_recorded = False
            for count_index, word_set in enumerate(word_count):
                # Checks if the word after the given string has been recorded yet
                if file_contents[index + 1] == word_set[0]:
                    # Enters the word count list into the current items folder and goes to the 1th spot to add 1 to occurances
                    word_count[count_index][1] += 1
                    word_recorded = True
                    break
            if not word_recorded:
                word_count.append([])
                word_count[-1].append(file_contents[index + 1])
                word_count[-1].append(1)
    
    # Checks which quantity is the highest
    highest_index = -1
    for index, word_set in enumerate(word_count):
        if word_count[highest_index][1] < word_set[1]:
            highest_index = index
    
    if len(word_count) == 0:
        return "None"
    else:
        return word_count[highest_index][0]
            
def countall():
    """ Returns the total number of words in the file """
    return (len(file_contents) + 1)

def countunique():
    """ Returns the total number of unique words """
    word_record = []
    for word in file_contents:
        is_word_recorded = False
        for counted_word in word_record:
            if counted_word == word:
                is_word_recorded = True
                break
        if not is_word_recorded:
            word_record.append(word)
    return len(word_record)
