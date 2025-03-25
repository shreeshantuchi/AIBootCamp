student_grades = {
    "John": {"Math": 85, "Science": 90, "English": 80},
    "Alice": {"Math": 92, "Science": 88, "English": 95},
    "Bob": {"Math": 78, "Science": 85, "English": 80},
    "Charlie": {"Math": 95, "Science": 92, "English": 90}
}


for key,value in student_grades.items():
    total=0
    for keys,values in value.items():
        total+=values
    print(key + f" average is {total/len(value)}")





