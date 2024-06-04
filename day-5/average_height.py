student_heights = input('enter the student heigts ').split()
for nasty in range(0, len(student_heights)):
    student_heights[nasty] = int(student_heights[nasty])

total_height = 0
number_of_students = 0
for height in student_heights:
    total_height += height
for height in student_heights:
    number_of_students += 1
average_height = total_height / number_of_students
average_height_rounded = round(average_height)
print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height_rounded}")
