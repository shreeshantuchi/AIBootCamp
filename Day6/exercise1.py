def count_number_lines_word(fileName):
    try:
        with open(fileName,"r") as file:
            lines=file.readlines()
            lineCount=len(lines)
            wordCoint=sum(len(line.split()) for line in lines)

            print(f"Line Count: {lineCount}")
            print(f"Word Count: {wordCoint}")
    except FileNotFoundError:
        print(f"file {fileName} doesnt Exist")



count_number_lines_word("sample.text")
