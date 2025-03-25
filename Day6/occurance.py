def count_occurance(fileName,wordSearch):
    count=0
    with open(fileName,"r") as file:
        content=file.read()
        words=content.split()
        for word in words:
            if word.lower()==wordSearch:
                count+=1

        print (f"the number of word {wordSearch} : {count}")




count_occurance("file1.txt","to")