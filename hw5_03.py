tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def classmates_names():
    name = 0
    room = 0
    while name < len(klasses):
        if name >= len(tutors):
            yield (klasses[name], None)
        else:
            yield (tutors[room], klasses[name])
        name += 1
        room += 1


for pupil in classmates_names():
    print(pupil)
