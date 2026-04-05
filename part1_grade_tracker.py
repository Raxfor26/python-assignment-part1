# Task 1

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:

    # remove extra spaces and fix capitalization
    name = student["name"].strip()
    name = name.title()

    # convert roll number from string to int
    roll = int(student["roll"])

    # split the marks string by ", " to get a list of strings, then convert each to int
    marks_list = student["marks_str"].split(", ")
    marks = []
    for m in marks_list:
        marks.append(int(m))

    # check if the name has only letters (ignore spaces)
    name_no_spaces = name.replace(" ", "")
    if name_no_spaces.isalpha():
        print("Valid name")
    else:
        print("Invalid name")

    # save the cleaned student data
    cleaned_students.append({
        "name": name,
        "roll": roll,
        "marks_str": marks
    })

    print("====================")
    print("Student: " + name)
    print("Roll No: " + str(roll))
    print("Marks: " + str(marks))
    print("====================")
    print("")

# find roll 103 and print their name in caps and lowercase
print("Requirement for Roll No 103")
for student in cleaned_students:
    if student["roll"] == 103:
        print("ALL CAPS: " + student["name"].upper())
        print("lowercase: " + student["name"].lower())
        print("")
        break




# Task 2

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("--- Grade Report for " + student_name + " ---")

# go through each subject one by one using the index
for i in range(len(subjects)):
    sub = subjects[i]
    score = marks[i]

    # assign grade based on score
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"

    print(sub + ": " + str(score) + " - Grade: " + grade)

# calculate total and average
total = 0
for m in marks:
    total = total + m

average = total / len(marks)

# find highest mark and which subject it belongs to
highest = marks[0]
for m in marks:
    if m > highest:
        highest = m

highest_index = marks.index(highest)
best_subject = subjects[highest_index]

# find lowest mark and which subject it belongs to
lowest = marks[0]
for m in marks:
    if m < lowest:
        lowest = m

lowest_index = marks.index(lowest)
worst_subject = subjects[lowest_index]

print("")
print("--- Current Statistics ---")
print("Total Marks: " + str(total))
print("Average Marks: " + str(round(average, 2)))
print("Highest Scoring Subject: " + best_subject + " (" + str(highest) + ")")
print("Lowest Scoring Subject: " + worst_subject + " (" + str(lowest) + ")")

# keep asking the user to add new subjects until they type done
print("")
print("--- Add New Subjects ---")
print("(Type 'done' as the subject name to stop)")

count_added = 0

while True:
    new_subject = input("Enter subject name: ")
    new_subject = new_subject.strip()

    if new_subject.lower() == "done":
        break

    new_mark_input = input("Enter marks for " + new_subject + " (0-100): ")
    new_mark_input = new_mark_input.strip()

    # make sure the mark is actually a number
    try:
        new_mark = float(new_mark_input)
    except ValueError:
        print("Warning: Invalid input. Marks must be a number. Entry skipped.")
        print("")
        continue

    # make sure the number is between 0 and 100
    if new_mark < 0 or new_mark > 100:
        print("Warning: Marks must be between 0 and 100. Entry skipped.")
        print("")
        continue

    # if we get here the input was fine so we add it
    subjects.append(new_subject)
    marks.append(new_mark)
    count_added = count_added + 1
    print("Successfully added " + new_subject + " with " + str(new_mark) + " marks.")
    print("")

print("")
print("--- Final Update ---")
print("New subjects added: " + str(count_added))

# recalculate average with any new subjects added
new_total = 0
for m in marks:
    new_total = new_total + m
new_average = new_total / len(marks)

print("Updated Average Marks: " + str(round(new_average, 2)))
print("")




# Task 3

class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma",   [55, 68, 49, 72, 61]),
    ("Priya Nair",    [91, 85, 88, 94, 79]),
    ("Karan Mehta",   [40, 55, 38, 62, 50]),
    ("Sneha Pillai",  [75, 80, 70, 68, 85]),
]

passed_count = 0
failed_count = 0
topper_name = ""
highest_avg = 0
total_of_all_averages = 0

# print the header row for the table
print(f"{'Name':<17} | {'Average':<7} | Status")
print("-" * 40)

for name, marks in class_data:

    # calculate average for this student
    total = 0
    for m in marks:
        total = total + m
    avg = total / len(marks)

    total_of_all_averages = total_of_all_averages + avg

    # pass if average is 60 or above
    if avg >= 60:
        status = "Pass"
        passed_count = passed_count + 1
    else:
        status = "Fail"
        failed_count = failed_count + 1

    # check if this student has the highest average so far
    if avg > highest_avg:
        highest_avg = avg
        topper_name = name

    print(f"{name:<17} | {avg:>7.2f}  | {status}")

class_average = total_of_all_averages / len(class_data)

print("")
print("--- Summary ---")
print("Passed: " + str(passed_count))
print("Failed: " + str(failed_count))
print("Class Topper: " + topper_name + " (" + str(round(highest_avg, 2)) + ")")
print("Class Average: " + str(round(class_average, 2)))
print("")




# Task 4

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# step 1 - remove the extra spaces at the start and end
clean_essay = essay.strip()

# step 2 - print in title case
print("--- Step 2: Title Case ---")
print(clean_essay.title())
print("")

# step 3 - count how many times python appears
count = clean_essay.count("python")
print("--- Step 3: Word Count ---")
print("'python' appears: " + str(count) + " times")
print("")

# step 4 - replace python with Python and the snake emoji
new_essay = clean_essay.replace("python", "Python 🐍")
print("--- Step 4: Replaced Text ---")
print(new_essay)
print("")

# step 5 - split into a list of sentences
sentences = clean_essay.split(". ")
print("--- Step 5: List of Sentences ---")
print(sentences)
print("")

# step 6 - print each sentence with a number in front
print("--- Step 6: Numbered Sentences ---")
number = 1
for sentence in sentences:
    # add a period at the end if it doesnt already have one
    if sentence.endswith(".") == False:
        sentence = sentence + "."
    print(str(number) + ". " + sentence)
    number = number + 1



#Output

"""
Valid name
====================
Student: Ayesha Sharma
Roll No: 101
Marks: [88, 72, 95, 60, 78]
====================

Valid name
====================
Student: Rohit Verma
Roll No: 102
Marks: [55, 68, 49, 72, 61]
====================

Valid name
====================
Student: Priya Nair
Roll No: 103
Marks: [91, 85, 88, 94, 79]
====================

Valid name
====================
Student: Karan Mehta
Roll No: 104
Marks: [40, 55, 38, 62, 50]
====================

Valid name
====================
Student: Sneha Pillai
Roll No: 105
Marks: [75, 80, 70, 68, 85]
====================

Requirement for Roll No 103
ALL CAPS: PRIYA NAIR
lowercase: priya nair

--- Grade Report for Ayesha Sharma ---
Math: 88 - Grade: A
Physics: 72 - Grade: B
CS: 95 - Grade: A+
English: 60 - Grade: C
Chemistry: 78 - Grade: B

--- Current Statistics ---
Total Marks: 393
Average Marks: 78.6
Highest Scoring Subject: CS (95)
Lowest Scoring Subject: English (60)

--- Add New Subjects ---
(Type 'done' as the subject name to stop)
Enter subject name: math
Enter marks for math (0-100): 77
Successfully added math with 77.0 marks.

Enter subject name: done

--- Final Update ---
New subjects added: 1
Updated Average Marks: 78.33

Name              | Average | Status
----------------------------------------
Ayesha Sharma     |   78.60  | Pass
Rohit Verma       |   61.00  | Pass
Priya Nair        |   87.40  | Pass
Karan Mehta       |   49.00  | Fail
Sneha Pillai      |   75.60  | Pass

--- Summary ---
Passed: 4
Failed: 1
Class Topper: Priya Nair (87.4)
Class Average: 70.32

--- Step 2: Title Case ---
Python Is A Versatile Language. It Supports Object Oriented, Functional, And Procedural Programming. Python Is Widely Used In Data Science And Machine Learning.

--- Step 3: Word Count ---
'python' appears: 2 times

--- Step 4: Replaced Text ---
Python 🐍 is a versatile language. it supports object oriented, functional, and procedural programming. Python 🐍 is widely used in data science and machine learning.

--- Step 5: List of Sentences ---
['python is a versatile language', 'it supports object oriented, functional, and procedural programming', 'python is widely used in data science and machine learning.']

--- Step 6: Numbered Sentences ---
1. python is a versatile language.
2. it supports object oriented, functional, and procedural programming.
3. python is widely used in data science and machine learning."""