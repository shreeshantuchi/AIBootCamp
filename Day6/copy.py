def copyText(fileName1,fileName2):
    with open(fileName1,"r") as file1:
        content= file1.read()
        with open(fileName2,"w") as file2:
            file2.write(content)



copyText("file1.txt","file2.txt")
    

