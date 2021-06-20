class Director_room:
    number=100
    name="Кабинет директора"
    access=3

class Teacher_room:
    number=101
    name = "Учительская"
    access = 2

class CLass_room:
    number=102
    name = "Кабинет для занятий"
    access = 1

class Act_room:
    name = "Актовый зал"
    number=103
    access = 0

class Directors:
    clas="Директор"
    name="Иван"
    surname="Иванов"
    access=3
    ficha = "Количество наград - 13"

class Teachers:
    clas="Учитель"
    name="Влад"
    surname="Савельев"
    access=2
    ficha = "Любимая шутка - про Вовочку"

class Pupils:
    clas="Ученик"
    name="Марк"
    surname="Белоухов"
    access=1
    ficha="Любимый предмет - Математика"

class Parents:
    clas="Родитель"
    name="Игорь"
    surname="Белоухов"
    access=0
    ficha="Любимый учитель - учитель математики"

dirroom=Director_room()
teachroom=Teacher_room()
classroom=CLass_room()
actroom=Act_room()

director=Directors()
teacher=Teachers()
pupil=Pupils()
parent=Parents()

print(f"{dirroom.name}, {dirroom.number}")
print(f"{teachroom.name}, {teachroom.number}")
print(f"{classroom.name}, {classroom.number}")
print(f"{actroom.name}, {actroom.number}")
print()
print(f"{director.clas}, {director.name} {director.surname}, {director.ficha} ")
print(f"{teacher.clas}, {teacher.name} {teacher.surname}, {teacher.ficha} ")
print(f"{pupil.clas}, {pupil.name} {pupil.surname}, {pupil.ficha} ")
print(f"{parent.clas}, {parent.name} {parent.surname}, {parent.ficha} ")
print()
print(f"{parent.clas} {parent.name} {parent.surname} пытается войти в {dirroom.name} {dirroom.number}: {parent.access>=dirroom.access}")
print(f"{parent.clas} {parent.name} {parent.surname} пытается войти в {teachroom.name} {teachroom.number}: {parent.access>=teachroom.access}")
print(f"{parent.clas} {parent.name} {parent.surname} пытается войти в {classroom.name} {classroom.number}: {parent.access>=classroom.access}")
print(f"{parent.clas} {parent.name} {parent.surname} пытается войти в {actroom.name} {actroom.number}: {parent.access>=actroom.access}")
print()
print(f"{director.clas} {director.name} {director.surname} пытается войти в {actroom.name} {actroom.number}: {director.access>=actroom.access}")
print(f"{teacher.clas} {teacher.name} {teacher.surname} пытается войти в {actroom.name} {actroom.number}: {teacher.access>=actroom.access}")
print(f"{pupil.clas} {pupil.name} {pupil.surname} пытается войти в {actroom.name} {actroom.number}: {pupil.access>=actroom.access}")
print(f"{parent.clas} {parent.name} {parent.surname} пытается войти в {actroom.name} {actroom.number}: {parent.access>=actroom.access}")
print()
print(f"{pupil.clas} {pupil.name} {pupil.surname} пытается войти в {dirroom.name} {dirroom.number} {pupil.access>=dirroom.access}")