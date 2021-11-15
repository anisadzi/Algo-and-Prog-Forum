file = open(r"C:\Users\NISA\Documents\GitHub\Algo-and-Prog-Task\TestText.txt")


ortext = file.read().split()
smplttl = ( "Mr.", "Mrs.", "Ms.", "Dr.", "Jr.", )

ntext = ""


for boundaries in ortext:
    if "?" not in boundaries and "!" not in boundaries:
        ntext += (boundaries + " ")
        if boundaries not in smplttl and "." in boundaries.split("."):
            pass
        elif "." in boundaries[-1] and boundaries not in smplttl:
            ntext += "\n"
    else:
        ntext += (boundaries + "\n")

print(ntext)