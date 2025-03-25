import re

def cleanText(text):
    #remove punchtutation
    text=re.sub("[^\w\s]"," ",text)

    #remove white space
    text=" ".join(text.split())

    return text.lower()



inpit_text=input("enter your text")
print(cleanText(inpit_text))