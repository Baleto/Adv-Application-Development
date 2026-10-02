# Program Name: Assignment2_10_students.py
# Course: IT3883/Section 01
# Student Name: Benel Kawata
# Assignment Number: Assignment 2
# Due Date: 10/2/2026
# Purpose: The purpose of this code is to calculate an average for a given list of 10 students
# with their names and grades separated by a space and saved in a separate file
# I have also defined a main function to somehow contain the code 
# Resources:
# W3Schools, "Python List sort() Method."
# https://www.w3schools.com/python/ref_list_sort.asp

def main():
    #Each student's name and grade is appended to this list
    students = []
#The rogram runs from the folder containing the 10 student scores (student_scores.txt)
#Once the reading block finishes, the with statement closes the file after the reading block finishes.
    with open("student_scores.txt", "r") as score_file:
        for line in score_file:
            slots = line.split()
            #The code ignores empty lines.
            if not slots:
                continue
            #The first field is interpreted by the machine as the name; the next six fields are scores.
            student_name = slots[0]
            score_total = 0
            for score in slots[1:]:
                score_total += int(score)

            #Each student has six equally weighted scores, which are then appended to the list as student name and final average
            final_average = score_total / 6
            students.append((student_name, final_average))

    #It begins sorting by the average at index 1 or after the name, from highest to lowest.
    students.sort(key=lambda student: student[1], reverse=True)

    #A formatted string is used to display each average with two decimal places.
    for student_name, final_average in students:
        print(f"{student_name} {final_average:.2f}")

if __name__ == "__main__":
    main()
