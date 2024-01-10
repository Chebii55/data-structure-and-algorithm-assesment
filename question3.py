import string

# Dictionaries: 

# Question 3: Implement a function word_frequency(sentence) that takes 
# a sentence and returns a dictionary containing the frequency of each 
# word in the sentence. 

# Ignore punctuation and consider words in a case-insensitive manner. 

# sample input = 

# sentence = "This is a test sentence. This sentence is a test."
# result = word_frequency(sentence)
# print(result)

def word_frequency(sentence) :
    sentence = sentence.lower()#to convert the whole sentence to lowercase
    
    new_sentence = ""
    for chr in sentence:
        if not chr in string.punctuation:
            new_sentence += chr
    #break the sentence into a list
    list_word = new_sentence.rsplit(" ")


    output_dict = {}
    #loop to check for frequency
    for word in list_word:
        #to prevent looping through the same word
        if word in output_dict:
            continue
        word_count = 0
        for otherword in list_word:
            if otherword == word:
                word_count += 1
        output_dict[word] = word_count

    return output_dict



sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)