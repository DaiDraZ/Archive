#!/usr/bin/env python

import os
import numpy

# += \n


class PATH:
    def __init__(self) -> None:
        self.src_dir = os.path.dirname(os.path.abspath(__file__))
        self.parent_dir = os.path.abspath(os.path.join(self.src_dir, '..'))
        self.img_dir = os.path.join(
            self.parent_dir, 'assets', 'data-server.png')
        self.data_dir = os.path.join(self.parent_dir, 'data')


class FILE(PATH):
    def __init__(self) -> None:
        super().__init__()
        # INJECTION().decrypt(file_zf='student.zf',file_txt='student.txt')
        # INJECTION().decrypt(file_zf='teacher.zf',file_txt='teacher.txt')

        self.teacher_file = open(os.path.join(
            self.data_dir, 'teacher.txt'), encoding='utf-8')
        self.student_file = open(os.path.join(
            self.data_dir, 'student.txt'), encoding='utf-8')

        self.teacher_data = []
        self.student_data = []

    def IMPORT(self, selection: str):
        if selection == 'A':
            self.READ(self.teacher_file, self.teacher_data)
            self.READ(self.student_file, self.student_data)

        if selection == 'T':
            self.READ(self.teacher_file, self.teacher_data)

        if selection == 'S':
            self.READ(self.student_file, self.student_data)
        # os.remove(os.path.join(self.data_dir, 'teacher.txt'))
        # os.remove(os.path.join(self.data_dir, 'student.txt'))

    def READ(self, file, lists: list):
        temp = file.readline()
        while temp != '':
            data = temp.strip('\n').split('#')
            lists.append(data)
            temp = file.readline()

    def WRITE(self, file, data: list):
        pass

    def CLOSE(self, file):
        file.close()


class INJECTION:
    def __init__(self) -> None:
        self.data_dir = PATH().data_dir 
        self.__key = 123
    
    def xor_marker(self, data):
        return bytearray([b ^ self.__key for b in data])

    def encrypt(self, file_txt ,file_zf):
        with open(os.path.join(PATH().data_dir, file_txt), 'rb') as data:
            file_data = data.read()
            enc_data = self.xor_marker(file_data)

        with open(os.path.join(PATH().data_dir, file_zf), 'wb') as enc_file:
            enc_file.write(enc_data)
            os.remove(os.path.join(self.data_dir,file_txt))
    def decrypt(self, file_zf, file_txt):
        with open(os.path.join(PATH().data_dir, file_zf), 'rb') as enc_file:
            enc_data = enc_file.read()
            dec_data = self.xor_marker(enc_data)

        with open(os.path.join(PATH().data_dir, file_txt), 'wb') as dec_file:
            dec_file.write(dec_data)
            os.remove(os.path.join(self.data_dir,file_zf))# .txt -> .zf 



