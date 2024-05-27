
class solution(object): 
    def climbingstairs(self,n):
        memo = {}  #Initialize an empty dictionary to store computed results 
        return self.ways(n,memo)   #Call the ways method with n and memo as arguments and return the results

    def ways(self, n, memo):   #Define a helper method ways which takes n and memo as input

        if n in memo:         #check if the result for n is already computed and stored in memo

            return memo[n]    #Return the stored result directly

        #Base case: if n is 1 or 2, retun 1 and 2 respectively

        if n ==1:
            return 1
        elif n == 2:
            return 2 

        #Recursive case: calculate the result for n by summing up results for n-1 and n-2

        memo[n] = self.ways(n-1,memo) + self.ways(n-2, memo)
        return memo[n]  #Store the calculated result in memo and return it
class person:
    def init(self, name, age, CID_number):
        self.name = name
        self.age = age
        self.CID_number = CID_number
    
    def behavior (self, walk, talk, eat, sleep):
        self.walk = walk
        self.talk = talk
        self.eat = eat
        self.sleep = sleep

Nm = input ("write the name of a person :")
A = input ("what is thee age of the person: ")
ID = input ("what is the persons CID_ number: ")
print ("\n")

p1 = person(Nm, A, ID)
p1.behavior("walking", "talking", "eating", "sleeping")

print(f"Name: {p1.name}, Age: {p1.age}, CID Number: {p1.CID_number}")
print(f"Behavior: Walk - {p1.walk}, Talk - {p1.talk}, Eat - {p1.eat}, Sleep - {p1.sleep}")
print ("\n")

class teacher (person):
    def init (self, subject, salary, department, designation):
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def  behavior (self,teaching, grade_student, attend_meeting):
        self.teaching = teaching 
        self.grade_student = grade_student
        self.attend_meeting = attend_meeting

t1= teacher( "biology","50000", "science", "senior")
t1.behavior("teaching biology", "grading papers", "attending department meetings")

print(f"Name: {p1.name}, Age: {p1.age}, CID Number: {p1.CID_number},\n subject: {t1.subject}, salary: {t1.salary}, department: {t1.department}, designation: {t1.designation} ")
print("\n")
print(f"Behavior: Walk - {p1.walk}, Talk - {p1.talk}, Eat - {p1.eat}, Sleep - {p1.sleep}, and \n {p1.name} job is to do : {t1.teaching}, {t1.grade_student}, and {t1.attend_meeting}")
print("\n")

class student(person):
    def init (self, student_id, course, year, GPA):
        self.student_id = student_id
        self.course = course
        self.year = year
        self.GPA = GPA 

    def behavior(self, study,Attend_class,write_exam):
        self.study = study
        self.Attend_class = Attend_class
        self.write_exam = write_exam


s1 = student("43521432", "Computer Science", "2", "3.8")
s1.behavior("studying CS subjects", "attending lectures", "writing exams")

print(f"Name: {p1.name}, Age: {p1.age}, CID Number: {p1.CID_number},\n student_id: {s1.student_id}, course: {s1.course}, year: {s1.year}, GPA: {s1.GPA}")
print("\n")
print(f"Behavior: Walk - {p1.walk}, Talk - {p1.talk}, Eat - {p1.eat}, Sleep - {p1.sleep}, and \n {p1.name}, job is to : {s1.study}, {s1.Attend_class}, {s1.write_exam}")