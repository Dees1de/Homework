grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
for i in range(len(grades)):
    grades[i]=sum(grades[i])/len(grades[i])
grades_students = dict(zip(sorted(list(students)),grades))
print(grades_students)