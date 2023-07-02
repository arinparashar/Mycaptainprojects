import csv

def enter_student_info():
    student_info = []
    while True:
        name = input("Enter student name (or 'q' to quit): ")
        if name == 'q':
            break
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        student_info.append([name, age, grade])
    return student_info

def preprocess_data(student_info):
    preprocessed_data = []
    for student in student_info:
        name = student[0]
        age = int(student[1])
        grade = int(student[2])
        preprocessed_data.append({'Name': name, 'Age': age, 'Grade': grade})
    return preprocessed_data

def write_to_file(preprocessed_data):
    fieldnames = ['Name', 'Age', 'Grade']
    filename = 'student_info.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(preprocessed_data)
    print(f"Data written to {filename} successfully.")

# Main program
student_info = enter_student_info()
preprocessed_data = preprocess_data(student_info)
write_to_file(preprocessed_data)
