#Qustion10

def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
a=int(input("pleas enter the max lenght of words: "))
print(long_words(a, "Write a Python program to find the list of words that are longer than n from a given list of words."))
