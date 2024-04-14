#!/usr/local/bin/python3

# Below references have been used to write this Program in Python
# https://www.packetswitch.co.uk/how-to-create-tables-python-tabulate-module/
# https://docs.python.org/3/howto/sorting.html
# https://stackoverflow.com/questions/70261334/how-to-rearrange-from-lowest-to-highest-value-in-python
# https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
# https://stackoverflow.com/questions/43432675/sort-a-list-in-reverse-order

from tabulate import tabulate
from operator import itemgetter

subject_names = []
student_names = [] 
student_scores = []

def banner(message):
    print(56*' ')
    print(56*'*')
    print('*' + 54*' ' + '*')
    print('*' + 17*' ' + (message) + 18*' ' + '*')
    print('*' + 54*' ' + '*')
    print(56*'*')

def student_score():  
    # Input subject details
    subject_count = input("Enter the Number of Subjects: ")
    if ' ' in subject_count:
        subject_count = subject_count.replace(' ', '')

    for i in range(int(subject_count)):
        subject_name = input(f"Enter the Name of Subject {i + 1}: ")
        if ' ' in subject_name:
            subject_name = subject_name.strip(' ')
        subject_names.append(subject_name)

    # Input scores for each student
    student_record = []
    serial_no = []
    student_count = input("Enter Number of Students: ")
    if ' ' in student_count:
        student_count = student_count.replace(' ', '')

    for i in range(int(student_count)):
        name = input(f"Enter name of the Student {i + 1}: ")
        if ' ' in name:
            name = name.strip(' ')
        student_names.append(name)
        serial_no.append(str(i+1))

        print(f"Enter test scores for {name}:")
        scores = []
        for j in range(int(subject_count)):
            score = input(f"Enter score for {subject_names[j]}: ")
            if ((' ' in score) and (int(score) <= 100)):
                score = score.strip(' ')
            scores.append(int(score))
            
        student_record.append([name] + scores)
        student_scores.append(scores)

    banner(message='Student Score Table')
    headers = ["Student Name"] + subject_names
    # Create a table with index
    print(tabulate(student_record, headers=headers,
          showindex=serial_no, tablefmt="heavy_grid"))

def student_rank(subject_names, student_scores, student_names):
    # Get number of Subjects & Students
    subject_count = len(subject_names)
    student_count = len(student_names)
    final_rank_record = []
    temp_rank_record = []
    
    # Aggregate score of all subjects for a student
    for x in range(student_count):
        name = []
        totalscore = []
        avgscore = []
        gpa = []
        t = 0
        for y in range(subject_count):
            t = student_scores[x][y] + t
            avg_score = t/subject_count
            if avg_score >= 90:
                GPA = str(4.0)
            elif 85 <= avg_score < 90:
                GPA = str(3.5)
            elif 80 <= avg_score < 85:
                GPA = str(3.0)
            elif 75 <= avg_score < 80:
                GPA = str(2.5)
            elif 70 <= avg_score < 75:
                GPA = str(2.0)
            elif 65 <= avg_score < 70:
                GPA = str(1.5)
            elif 60 <= avg_score < 65:
                GPA = str(1.0)
            else:
                GPA = str(0.0)

        name.append(student_names[x])
        totalscore.append(int(t))
        avgscore.append(float(avg_score))
        gpa.append(GPA)
        temp_rank_record.append(name + totalscore + avgscore + gpa) 
    
    sorted_rank_record = sorted(temp_rank_record, key=itemgetter(1), reverse=True)
    # print(sorted_rank_record)
    i=0
    for subrecord in sorted_rank_record:
        rank_index = []
        rank_name = []
        rank_totalscore = []
        rank_avgscore = []
        rank_gpa = []
        i=i+1
        rank_index.append(str(i))
        rank_name.append(subrecord[0])
        rank_totalscore.append(subrecord[1])
        rank_avgscore.append(subrecord[2])
        rank_gpa.append(subrecord[3])
        final_rank_record.append(rank_index + rank_name + rank_totalscore + rank_avgscore + rank_gpa)     
    # print(final_rank_record)
    banner(message='Students Rank Table')
    headers = ["Rank"]+["Student Name"]+["Total Score"]+["Average Score"]+["GPA"]
    # Create a table with index
    print(tabulate(final_rank_record, headers=headers, tablefmt="heavy_grid"))    
        
student_score()
student_rank(subject_names, student_scores, student_names)
