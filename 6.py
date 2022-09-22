#to find the frquency of words in a word
def most_frequency(string):
    dict = {}
    for i in string:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
x=input("Please enter the string:")
print(most_frequency(x))
