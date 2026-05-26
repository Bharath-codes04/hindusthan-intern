students = []
def add():
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    m1 = int(input("Mark 1 : "))
    m2 = int(input("Mark 2 : "))
    m3 = int(input("Mark 3 : "))
    marks = (m1, m2, m3)
    d = {
        "name": name,
        "age": age,
        "marks": marks
    }
    students.append(d)
    print("Student Added")

def display():
    if len(students) == 0:
        print("No Records")
    else:
        for i in students:
            print("\nName :", i["name"])
            print("Age :", i["age"])
            print("Marks :", i["marks"])
            avg = sum(i["marks"]) / 3
            print("Average :", avg)

def topper():
    if len(students) == 0:
        print("No Records")
    else:
        top = students[0]
        high = sum(top["marks"]) / 3
        for i in students:
            avg = sum(i["marks"]) / 3
            if avg > high:
                high = avg
                top = i
        print("\nTopper :", top["name"])
        print("Average :", high)

while True:
    print("\n1.Add Student")
    print("2.Display Students")
    print("3.Find Topper")
    print("4.Exit")

    ch = int(input("Enter choice : "))

    if ch == 1:
        add()

    elif ch == 2:
        display()

    elif ch == 3:
        topper()

    elif ch == 4:
        break

    else:
        print("Invalid Choice")