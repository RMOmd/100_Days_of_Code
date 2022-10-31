students_hieghts = input("Input a list of students heights ").split()
for n in range(0, len(students_hieghts)):
    students_hieghts[n] = int(students_hieghts[n])
print(students_hieghts)
total_height = 0
for h in students_hieghts:
    total_height += h
number_of_students = 0
for student in students_hieghts:	
	number_of_students +=1
average_height = round(total_height / number_of_students)
print(average_height)
	