#Create a student class that holds the details of student like name,usn,marks in 5 subjects percentage and grade
class Std:
    def __init__(self): 
        self.__USN = None
        self.__Name = None
        self.__Marks = []
        self.__Percentage = None
        self.__Grade = None

    def Std_Input(self):
        self.__Name = input("Enter your Name: ")
        self.__USN = input("Enter Your USN: ")
        for i in range (0,5):
            marks = input(f"Enter Your Marks in Sub{i+1} : ")
            self.__Marks.append(marks)

    def calc_percentage (self):
        sum = 0
        for i in self.__Marks:
            sum = sum + int(i)
        self.__Percentage = (sum/500)*100

    def calc_Grade(self):
        per = float(self.__Percentage)
        if per<=100 and per >=80:
            self.__Grade = "A"
        elif per<80 and per >=60:
            self.__Grade = "B"
        elif per<60 and per >=40:
            self.__Grade = "C"
        elif per<40 and per >=0:
            self.__Grade = "D"
        else: 
            self.__Grade = "Inavlid"

    def print_details(self):
        print("Name: ",self.__Name)
        print("USN : ",self.__USN)
        print("Marks in Five Subject are :")
        for i in range(0,5):
            print(f"Subject {i+1} = {self.__Marks[i]}")
        print("Percentage : ", self.__Percentage)
        print("Grade : ", self.__Grade)

    def convert_list(self):
        st_list = [self.__USN,self.__Name,self.__Marks,self.__Percentage,self.__Grade]
        return st_list

    def covert_ob(self,stu_list):
        self.__USN = stu_list[0]
        self.__Name = stu_list[1]
        self.__Marks = stu_list[2]
        self.__Percentage = stu_list[3]
        self.__Grade = stu_list[4]
st1 = Std()

print(type(st1))

st1.Std_Input()

st1.calc_percentage()
st1.calc_Grade()

st1.print_details()

