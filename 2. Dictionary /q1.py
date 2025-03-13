# Define a function to count the frequency of words in a given list of words.

#My Logic
# def count_word_frequency(words):
#     for key in words:
#         repeat = 0
#         for i in words:
#             if key == i:
#                 repeat += 1
#         if repeat > 1:
#             print (key)
#             print(repeat-1)
            
# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
# count_word_frequency(words) 

#Actual Solution
def count_word_frequency(words):
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
print(count_word_frequency(words))