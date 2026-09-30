# 3. attendance management
def attendance_manage(data):
    while True:
        print("------Attendance Menu------")
        print("1. View attendance percentage")
        print("2. Back to main menu")
        selection=input("Choose any option from (1-2)")

        if selection=='1':
            register=input("Enter register number")
            if register in data:
                total=int(input("Enter total classes happened: "))
                attend=int(input("Enter total classes attened: "))

                if total>0 and attend<=total:
                    atten_per=(attend/total)*100
                    print("\nstudent name:",)
                    print("attendance:",atten_per,"%")
                else:
                    print("|Invalid classes count! attended classes cannot be more than total classes.")
            else:
                print("Registration number not found.")
        elif selection=='2' or selection=='3':
            break
        else:
            print("invalid choice!")
