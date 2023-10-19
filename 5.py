from collections import namedtuple
Student = namedtuple('Student', 'name age grade city')
students = (
   Student('Елена', '13', 3.3, 'Москва'),
   Student('Ольга', '21', 4.9, 'Омск'),
   Student('Елизавета', '17', 4.8, 'Новосибирск'),
   Student('Дмитрий', '18', 4, 'Челябинск'),
   Student('Максим', '17', 4.2, 'Мурманск'),
   Student('Никола', '18', 3.5, 'Владивосток'),
   Student('Алексей', '16', 5, 'Махачкала')
)
def gs(students):
   tg = 0

   for student in students:
       tg += student.grade
   a = tg / len(students)

   g = [student.name for student in students if student.grade >= a]
   print('Ученики ', ', '.join(g), ' в этом семестре хорошо учатся!')

gs(students)
