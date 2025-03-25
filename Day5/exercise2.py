def reverseText(text):
    words=text.split()
    reverseSentence=words[::-1]
    return " ".join(reverseSentence)



inputText=input("Enter your word: ")
print(reverseText(inputText))
