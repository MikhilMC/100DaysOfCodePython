sentence = input()

list_of_words = sentence.split(" ")
result = {word: len(word) for word in list_of_words}


print(result)
