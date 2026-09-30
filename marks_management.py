# 2. Marks Management
def mark_manage(data):
    while True:
        print("\n-----Marks Section-----")
        print("1. Enter/Update Marks")    
        print("2. View Grade Card")    
        print("3. Back to main Menu")
        selection=input("Enter choice (1-3): ")

        if selection=='1':
            register=input("Enter registration number: ")
            if register in data:
                print("Enter marks out of hundred: ")
                python=float(input("Python: "))
                calculus=float(input("Calculus: "))
                evs=float(input("EVS: "))
                english=float(input("English: "))

                data[register]["marks"]={"python":python,"calculus":calculus,"evs":evs,"english":english}
                print("marks saved successfully!")
            else:
                print("student not found! add student first")
        
        elif selection=='2':
            register = input("Enter Reg Number: ")
            if register in data:
                st = data[register]
                if not st["marks"]:
                    print("Marks not entered for this student yet.")
                    continue

                print("\n==============================")
                print("----------Mark Sheet-----------")
                print("==============================")
                print(f"Reg No: {register} | Name: {st['name']}")
                print(f"Branch: {st['branch']} | Sem: {st['semester']}")
                print("------------------------------")

                total = 0
                for sub, m in st["marks"].items():
                    # Individual subject grade calculation
                    if m >= 90: g = "A"
                    elif m >= 80: g = "B"
                    elif m >= 40: g = "C"
                    else: g = "Fail"
                    
                    print(f"{sub}: {m} (Grade: {g})")
                    total += m
                
                # Total and Percentage calculation
                per = (total / 400) * 100
                if per >= 40: final_g = "Pass"
                else: final_g = "Fail"
                
                print("------------------------------")
                print(f"Total Marks: {total}/400")
                print(f"Percentage: {per:.2f}%")
                print(f"Final Status: {final_g}")
                print("==============================")
            else:
                print("Reg Number not found.")

        elif selection == '3':
            break
        else:
            print("Invalid choice!")