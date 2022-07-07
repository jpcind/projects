import random

class Student:
    def __init__(self, name, score = 0):
        self.name = name.title()
        self.score = score

    def show_score(self):
        print("\n{}'s score: {}".format(self.name, self.score))

    def grade_score(self):
        if self.score > 100:
            print("Grade: A+")
        elif self.score >= 90:
            print("Grade: A")
        elif self.score >= 80:
            print("Grade: B")
        elif self.score >= 70:
            print("Grade: C")
        elif self.score >= 60:
            print("Grade: D")
        elif self.score >= 0:
            print("Grade: FAIL")
        else:
            print("lmao you in the negative")

    def increment_score(self):
        self.score = self.score + 20

    def decrement_score(self):
        self.score = self.score - 20

    def greeting(self):
        print("\nWelcome to the Testing Center, {}!".format(self.name))

    def take_test(self):
        self.greeting()

        question_pool = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        random.shuffle(question_pool)

        flag = 1
        while True:
            for i in question_pool:
                if i == 'a':
                    print("\nQuestion {}".format(flag))
                    self.question1()
                    flag = flag + 1
                elif i == 'b':
                    print("\nQuestion {}".format(flag))
                    self.question2()
                    flag = flag + 1
                elif i == 'c':
                    print("\nQuestion {}".format(flag))
                    self.question3()
                    flag = flag + 1
                elif i == 'd':
                    print("\nQuestion {}".format(flag))
                    self.question4()
                    flag = flag + 1
                elif i == 'e':
                    print("\nQuestion {}".format(flag))
                    self.question5()
                    flag = flag + 1
                elif i == 'f':
                    print("\nQuestion {}".format(flag))
                    self.question6()
                    flag = flag + 1
                elif i == 'g':
                    print("\nQuestion {}".format(flag))
                    self.question7()
                    flag = flag + 1
                if flag == 6: #Max 5 questions
                    break
            self.show_score()
            self.grade_score()
            return

    def question1(self):
        while True:
            print("Where is Cal Poly Pomona? (20 pts.)")
            print("A. Texas")
            print("B. California")
            print("C. Nevada")
            print("D. Washington")
            answer = input("Answer: ").upper()
            if answer == "B":
                print("**CORRECT**")
                self.increment_score()
                break
            elif answer == "A" or answer == "C" or answer == "D":
                print("**INCORRECT**")
                break
            else:
                print("Unrecognized response\nTry again")

    def question2(self):
        while True:
            print("On your student records system, what does CSU stand for? (20 pts.)")
            print("A. California State University")
            print("B. Colorado State Universities")
            print("C. Color Sparkling Unicorn")
            print("D. Canadian Swan Upping")
            answer = input("Answer: ").upper()
            if answer == "A":
                print("**CORRECT**")
                self.increment_score()
                break
            elif answer == "B" or answer == "C" or answer == "D":
                print("**INCORRECT**")
                break
            else:
                print("Unrecognized response\nTry again")

    def question3(self):
        while True:
            print("According to Shrek, what has layers? (20 pts.)")
            print("A. Cake")
            print("B. Doesn't matter. Get out of his swamp")
            print("C. Onions")
            print("D. Donkeaayy")
            answer = input("Answer: ").upper()
            if answer == "B":
                print("You not even lying.\n**BONUS POINTS (+10 pts.)**")
                self.increment_score()
                self.score = self.score + 10
                break
            elif answer == "C":
                print("**CORRECT**")
                self.increment_score()
                break
            elif answer == "A":
                print("Shrek did not say that. Shame")
                print("**POINTS LOST (-20 pts.)**")
                self.decrement_score()
                break
            elif answer == "D":
                print("DONKKKAYYYYYY")
                break
            else:
                print("Unrecognized response.\nTry again")

    def question4(self):
        while True:
            print("How many Lowe's could Rob Lowe rob if Rob Lowe could rob Lowe's? (35 pts.)")
            print("A. Yes")
            print("B. No")

            try:
                answer = int(input("Answer: "))
                if answer == 0:
                    print("I mean... theoretically... at least one...")
                    break
                elif answer < 0:
                    print("Very funny. That's a negative number bruh.")
                    print("**POINTS LOST (-20 pts.)**")
                    self.decrement_score()
                    break
            except (ValueError, TypeError):
                print("Trick question.")
                print("You could have put any positive whole number and gotten it right.")
                break
            else:
                print("Clever. It is within the realm of possibilities that Row Lowe could rob {} Lowe's".format(answer))
                self.increment_score()
                self.score = self.score + 15
                break

    def question5(self):
        while True:
            print("Who is amazing? (50 pts.)")
            print("A. Me")
            print("B. {}".format(self.name))
            print("C. I am amazing")
            print("D. The person taking this test")
            print("E. (skip)")
            answer = input("Answer: ").upper()
            if answer == "A" or answer == "B" or answer == "C" or answer == "D":
                print("**Ya dang right you are**")
                self.increment_score()
                self.increment_score()
                self.score = self.score + 10
                break
            elif answer == "E":
                print("**STOP TRYING TO SKIP THIS QUESTION (-40 pts.)**")
                self.decrement_score()
                self.decrement_score()
            else:
                print("**You. YOU are amazing. Now try again.**")

    def question6(self):
        counter = 0
        while True:
            print("Yes (20 pts.)")
            answer = input("Answer: ").upper()
            if answer == "NO":
                if counter == 1:
                    print("**Seriously..? I'm deducting points smh (-15 pts.)")
                    self.score = self.score - 15
                    break
                counter = counter + 1
                print("Could've typed anything else and would've been awarded points...")
                print("I'll give you one more shot...")
            elif answer == "YES":
                print("yes. yes indeed")
                print("**BONUS POINT (+1 pt.)**")
                self.increment_score()
                self.score = self.score + 1
                break
            else:
                print("lmao **FREE POINTS**")
                self.increment_score()
                break

    def question7(self):
        while True:
            print("How much wood could a woodchuck chuck if a wood chuck could chuck wood? (317.515 pts.)")
            print("A. A woodchuck can't chuck wood! ")
            print("B. About 317.515 lbs")
            print("C. Approximately 317.515 kgs")
            print("D. Iono. But it chuck somethin'")
            answer = input("Answer: ").upper()
            if answer == "A":
                print("Obviously they can. It's in the name. I'm deducting points smh")
                self.decrement_score()
                break
            elif answer == "D":
                print("Well, you're not wrong I guess. I'll give you a point")
                print("**You get a single point**")
                self.score = self.score + 1
                break
            elif answer == "B":
                print("So close... but wrong ¯\_(ツ)_/¯ ")
                break
            elif answer == "C":
                print("Oh please. You didn't know that.")
                print('I\'ll give you 20 points for "guessing"')
                self.increment_score()
                break
            else:
                print("Yeah I woulda put down something random too")
                print("So brave.\n**+5 points for bravery**")
                self.score = self.score+ 5
                break

def main():
    try:
        num_of_students = int(input("How many students will take the exam? "))
    except:
        print("Invalid input.")
        main()
    else:
        if num_of_students > 0:
            for i in range(num_of_students):
                student = input("\nName of examinee: ")
                examinee = Student(student)
                examinee.take_test()
        else:
            print("Invalid input")
            main()
main()
'''
How many students will take the exam? 3

Name of examinee: Shrek

Welcome to the Testing Center, Shrek!

Question 1
How many Lowe's could Rob Lowe rob if Rob Lowe could rob Lowe's? (35 pts.)
A. Yes
B. No
Answer: b
Trick question.
You could have put any positive whole number and gotten it right.

Question 2
Where is Cal Poly Pomona? (20 pts.)
A. Texas
B. California
C. Nevada
D. Washington
Answer: b
**CORRECT**

Question 3
Yes (20 pts.)
Answer: no
Could've typed anything else and would've been awarded points...
I'll give you one more shot...
Yes (20 pts.)
Answer: no
**Seriously..? I'm deducting points smh (-15 pts.)

Question 4
Who is amazing? (50 pts.)
A. Me
B. Shrek
C. I am amazing
D. The person taking this test
E. (skip)
Answer: b
**Ya dang right you are**

Question 5
On your student records system, what does CSU stand for? (20 pts.)
A. California State University
B. Colorado State Universities
C. Color Sparkling Unicorn
D. Canadian Swan Upping
Answer: a
**CORRECT**

Shrek's score: 75
Grade: C

Name of examinee: ginger bread man

Welcome to the Testing Center, Ginger Bread Man!

Question 1
How much wood could a woodchuck chuck if a wood chuck could chuck wood? (317.515 pts.)
A. A woodchuck can't chuck wood!
B. About 317.515 lbs
C. Approximately 317.515 kgs
D. Iono. But it chuck somethin'
Answer: d
Well, you're not wrong I guess. I'll give you a point
**You get a single point**

Question 2
Where is Cal Poly Pomona? (20 pts.)
A. Texas
B. California
C. Nevada
D. Washington
Answer: c
**INCORRECT**

Question 3
Who is amazing? (50 pts.)
A. Me
B. Ginger Bread Man
C. I am amazing
D. The person taking this test
E. (skip)
Answer: e
**STOP TRYING TO SKIP THIS QUESTION (-40 pts.)**
Who is amazing? (50 pts.)
A. Me
B. Ginger Bread Man
C. I am amazing
D. The person taking this test
E. (skip)
Answer: huh?
**You. YOU are amazing. Now try again.**
Who is amazing? (50 pts.)
A. Me
B. Ginger Bread Man
C. I am amazing
D. The person taking this test
E. (skip)
Answer: a
**Ya dang right you are**

Question 4
On your student records system, what does CSU stand for? (20 pts.)
A. California State University
B. Colorado State Universities
C. Color Sparkling Unicorn
D. Canadian Swan Upping
Answer: a
**CORRECT**

Question 5
According to Shrek, what has layers? (20 pts.)
A. Cake
B. Doesn't matter. Get out of his swamp
C. Onions
D. Donkeaayy
Answer: c
**CORRECT**

Ginger Bread Man's score: 51
Grade: FAIL

Name of examinee: donkey

Welcome to the Testing Center, Donkey!

Question 1
Who is amazing? (50 pts.)
A. Me
B. Donkey
C. I am amazing
D. The person taking this test
E. (skip)
Answer: b
**Ya dang right you are**

Question 2
On your student records system, what does CSU stand for? (20 pts.)
A. California State University
B. Colorado State Universities
C. Color Sparkling Unicorn
D. Canadian Swan Upping
Answer: a
**CORRECT**

Question 3
How much wood could a woodchuck chuck if a wood chuck could chuck wood? (317.515 pts.)
A. A woodchuck can't chuck wood!
B. About 317.515 lbs
C. Approximately 317.515 kgs
D. Iono. But it chuck somethin'
Answer: c
Oh please. You didn't know that.
I'll give you 20 points for "guessing"

Question 4
According to Shrek, what has layers? (20 pts.)
A. Cake
B. Doesn't matter. Get out of his swamp
C. Onions
D. Donkeaayy
Answer: b
You not even lying.
**BONUS POINTS (+10 pts.)**

Question 5
How many Lowe's could Rob Lowe rob if Rob Lowe could rob Lowe's? (35 pts.)
A. Yes
B. No
Answer: 3
Clever. It is within the realm of possibilities that Row Lowe could rob 3 Lowe's

Donkey's score: 155
Grade: A+
'''
