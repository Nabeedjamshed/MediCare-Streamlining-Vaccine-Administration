import pyodbc

class Patient:

    def __init__(self, n, gm, p, ph):
        self.name = n
        self.gmail = gm
        self.password = p
        self.phoneno = ph

    def show(self):
        print("\t____________________________________________")
        print("\t\t\t!*LOGIN*!")
        print("\t____________________________________________")
        print("\tName\t\t",self.name,'\n')
        print("\tGmail\t\t",self.gmail,'\n')
        print("\tPassword\t",self.password,'\n')
        print("\tPh.No\t\t",self.phoneno,'\n')

class Doctor(Patient):

    def __init__(self, n, gm, p, ph, degreestaus):
        Patient.__init__(self, n, gm, p, ph)
        self.degreestatus = degreestaus

    def show1(self):
        Patient.show(self)
        print("\tDegree Status\t",self.degreestatus)
        print("\t____________________________________________")

conncetor = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Pl Labs\Vaccine_management.accdb'
connect = pyodbc.connect(conncetor)
cursor = connect.cursor()

def insert_patient(n, g, ps, phone):
    cursor.execute(f"INSERT INTO Patient (Name, Gmail, Password, Phone_no) VALUES ('{n}', '{g}', '{ps}', '{phone}')")
    connect.commit()

def insert_doctor(n, g, ps, phone, deg):
    cursor.execute(f"INSERT INTO Doctor (Name, Gmail, Password, Phone_no, Degree_Status) VALUES ('{n}', '{g}', '{ps}', '{phone}', '{deg}')")
    connect.commit()

keys = ["Fever","Flu","Headache"]
values = [["Panadole","Nice"],["Rigix","Lomitile"],["Disprine","Brophin"]]
start = input("Do you want to start the app (Y/N): ")

if start == 'Y':
    account = input("Are you create Doctor account or Patient account(D/P): ")

    if account == 'P':
        print("\n**********Welcome to Vaccine Management System************ ",'\n\n',"Hopes this app will help you!!",'\n')
        n = input("What is your name: ")
        g = input('Enter your gmail id: ')
        ps = input("Enter the password: ")
        phone = input("Enter your phone number:")
        insert_patient(n, g, ps, phone)
        p = Patient(n,g,ps,phone) 
        p.show()
        while True:
            new = input("Do you want to search your disease (Y/N): ")
            if new == 'Y':
                searh = input("Let's Search: ")
                my_dict = {k: v for k, v in zip(keys, values)}

                l = []
                if searh in my_dict:
                    a = my_dict[searh]
                    l.append(a)

                for i in l:
                    for j in i:
                        print(j)
                print()

                fb = []
                feedback = input("Please Enter Your Feedback: ")
                fb.append(feedback)
                print("Thank You")
            elif new == 'N':
                break

    else:
        print("\n**********Welcome to Vaccine Management System************ ",'\n')
        n = input("What is your name: ")
        g = input('Enter your gmail id: ')
        ps = input("Enter the password: ")
        phone = input("Enter your phone number:") 
        deg = input("What is your degree status: ")
        insert_doctor(n, g, ps, phone, deg)
        d = Doctor(n,g,ps,phone, deg)
        d.show1()
        asked = input("Doctor do you want to add new disease vaccine or search vaccine (A/S): ")

        if asked == 'S':
            search = input("Search disease: ")
            my_dict = {k: v for k, v in zip(keys, values)}

            l = []
            if search in my_dict:
                a = my_dict[search]
                l.append(a)

            for i in l:
                for j in i:
                    print(j)
            print()
            ask = input("Doctor do you want to add some new medines or add some new disease (M/D): ")

            if ask == 'M':
                enter = input("Please enter the name of the medicines separated by commas: ").split(',')
                l.append(enter)
            
                print("Thank You")
        else:
            new_disease = input("What is the name of the disease: ")
            keys.append(new_disease)
            medicines = input(f"What is the name of medicines for {new_disease} separated by commas: ").split(',')
            values.append(medicines)

        fb1 = []
        feedback = input("Please Enter Your Feedback: ")
        fb1.append(feedback)
        print("Thank You")
            
else:
    print("Thank You")