#lists
# students = ["Hermione", "Harry", "Ron"]

# print(students[1])

# for student in students:
#   print(student)

# for i in range(len(students)):
#   print(i + 1, students[i])

# for count, student_name in enumerate(students, start=1):
#     print(count, student_name)

#dic
# students = {
#   "Hermione": "Gryffindor",
#   "Harry": "Gryffindor", 
#   "Ron": "Gryffindor",
#   "Draco": "Slytherin"
# }

# print(students["Hermione"])
# print(students["Draco"])

# for student in students:
#   print(student, students[student], sep=", ")


# for name, house in students.items():
#   print(name, house, sep=", ")

#3:45 yt

students = [
  {"name":"Hermione", "house": "Gryffindor", "patronus": "Otter"},
  {"name":"Harry", "house": "Gryffindor", "patronus": "Stag"}, 
  {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
  {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
  print(student["name"])

  #s:48yt