from random import *
import os

class creat_list:

    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.student_path = os.path.join(self.path, 'data', 'student.txt')
        self.teacher_path = os.path.join(self.path, 'data', 'teacher.txt')

        self.name = ['duong', 'anh', 'cuong', 'dat', 'hoang', 'viet',
                     'dung', 'ngoc', 'thu', 'tien', 'thao', 'binh', 'an']
        self.midlename = ['huy', 'van', 'chi', 'nhu',
                          'ngoc', 'thi', 'manh', 'ngoc', 'tien']
        self.surname = ['truong', 'nguyen', 'le',
                        'tran', 'pham', 'dang', 'ta', 'do']
        self.gender = ['nam', 'nu']
        self.rank = ['y', 'tb', 'k', 'g']
        self.alpha = ['a', 'b', 'c']
        # self.student_year = ['2005', '2006', '2007', '2008']
        self.student_year = ['2005']
        self.teacher_year = ['1990', '1996', '1989', '1983', '1989', '1995']
        self.subject = ['toan', 'ly', 'hoa', 'su', 'dia',
                        'sinh', 'gdcd', 'anh', 'van', 'congnghe', 'tin']

    def file_out(self):
        file_student = open(self.student_path, mode='w')
        file_teacher = open(self.teacher_path, mode='w')
        file_student_stats = os.stat(self.student_path)
        file_teacher_stats = os.stat(self.teacher_path)
        if file_student_stats.st_size > 0:
            os.remove(self.student_path)
            open(self.student_path, mode='w').close()

        if file_teacher_stats.st_size > 0:
            os.remove(self.teacher_path)
            open(self.teacher_path, mode='w').close()
        else:
            for i in range(1000):
                file_student.write(
                    str(f'{randint(1,9)}{randint(1,9)}{randint(1,9)}{randint(1,9)}{randint(1,9)}{randint(1,9)}') + '#' +
                    choice(self.surname) + ' ' + choice(self.midlename) + ' ' + choice(self.name) + '#' +
                    str(randint(1, 31)) + '/' + str(randint(1, 12)) + '/' + choice(self.student_year) + '#' +
                    choice(self.gender) + '#' +
                    '12' + choice(self.alpha) + str(randint(1, 3)) + '\n')
            for j in range(60):
                file_teacher.write(str(randint(0, 9)) + str(randint(100, 999)) + '#' +
                                   choice(self.surname) + ' ' + choice(self.midlename) + ' ' + choice(self.name) + '#' +
                                   str(randint(1, 31)) + '/' + str(randint(1, 12)) + '/' + choice(self.teacher_year) + '#' +
                                   choice(self.gender) + '#' +
                                   choice(self.subject) + '#'
                                   f'09{randint(1,9)}{randint(1,9)}{randint(1,9)}{randint(1,9)}{randint(1,9)}{randint(1,9)}{randint(1,9)}{randint(1,9)}' + '\n')
            print('creating file completed')


class creat_point:
    def __init__(self):
        self.id = {}
        self.year = {}
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.student_path = os.path.join(self.path, 'student.txt')
        file = open(self.student_path, 'r')
        file_point = open('data.json', 'w')
        f = file.readline()
        while f != '':
            f = f.strip('\n')
            f = f.split('#')
            self.id[f[0]] = f[1:]
            if f[2][-4:] not in self.year:
                self.year[f[2][-4:]] = [f[0]]
            else:
                self.year[f[2][-4:]].append(f[0])
            f = file.readline()
        for i in self.year['2005']:
            print(self.id[i])


creat_list().file_out()

# creat_point()
