''' Practical1
first = "Dave"
last = "Gray"

print(type(first))
print(type(first)==str)
print(isinstance(first, str))

pizza = str("Pepperoni")
print(type(first))
print(type(first)== str)
print(isinstance(first, str))

fullname = first+" "+last
print(fullname)

decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " +decade+ "s."
print(statement)

#1
scores = []
for i in range(5):
    score = float(input(f"Enter test score {i+1}:"))
    scores.append(score)

average = sum(scores) /5
print(f"The average score is: {average:.2f}")

#2
rm = float(input("Enter rm: "))
sgd = float(rm/3.27)
print(f"sgd amount {sgd:.2f}")

#3
speed_of_light = 3e8
seconds_in_light_year = speed_of_light *365 *24 *60*60
exp=0

while seconds_in_light_year >=10:
    seconds_in_light_year /=10
    exp+=1

print(f"The value of a light-year is {seconds_in_light_year:.2f} x 10^{exp} meters.")

#6
r = float(input("Enter radius for sphere: "))
print(f"""Sphere properties:
      1 Diameter: {r*2:.2f}
      Circumference: {2*3.142*r:.2f}
      Surface Area: {4*3.142*(r**2):.2f}
      Volume: {4/3*3.142*r**3:.2f}""")

#7
bill = float(input("Total Bill: "))
num = int(input("How many people are eating with us: "))
taxed_bill = bill*1.16
each = round(taxed_bill / num, 2)
print(f"Each friend pays {each} ringgit.")

#8
hrwage = float(input("Hourly wage: "))
totalhrs = float(input("Working duration per day: "))
overtime = float(input("Overtime duration: "))

weeklypay= float(hrwage * (totalhrs + 1.5*(overtime)))
print(f"Weekly pay is RM{weeklypay:.2f}")

#use rjust, center thing
#1
#menu = Welcome to Underground Video rental store
new_rental = 3.00
old_rental = 2.00

new_vid = int(input("Enter new>>> "))
old_vid = int(input("Enter old>>> "))
days =int(input("Days renting: "))
sum = float((new_rental * (new_vid)+ old_rental *(old_vid))*days)
print(f"Total ammount to pay is RM{sum:.2f} for {days} days")

#2
seconds = int(input("Enter total seconds: "))

hrs = seconds // 3600
seconds %= 3600
minutes= seconds//60
seconds %=60

print(f"Elapsed time: {hrs}:{minutes:02}:{seconds:02}")

#3 simple way
income = float(input(">>>"))

if income <= 2500:
    tax_rate = 0
elif income <=10000:
    tax_rate = 0.05
elif income <=50000:
    tax_rate = 0.15
else:
    tax_rate = 0.25
    
tax = income* tax_rate
print(f"Tax rate: {tax_rate *100:.0f}%")
print(f"Total tax to pay: RM {tax:.2f}")

#3 tuple
def calculate_tax(income):
    brackets = [
        (2500, 0.00),
        (10000, 0.05),
        (50000, 0.15),
        (float('inf'), 0.25)
    ]
    for limit, rate in brackets:
        if income<=limit:
            return rate, income*rate
        
income = float(input("Enter yearly income: RM"))
rate, tax = calculate_tax(income)
print(f"Tax rate: {rate*100:.0f}% | Tax to pay: RM {tax:.2f}")

#4
gb = int(input(">>> "))
if gb <= 10:
    cost = gb*15
else:
    cost = ((10)*15 +(gb-10)*30)
print(f"Amount to pay for usage of {gb}GB is RM{cost:.2f}.")

#4 tuple
def calculate_cost(gb):
    brackets = [
        (5, 10),
        (10, 15),
        (20, 20),
        (float('inf'), 30)
    ]

    prev_limit = 0
    total_cost = 0

    for limit, rate in brackets:
        if gb>limit:
            total_cost += (limit-prev_limit) *rate
            prev_limit = limit
        else: 
            total_cost +=(gb - prev_limit) *rate
            break
    return total_cost

gb = int(input("Enter total GB used>>>"))
cost = calculate_cost(gb)
print(f"Amount to pay for usage of {gb}GB is RM{cost:.2f}. ")


#5
choice = input("Choose circle (C/c) or Rectangle (R/r)>>> ").lower()
if choice =="c":
    radius = int(input("Radius>>>"))
    circle = float(3.14159 * radius)
    print(f"Circle area is {circle:.2f}")
elif choice == "r":
    length = int(input("length>>> "))
    width = int(input("width>>> "))
    rectangle = length*width
    print(f"Rectangle area is {rectangle}")
else:
    print("Error")

#6
day = int(input("Enter day of the week (1=Monday, 2=Tuesday...)"))

match day:
    case 1 :
        drink = "Peppermint Mocha"
    case 2:
        drink = "Canday Bar Latte"
    case 3:
        drink = "Caramel Coffee"
    case 4 :
        drink = "Chocolate Almond Cafe Au Lait"
    case 5:
        drink = "Pumpkin-Chai Latte"
    case 6:
        drink = "Vanilla Chai Tea"
    case 7:
        drink ="Gingerbread Latte"
    case _:
        drink ="Invalid day number"

print(f"Drink of the day: {drink}")


#practical 4
#1
print("Starting")
i = 0
while i<10:
    print(i, end= " ")
    i+=1
print("\nDone")

#2
print("Starting")
i = -20
while i<=-2:
    print(i, end= " ")
    i+=2
print("\nDone")


#3
while True:
    print("This is a function that take input a and input b, given a to the power of b")
    a=int(input("a>>> "))
    b=int(input("b>>> "))
    power = a**b
    print(f"Calculation: {power}")
    stay = input("Continue? (1 to stay, 0 to exit)")
    if stay ==1:
        continue
    if stay==0:
        break
    else:
        break
        
a=int(input("a>>> "))
b=int(input("b>>> "))
power=1
i=1
while i<=b:
    power*=a
    i+=1
    
print(a, "to the power of ",b, "=", power)
   
#4
sum=0
while True:
    num = int(input(">>> "))
    sum +=num
    print(f"Sum is {sum}")
    stay = input("DONE? ").strip().upper()

    if stay =="DONE":
        break
    
#5
COUNT=1
while True:
    SECRET_NUM = 540
    num = int(input("Enter a number: "))

    if SECRET_NUM == num:
        print(f"Well done, you took {COUNT} attempts to guess the correct number")
        break
    if SECRET_NUM >= num:
        print("Guess is lower")
    else:
        print("Guess is higher")
    COUNT+=1
    
#Practical5
#1
import random
import sys
while True:
    COUNT=0
    SECRET_NUM = random.randint(1,200)
    guess_num = int(input("Guess>>> "))
    
    #mechanism for guessing
    while SECRET_NUM != guess_num:
        if guess_num < SECRET_NUM:
            print("Guess is lower")          
        else:
            print("Guess is higher")
        guess_num = int(input("Guess again>>> "))
        COUNT+=1

    print("\n   Hooray! You got it")
    print(f"    Guess number {guess_num} is equal to secret number {SECRET_NUM}")
    print(f"    You have taken {COUNT} attempts to guess")   

    #mechanism for quitting or staying in the game
    while True:
        try:
            STAY = int(input("Continue playing? (1 to continue ; 0 to quit)>>>  "))
            if STAY == 1:
                print("\nYou entered a new game!!! ")
                break

            if STAY ==0:
                print("Goodbye.")
                sys.exit()
            else:
                print("ERROR!!")
                STAY = int(input("Continue playing? (1 to continue ; 0 to quit)>>>  "))
        except ValueError:
            print("ERROR!!")
            STAY = int(input("Continue playing? (1 to continue ; 0 to quit)>>>  "))

#2 Multiplication Table Generator
num = int(input("\nWhich multiplication table would you like to print? "))
limit= int(input("How high would you like it to go? "))
print("Here is your multiplication table: ")

i=1
while i<=limit:
    print(f"{num} times {i} = {num*i}")
    i+=1

    
#3 Printing character by character
ROWS = 5
COLS = 11

i=0
while i<ROWS:
    j=0
    while j<COLS:
        if j%2 ==0:
            print("1", end="")
        else:
            print("0", end="")
        j+=1
    print()
    i+=1

#4 Temperature conversion program
import sys

def ctf(c):
    return(c*9/5) +32
def ftc(f):
    return(f-32)*5/9
def convert_temps(selection, min_temp, max_temp):
    while min_temp <= max_temp:
        if selection ==1:
            print(f"{min_temp}C = {ctf(min_temp):.1f} F")
        else:
            print(f"{min_temp}F = {ftc(min_temp):.1f} C")
        min_temp+=1
    print("Conversion Done!")

def main():
    while True:
        print("""Temperature Conversion Programme
[1] Convert Celsius to Farenheit.
[2] Convert Farenheit to Celsius.""")
        try:
            selection = int(input("Enter your selection, 1 or 2: "))
        except ValueError:
            print("ERROR: Invalid Selection!")
            continue

        if selection not in [1,2]:
            print("ERROR: Invalid Selection!")
            continue

        print("Enter temperature in integer values only.")
        try:
            min_temp = int(input("Enter minimum temperature: "))
            max_temp = int(input("Enter maximum temperature: "))
        except ValueError:
            print("ERROR: Invalid Input!")
            continue
        if min_temp > max_temp:
            print("ERROR: Invalid Input!")
            continue

        convert_temps(selection, min_temp, max_temp)

        again = input("Do you want to run the program again? [Y/N]: ").upper()
        if again != "Y":
            print("Goodbye!")
            sys.exit()

main()
 
 
#Practical 6
#1 loop to amend into list
mylist= []
COUNT=0

while COUNT <5:
    num = float(input("Enter a number: "))
    mylist.append(num)
    COUNT+=1

print("my_list =", mylist)

#2 store list in incremental order, calc total and average values
MY_LIST =[]
COUNT=0

while COUNT <5:
    num = float(input("Enter a number: "))
    MY_LIST.append(num)
    MY_LIST.sort()
    COUNT+=1

total =0
i=0
while i<len(MY_LIST):
    total +=MY_LIST[i]
    i+=1

avg = total / len(MY_LIST)
print(f"""my_list = {MY_LIST} \nTotal = {total} \nAverage = {avg}""")

#3 forward_list in incremental order and decremental order
FORWARD_LIST =[]
COUNT=0

while COUNT <5:
    num = float(input("Enter a number: "))
    FORWARD_LIST.append(num)
    FORWARD_LIST.sort()
    COUNT+=1

REVERSE_LIST = []
#REVERSE_LIST = FORWARD_LIST.copy().sort().reverse()
#REVERSE_LIST.sort(reverse=True)
index = len(FORWARD_LIST) -1
while index >=0:
    REVERSE_LIST.append(FORWARD_LIST[index])
    index -=1

print(f"""forward_list = {FORWARD_LIST} \nreverse_list = {REVERSE_LIST}""")

#4
MY_LIST = []
COUNT=0
while COUNT <5:
    num = float(input("Enter a number: "))
    MY_LIST.append(num)
    COUNT+=1
print(f"my_list = {MY_LIST}")

INDEX =len(MY_LIST)-1
while INDEX >=0:
    del MY_LIST[INDEX]
    print(f"my_list = {MY_LIST}")
    INDEX-=1

#5 
MY_LIST = []
COUNT=0
print(f"my_list = {MY_LIST}")
while COUNT <5:
    data = input("Enter a data: ")
    MY_LIST.append(data)
    COUNT+=1
print(f"my_list = {MY_LIST}")

INDEX =len(MY_LIST)-1
while INDEX >=0:
    del MY_LIST[INDEX]
    print(f"my_list = {MY_LIST}")
    INDEX-=1

#6
MY_LIST = []
COUNT=0
print(f"my_list = {MY_LIST}")
while COUNT <5:
    data = input("Enter a data: ")
    MY_LIST.append(data)
    COUNT+=1
print(f"my_list = {MY_LIST}")

INDEX =len(MY_LIST)-1
while INDEX >=0:
    if INDEX%2 ==0:
        del MY_LIST[INDEX]
        print(f"my_list = {MY_LIST}")
    INDEX-=1


#Object Oriented Programming in Python Tech w Tim
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age =age
        self.grade = grade

    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False 
    
    def get_average_grade(self):
        pass

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students)

#Practical9
#1 File Menu System

def main():
    while True:
        print("""\n[1] Create a new file.
[2] Display the file.
[3] Add a new item to the file.""")
        
        try:
            choice=int(input("Enter 1, 2, or 3: "))
        except ValueError:
            print("ERROR: Please enter a valid number (1, 2, or 3).")
            continue

        if choice ==1:
            subject = input("Enter subject name: ")
            with open("Subject.txt", "w") as f:
                f.write(subject + "\n")
            print("File created successfully")

        elif choice ==2:
            try:
                with open("Subject.txt", "r") as f:
                    print("\nFile contents:")
                    print(f.read())
            except FileNotFoundError:
                print("ERROR: 'Subject.txt' not found.")

        elif choice ==3:
            subject = input("Enter new subject to add: ")
            with open ("Subject.txt", "a") as f:
                f.write(subject + "\n")
            print("\nUpdated file contents:")
            with open("Subject.txt", "r") as f:
                print(f.read())

        else:
            print("ERROR: Invalid selection! Please enter 1, 2, or 3.")

        again = input("Run again? (y/n): ").lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()
    
#2 Multiplication Table to File
def main():
    try:
        num = int(input("Display multiplication table of? "))
    except ValueError:
        print("ERROR: Please enter a valid integer.")
        return
    
    filename = f"TT{num}TXT.txt"
    with open(filename, "w") as f:
        f.write(f"A multiplication table of {num} times 1 to 12.\n")
        for i in range (1, 13):
            line = f"{num} x {i} = {num*i}\n"
            f.write(line) #What does f.write line means

    with open(filename, "r") as f:
        print(f.read())
if __name__ == "__main__":
    main()
    
#3 Student Grade Manager
def add_grade():
    name = input("Enter student name: ")
    try:
        grade = float(input("Enter grade (0-100): "))
        if not (0 <=grade <=100):
            print("ERROR: Grade must be between 0 and 100.")
            return
    except ValueError:
        print("ERROR: Invalid grade input.")
        return
    
    with open("grades.txt", "a") as f:
        f.write(f"{name}, {grade}\n")
    print("Grade added successfully!")
def view_grades():
    try:
        with open("grades.txt", "r") as f:
            print("\nStudent Grades:")
            for line in f:
                name, grade = line.strip().split(",")
                print(f"{name}: {grade}")
    except FileNotFoundError:
        print("ERROR: 'grades.txt' not found.")
def class_average():
    try:
        with open("grades.txt", "r") as f:
            grades = [float(line.strip().split(",")[1]) for line in f] #complex
        if grades:
            avg = sum(grades) / len(grades)
            print(f"Class average: {avg:.2f}")
        else:
            print("No grades recorded yet.")
    except FileNotFoundError:
        print("ERROR: 'grades.txt' not found.")

def main():
    while True:
        print("""\nStudent Grade Manager
[1] Add new student grades
[2] View all grades
[3] Calculate class average
[4] Exit""")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_grade()
        elif choice =="2":
            view_grades()
        elif choice =="3":
            class_average()
        elif choice=="4":
            print("Existing program. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose between 1 and 4.")

if __name__ =="__main__":
    main()

#Practical7
#1
j = int(input("Enter>>> "))
for i in range(1, 13):
    print(f"{i} x {j} = {i*j}")
    #i+=1  

#2 count down from 50
cdnum = int(input("Count down from 50, input sth less than 50 \n>>> "))
for i in range(50, cdnum-1, -1):
    print(i)

    
#3counting up or down
def countup():
    """Counting up from 1 to what user input"""
    cunum = int(input("Counting up from 1\n>>> "))
    for i in range(1, cunum+1, +1):
        print(i)
def countdown():
    """Counting down until what user input from 20"""
    cdnum = int(input("Counting down from 20 \nPlease enter sth below 20 \n>>> "))
    for i in range(20, cdnum-1, -1):
        print(i)
def main():
    """body program"""
    while True:
        try:
            choice = int(input("Welcome to the counting up or down machine \nHere you have \n1 Counting up from 1 to whichever number you want \n2 Counting down from 20 to whichever number you input \n>>> "))
            if choice == 1:
                countup()
                #break
            elif choice ==2:
                countdown()
                #break
            else:
                print("I don't understand! Please enter 1 or 2.")
        except ValueError:
            print("Invalid input! Please enter a number (1 or 2).")
        print("\n\n")
if __name__ ==  "__main__" :
    main()

#4 math quiz
import random
def main():
    """A game to make user do calculation on two random numbers operated"""
    correct =0
    for i in range (5):
        print("Welcome to the random addition arithmetic game")
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        usercalc = int(input(f"{num1} + {num2} = "))
        if usercalc == num1+num2 :
            print("Congrats, correct")
            correct +=1
        else:
            print(f"The correct answer is {num1+num2}")
    print(f"\n\nCongrats you have had {correct} successful attempts! \nThat's impressive. ")

if __name__ == "__main__" :
    main()

#6 Find minimum and maximum out of 10 inputs
def mnf(my_list):
    #find out maximum number out of lists using for loop 
    maximum = my_list[0]
    for i in my_list:
        if i >maximum:
            maximum = i
    return maximum
def min(my_list):
    #find out minimum number out of lists using for loop
    minimum = my_list[0]
    for i in my_list:
        if i<minimum:
            minimum = i
    return minimum

def main():
    #A program to find the maximum and minimum numbers in a list
    print("\n\nA program to find the maximum and minimum numbers in a list.")
    print("Enter ten (10) numbers into a list.")
    my_list = []
    for i in range (10):
        num = int(input("Enter a number: "))
        my_list.append(num)
    print(f"my_list = {my_list}")
    print(f"Maximum number = {mnf(my_list)}")
    print(f"Minimum number = {min(my_list)}")
    
if __name__ =="__main__":
    main()

#Practical 8
#1
def askinput():
    num = int(input("Enter a number: "))
    return num

def counting(num):
    for i in range(1, num+1):
        print(i)

storednum = askinput()
counting(storednum)

#2 
import random
def gethnl():
    high = int(input("Enter high number: "))
    low = int(input("Enter low number: "))
    return high, low
def main():
    high, low = gethnl()
    comp_num = random.randint(low, high)
    print("Computer chose:", comp_num)

main()

#2 advanced using class
import random
class GuessGame:
    def __init__(self):
        self.low = int(input("Enter low number: "))
        self.high = int(input("Enter high number: "))
        self.comp_num = random.randint(self.low, self.high)
        print(f"Computer chose a number between {self.low} and {self.high}, which is {self.comp_num}.")
    def thinking(self):
        return int(input("I am thinking of a number..."))
    def checking(self):
        while True:
            try:
                guess = self.thinking()
                if self.comp_num == guess:
                    print("Correct, you win!")
                    break
                if self.comp_num < guess:
                    print("Guess is higher")
                elif self.comp_num > guess:
                    print("Guess is lower")    
            except ValueError:
                print("Invalid input. Please enter a number.")
game = GuessGame()
game.checking()

#3 menu
import random
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {correct_answer}.")

def addition():
    a = random.randint(5, 20)
    b = random.randint(5, 20)
    print(f"What is {a} + {b}?")
    answer = int(input("Your answer: "))
    check_answer(answer, a + b)

def subtraction():
    a = random.randint(25, 50)
    b = random.randint(1, 25)
    print(f"What is {a} - {b}?")
    answer = int(input("Your answer: "))
    check_answer(answer, a - b)

def main():
    while True:
        choice = int(input("""Menu: \n[1] Addition \n[2] Subtraction \nEnter 1 or 2: """))
        match choice:
            case 1:
                addition()
            case 2:
                subtraction()
            case _:
                print("Invalid choice!")

if __name__ == "__main__":
    main()

#teacher spotcheck
import sys
def ctf(c):
    return(c*9/5) +32
def ftc(f):
    return(f-32)*5/9
def convert_temps(selection, temp):
    if selection ==1:
        print(f"{temp}C = {ctf(temp):.1f} F")
    elif selection==2:
        print(f"{temp}F = {ftc(temp):.1f} C")
    else:
        print("ERROR: Invalid Selection!")

def main():
    while True:
        print("""Temperature Conversion Programme
[1] Convert Celsius to Farenheit.
[2] Convert Farenheit to Celsius.""")
        selection = int(input("Enter your selection, 1 or 2: "))
        temp = int(input("Enter temperature: "))
        convert_temps(selection, temp)
        again = input("Do you want to run the program again? [Y/N]: ").upper()
        if again != "Y":
            print("Goodbye!")
            sys.exit()
main()

#4
user_list = []
def read_number(total_nuum_to_read):
    for _ in range (total_nuum_to_read):
        num = int(input("Enter a number: "))
        user_list.append(num)
    return user_list
def find_max_number(a_list_of_numbers):
    maximum = a_list_of_numbers[0]
    for i in a_list_of_numbers:
        if i > maximum:
            maximum = i
    return maximum
def find_min_number(a_list_of_numbers):
    minimum = a_list_of_numbers[0]
    for i in a_list_of_numbers:
        if i < minimum:
            minimum = i
    return minimum

def main():
    print("A program to find the maximum and minimum numbers in a list.")
    times = int(input("How many numbers you want to read into a list: "))
    numbers = read_number(times)
    print(f"my_list = {numbers}")
    print(f"Maximum Number = {max(user_list)} \nMinimum Number = {min(user_list)}")

main()

#W8 Bomb countdown timer
def countdowntimer():
    total_seconds = int(input("Enter countdown time in seconds: "))
    for total_seconds in range(total_seconds, -1, -1):
        print(total_seconds)

    print("The bomb has gone off!")
countdowntimer()

#W8 recursive method
def countdown(n):
    if n==0: #base case to prevent infinite recursion until program crashes, Stack Overflow
        print("Blast off!")
        return
    print(n)
    countdown(n-1) #recursive call

getuser = int(input("Enter a number to countdown from: "))
print("Countdown:")
countdown(getuser)

#W8 Display numbers
i=1
j=1
while i<=2:  
    while j <= (4*i):
        print(j, end=" ")
        j+=1
    print()
    i+=1

#W9
print(list(range(1, 10, 2)))

#import statistics
import numpy as np
numbers =[]
for i in range (5):
    number = int(input(">>> "))
    numbers.append(number)
numbers_array = np.array(numbers)
print(*numbers_array)
print(numbers_array.sum())
#print(sum(numbers)/len(numbers))
#print(statistics.mean(numbers))
print(numbers_array.mean())

for total_indexes in range(1, 6):
    for number in range (1, 6):
        print(total_indexes*number, end = "\t")
    print()    

#print first 100 prime numbers
count = 0
num = 2

while count < 100:
    prime = True
    for i in range (2, num):
        if num % i ==0:
            prime = False
            break
    if prime: #2 is directly here as cannot enter the for loop before
        print(num)
        count+=1
    num+=1  
'''
import os
#check immutability of integers
def change_value(param1):
    # 2. Inside the function (Start)
    print(f"  [Inside Start] Value: {param1} | ID: {id(param1)} <--- SAME as Global!")
    # THE MOMENT OF CHANGE
    param1 = 45   
    # 3. Inside the function (End)
    print(f"  [Inside End] Value: {param1} | ID: {id(param1)} <--- LOOK! New ID (New Object)")
# --- Main Program ---
a = 9
# 1. Before calling
print(f"[Global Start] Value: {a} | ID: {id(a)}")
change_value(a)
# 4. After calling
print(f"[Global End  ] Value: {a} | ID: {id(a)} <--- Back to original ID")

os.system("clear")