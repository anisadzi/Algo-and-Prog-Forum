orfile = open(r"C:\Users\NISA\Documents\GitHub\Algo-and-Prog-Task\SampleBook.txt")
nfile = open("SampleCount.txt", "x")

frml = orfile.read().split("\n")

counter = 0

for i in frml :
    counter += 1
    nfile.write(str(counter) + " " + str(frml[counter-1]) + "\n")