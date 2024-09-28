
def add_or_update_student_info(file_name, student_name, grade, fav_subject):
    
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        
        lines = []

    
    student_found = False
    updated_data = []
    
    for line in lines:
        if student_name in line:
            
            updated_data.append(f"{student_name} | Grade: {grade} | Favorite Subject: {fav_subject}\n")
            student_found = True
        else:
            updated_data.append(line)

    
    if not student_found:
        updated_data.append(f"{student_name} | Grade: {grade} | Favorite Subject: {fav_subject}\n")
    
    
    with open(file_name, 'w') as file:
        file.writelines(updated_data)
    
    print(f"Student info updated: {student_name} | Grade: {grade} | Favorite Subject: {fav_subject}")


def display_student_info(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            if data:
                print("Current Student Records:")
                print(data)
            else:
                print("No student records found.")
    except FileNotFoundError:
        print(f"No file named {file_name} found. Please add a student first.")


def main():
    file_name = "student_info.txt"
    
    while True:
        print("\n1. Add/Update Student Information")
        print("2. Display All Students' Information")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            student_name = input("Enter the student's name: ")
            grade = input("Enter the student's grade: ")
            fav_subject = input("Enter the student's favorite subject: ")
            add_or_update_student_info(file_name, student_name, grade, fav_subject)
        
        elif choice == '2':
            display_student_info(file_name)
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
