import wikipedia

while True:
    userinput = input("Question: ")
    print (wikipedia.summary(userinput, sentences = 2))


