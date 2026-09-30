# 1. Student Management
def student_manage(data):
    while True:
        print("\n--------Student Menu--------")
        print("1. Register Student")
        print("2. View registered students")
        print("3. Update registered student info")
        print("4. Remove registered student")
        print("5. Back to main menu")
        selection=input("Select any option from (1-5)")

        if selection=='1':
            register=input("Enter registration number:")
            if register in data:
                print("This registration number already exists!")
            else:
                name=input("Enter name")
                branch=input("Enter branch")
                semester=input("Enter semester")

                data[register]={
                    "name":name,
                    "branch":branch,
                    "semester":semester,
                    "marks":{}
                }
                print("Student added successfully!")

        elif selection=='2':
            if not data:
                print("Student record is empty")
            else:
                print("\nRegistration no. | Name | Branch | Semester")
                print("----------------------------------------------")
                for i in data:
                    print({i} | {data[i]['name']} | {data[i]['branch']} | {data[i]['semester']})

        elif selection=='3':
            register=input("Enter registration no. to update student info")
            if register in data:
                print("Enter new details:")
                name=input("Enter name")
                branch=input("Enter branch")
                semester=input("Enter semester")
                data[register]["name"]=name
                data[register]["branch"]=branch
                data[register]["semester"]=semester
                print("student info updated")
            else:
                print("Registration no. not found")

        elif selection=='4':
            register=input("Enter registration number to remove")
            if register in data:
                del data[register]
                print("student data removed successfully.")
            else:
                print("registration number not found.")

        elif selection=='5':
            break
        else:
            print("invalid choice!")