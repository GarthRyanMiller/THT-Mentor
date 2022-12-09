def allDaysOfWeek():
    print("Monday, Tuesday, Wednesday, Thursday, Friday, Saturday")
allDaysOfWeek()

def replaceWithHello(sentence):
    splitSent = sentence.split(' ')
    print(splitSent)
    for x, word in enumerate(splitSent):
        print(x)
        print (x % 2)
        if x % 2 != 0:
            splitSent[x] = 'Hello'
    splitSent = (" ").join(splitSent)
    print (splitSent)
    
sentence1 = input("Enter Sentence:")
replaceWithHello(sentence1)