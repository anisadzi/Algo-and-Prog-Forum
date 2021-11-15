import re


def wordlength():
    file = open(r"C:\Users\NISA\Documents\GitHub\Algo-and-Prog-Task\SampleBook.txt")
    words = re.findall("\w+", file.read())
    avrg = sum(len(word) for word in words) / len(words)
    avrg = "{:.1f}".format(avrg)
    print ("The average word length is : ", avrg)

wordlength()