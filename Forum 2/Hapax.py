import re


def hapax(path):
    file = open(r"C:\Users\NISA\Documents\TheTunnelUndertheChannel.txt")
    words = re.findall("\w+", file.read().lower())
    quantity = {sent: 0 for sent in words}

    for word in words:
        quantity[word] += 1

    for word in quantity:
        if quantity[word] == 1:
            print (word)


hapax("TheTunnelUndertheChannel.txt")