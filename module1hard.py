grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
import statistics
grades = [statistics.mean([5, 3, 3, 5, 4]), statistics.mean([2, 2, 2, 3]), statistics.mean([4, 5, 5, 2]), statistics.mean([4, 4, 3]),statistics.mean( [5, 5, 5, 4, 5])]
print(grades)
students = list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
students.sort()
print(students)
diary={students[0]:grades[0],students[1]:grades[1], students[2]:grades[2],students[3]:grades[3],students[4]:grades[4]}
print(diary)

