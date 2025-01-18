

#!/usr/bin/python
#requirement :pip install googletrans==3.1.0a0

import os 
import sys
from termcolor import colored
from PyPDF2 import PdfReader,PdfWriter
from googletrans import Translator
from gtts import gTTS
#IMPORT FILE
while True:
    file_inp = input('nhap ten file hoac duong dan file : ')
    if file_inp[len(file_inp)-3:] in ['txt','pdf','docx']:
        break
    print('Ten file khong hop le hoac duong dan khong dung !')




#WRITE FILE TO TXT
percent = 0
# pdf_reader = PdfReader(file_name)
# number_of_pages = len(pdf_reader.pages)
file_out = open(f'{file_inp[:len(file_inp)-4]}_copy.txt',mode='w',encoding='utf-8-sig')
# check file exist
def exist_file(name_file):
    file_stats = os.stat(name_file)
    if file_stats.st_size > 0:
        os.remove(name_file)
        open(name_file,mode = 'w').close()
#sort library 

stack_word = ['_']
def sort_file(text_line):
    global file_out
    if len(text_line.split()) == 0 and stack_word[0] != '':
        t  = Translator()
        trans = t.translate(stack_word[0],src='en',dest='vi')
        vi = trans.text
        file_out.write(vi + ' \n')
        stack_word[0] = '_'
    stack_word[0] += text_line
    print(stack_word)







exist_file(f'{file_inp[:len(file_inp)-4]}_copy.txt')
#TRANSLATE FILE PDF
language = 'en'

file_inp = open(file_inp,mode='r',encoding='utf-8-sig')
reader = file_inp.readline()
while reader != '':
    # page = pdf_reader.pages[i]
    # text = page.extract_text()
    # if len(text) != 0 :
    #     trans = t.translate(text,src='en',dest='vi')
    #     vi = trans.text
    #     # sort_file(vi)
    #     file_txt.write(vi)
    #     percent = (i+1)*100/number_of_pages
    #     print(f'Loading {round(percent,2)}%')
    sort_file(reader)
    reader = file_inp.readline()
file_out.close()

