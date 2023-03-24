from student import Student

name = input("Enter the name of a student: ")

# initialize student0
student0 = Student(name, 5)

print() # print newline for formatting

# print student0's name
print("Name: {}".format(student0.getName()), '\n')

# print first score in list of student0
print("Score 0: {}".format(student0.getScore(0)))

# change score 0
student0.setScore(0, int(input("Input the first score: ")))

# print first score again to see changed value
print("Score 0: {}".format(student0.getScore(0)), '\n')

# set student0's other scores
student0.setScore(1, 34)
student0.setScore(2, 50)
student0.setScore(3, 74)
student0.setScore(4, 93)

# print the average score of student0
print("Average score: {}".format(student0.getAverage()))

# print student0's highest score
print("High score: {}".format(student0.getHighScore()), '\n')

# print all of student0's information
print(student0)

# change student0's name
student0.setName(str(input("Input a new name for the student: ")))

print() # print newline for formatting

# print student0's new name
print("Name: {}".format(student0.getName()), '\n')

# make a new student: student1
student1 = Student("Alice", 5)

# set student1's scores
student1.setScore(0, 75)
student1.setScore(1, 82)
student1.setScore(2, 92)
student1.setScore(3, 76)
student1.setScore(4, 98)

# compare student0 with student1 and print result
print("{0}'s average is {1} {2}'s average.".format(student0.getName(), student0.compare(student1), student1.getName()))

# compare student1 with student0 and print result
print("{0}'s average is {1} {2}'s average.".format(student1.getName(), student1.compare(student0), student0.getName()))
