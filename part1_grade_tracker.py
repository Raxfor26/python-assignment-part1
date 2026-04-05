#Task 1


raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]


cleaned_students = []

for students in raw_students:

    cleaned_name = students["name"].strip().title()

    cleaned_roll = int(students["roll"])

    cleaned_marks = [int(mark) for mark in students["marks_str"].split(", ")]
    

    is_valid_name = cleaned_name.replace(" ", "").isalpha()
    
    if is_valid_name:
        print('Valid name')
    else:
        print('Invalid name')      
        
  
    cleaned_students.append({
        "name": cleaned_name,
        "roll": cleaned_roll,
        "marks_str": cleaned_marks
    })       

    print('====================')
    print(f"Student: {cleaned_name}")
    print(f"Roll No: {cleaned_roll}")
    print(f"Marks: {cleaned_marks}")
    print('====================\n')

print('Requirement for Roll No 103')
for students in cleaned_students:
    if students['roll'] == 103:
        print(f"ALL CAPS: {students['name'].upper()}")
        print(f"lowercase: {students['name'].lower()}\n")
        break





#Task 2


# --- Initial Data ---
student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

# --- Part 1: For Loop & Grade Assignment ---
print(f"--- Grade Report for {student_name} ---")

for i in range(len(subjects)):
    sub = subjects[i]
    score = marks[i]
    
    # Determine the grade based on the score
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
        
    print(f"{sub}: {score} - Grade: {grade}")

# --- Part 2: Calculate Statistics ---
total_marks = sum(marks)
average_marks = total_marks / len(marks)

# Find the highest and lowest scores
max_mark = max(marks)
max_index = marks.index(max_mark)
highest_sub = subjects[max_index]

min_mark = min(marks)
min_index = marks.index(min_mark)
lowest_sub = subjects[min_index]

print("\n--- Current Statistics ---")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Highest Scoring Subject: {highest_sub} ({max_mark})")
print(f"Lowest Scoring Subject: {lowest_sub} ({min_mark})")

# --- Part 3: While Loop (Interactive Entry) ---
print("\n--- Add New Subjects ---")
print("(Type 'done' as the subject name to stop)")

new_subjects_count = 0

while True:
    new_sub = input("Enter subject name: ").strip()
    
    # Check for the exit condition
    if new_sub.lower() == 'done':
        break
        
    mark_input = input(f"Enter marks for {new_sub} (0-100): ").strip()
    
    # Validate the input using a try-except block
    try:
        new_mark = float(mark_input) # Using float handles both decimals and integers
        
        # Check if the number is within the valid range
        if new_mark < 0 or new_mark > 100:
            print("⚠️ Warning: Marks must be between 0 and 100. Entry skipped.\n")
            continue
            
    except ValueError:
        # If float() fails, it wasn't a number
        print("⚠️ Warning: Invalid input. Marks must be a number. Entry skipped.\n")
        continue
        
    # If we reach here, the input is valid!
    subjects.append(new_sub)
    marks.append(new_mark)
    new_subjects_count += 1
    print(f"✓ Successfully added {new_sub} with {new_mark} marks.\n")

# --- Part 4: Final Summary ---
print("\n--- Final Update ---")
print(f"New subjects added: {new_subjects_count}")

# Recalculate average with the updated lists
updated_average = sum(marks) / len(marks)
print(f"Updated Average Marks: {updated_average:.2f}\n")





#Task 3


class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

# 1. Variables to track our summary statistics
passed_count = 0
failed_count = 0
highest_avg = 0
topper_name = ""
sum_of_averages = 0

# 2. Print the table header
print(f"{'Name':<17} | {'Average':<7} | Status")
print("-" * 40)

# 3. Loop through the data to process each student
for name, marks in class_data:
    # Calculate average
    student_avg = sum(marks) / len(marks)
    sum_of_averages += student_avg
    
    # Determine status and update counts
    if student_avg >= 60:
        status = "Pass"
        passed_count += 1
    else:
        status = "Fail"
        failed_count += 1
        
    # Check if this student is the new topper
    if student_avg > highest_avg:
        highest_avg = student_avg
        topper_name = name
        
    # Print the formatted row
    # <17 means left-align with 17 spaces, >7.2f means right-align with 7 spaces & 2 decimal points
    print(f"{name:<17} | {student_avg:>7.2f}  | {status}")

# 4. Calculate final class average
class_average = sum_of_averages / len(class_data)

# 5. Print the summary
print("\n--- Summary ---")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Topper: {topper_name} ({highest_avg:.2f})")
print(f"Class Average: {class_average:.2f}\n")




#Task 4

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# --- Step 1: Strip Whitespace ---
clean_essay = essay.strip()

# --- Step 2: Convert to Title Case ---
print("--- Step 2: Title Case ---")
print(clean_essay.title())
print() # Adding empty prints just to make the terminal output easier to read

# --- Step 3: Count 'python' ---
# The hint correctly notes that clean_essay is completely lowercase already
count_python = clean_essay.count("python")
print("--- Step 3: Word Count ---")
print(f"'python' appears: {count_python} times")
print()

# --- Step 4: Replace 'python' with 'Python 🐍' ---
replaced_essay = clean_essay.replace("python", "Python 🐍")
print("--- Step 4: Replaced Text ---")
print(replaced_essay)
print()

# --- Step 5: Split into sentences ---
sentences = clean_essay.split(". ")
print("--- Step 5: List of Sentences ---")
print(sentences)
print()

# --- Step 6: Numbered & Formatted Sentences ---
print("--- Step 6: Numbered Sentences ---")
# Using enumerate() allows us to easily get both the index (starting at 1) and the sentence
for index, sentence in enumerate(sentences, start=1):
    # Ensure every sentence ends with a period
    if not sentence.endswith("."):
        sentence += "."
        
    print(f"{index}. {sentence}")


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
Average Marks: 78.60
Highest Scoring Subject: CS (95)
Lowest Scoring Subject: English (60)

--- Add New Subjects ---
(Type 'done' as the subject name to stop)
Enter subject name: done

--- Final Update ---
New subjects added: 0
Updated Average Marks: 78.60

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
Class Topper: Priya Nair (87.40)
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