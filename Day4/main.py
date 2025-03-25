def wordFrequencyCounter(text):
    words=text.split()
    wordCount={}
    for word in words:
        word=word.lower()
        if word in wordCount:
            wordCount[word]+=1
        else:
            wordCount[word]=1
            

    print(wordCount)


wordFrequencyCounter("hello this is me me")   



