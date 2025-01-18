#!usr/bin/python3


from tkinter import *
from tkinter.ttk import *
from tkinter import colorchooser, filedialog, messagebox
from tkinter.messagebox import askyesno
import math as m
import os
from pathlib import Path, PurePath
import math
# Import main library
from ntpath import abspath
from set_theme import Themes


class App(Tk):
    "Gui created by Tkinter Library"

    def __init__(self):
        super().__init__()
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.option = ['Standard', 'Scientific',
                       'Graphing', 'Programer', 'Date calculation',
                       'Currency', 'Volume', 'Lenght', 'Weight and mass',
                       'Temperature', 'Energy', 'Area', 'Time',
                       'Power', 'Data', 'Pressure', 'Angle']
        # self.class_set = (Standard, Scientific,
        #     Graphing, Programer, Date_calc,
        #     Currency, Volume, Lenght, Weight_and_mass,
        #     Temperature, Energy, Area, Time,
        #     Power, Data, Pressure, Angle)
        self.listbox_visible = True
        self.bg_color = '#202020'
        self.font_and_size = ['arial', 20]
        self.expression = ["", ""]

        self.dictframe = {}
        for F in (Standard, Date_calc):
            name = F.__name__
            frames = F(self, self.bg_color)
            self.dictframe[name] = frames
            frames.place(relwidth=1, relheight=1)
        self.title('CALCULATOR')
        self.setup_window()
        self.setup_styles()

        # Set up UI dimensions and constraints
        self.creat_window()

    def show_frame(self, frame):
        self.child_frame = self.dictframe[frame]  # Standard là một Frame
        self.child_frame.tkraise()

        self.sub_frame = Frame(self.child_frame)
        self.collumn_menu = Frame(self.sub_frame, style='t.TFrame')
        self.collumn_menu.place(relwidth=1, relheight=1)
        self.listbox_left()

    def creat_window(self):
        self.creat_menu()
        self.show_frame('Standard')

    def setup_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = screen_width // 4
        window_height = screen_height * 2 // 3
        base_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.abspath(os.path.join(base_dir, '..'))
        img_dir = os.path.join(project_dir, 'image')

        self.geometry(f'{window_width+1}x{window_height}')
        self.minsize(window_width - 10, window_height)
        self.maxsize(screen_width, screen_height)

        self.icon = PhotoImage(file=os.path.join(img_dir,'calc.png'))
        self.iconphoto(False, self.icon)

    def setup_styles(self):
        self.style_gui = Style()
        self.style_gui.theme_use('alt')
        self.style_gui.configure('l.TFrame', background=self.bg_color)
        self.style_gui.configure('r.TFrame', background=self.bg_color)

        self.style_gui.configure(
            'b.TButton',
            background='#323232',
            focuscolor='none',
            relief='flat',
            foreground='white',
            border=0,
            highlichtthickness=0)
        self.style_gui.configure(
            'sub.TButton',
            background=self.bg_color,
            focuscolor='none',
            relief='flat',
            foreground='white',
            border=0,
            highlichtthickness=0)
        self.style_gui.configure('t.TFrame', background=self.bg_color)
        self.style_gui.configure('lb1.TLabel', background=self.bg_color)
        self.style_gui.configure('lb2.TLabel', background=self.bg_color)
        self.style_gui.map('b.TButton', background=[('active', '#3B3B3B')])
        self.style_gui.map('sub.TButton',
                           background=[('disabled', self.bg_color), ('active', '#3B3B3B')])

    def theme(self):
        self.call_theme = Themes()
        self.call_theme.start()

    def pick_color(self) -> None:
        self.bg_color = colorchooser.askcolor()[1]
        self.ev_change_color()

    def ev_change_color(self):
        self.style_gui.configure('l.TFrame', background=self.bg_color)
        self.style_gui.configure('r.TFrame', background=self.bg_color)
        self.style_gui.configure('b.TButton', background=self.bg_color)
        self.style_gui.configure('sub.TButton', background=self.bg_color)
        self.style_gui.configure('t.TFrame', background=self.bg_color)
        self.style_gui.configure('lb1.TLabel', background=self.bg_color)
        self.style_gui.configure('lb2.TLabel', background=self.bg_color)

    def creat_menu(self):
        menubar = Menu(self)
        menubar.add_cascade(label='Option',
                            command=self.ev_toggle_list,)
        # main menus
        optionmenu = Menu(menubar, tearoff=0)
        optionmenu.add_command(label='Open')
        optionmenu.add_command(label='Save')
        # sub optionmenu
        sub_optionmenu = Menu(optionmenu, tearoff=0)
        sub_optionmenu.add_command(label='History')
        sub_optionmenu.add_command(label='Charity')
        sub_optionmenu.add_command(label='Map')
        # submenu <- optionmenu <- menubar
        optionmenu.add_cascade(label='More', menu=sub_optionmenu)

        menubar.add_cascade(label='View', menu=optionmenu)  # add name bar

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label='Theme setting', command=self.theme)
        editmenu.add_command(label='Font setting', command=self.theme)
        menubar.add_cascade(label='Edit', menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label='Document')
        helpmenu.add_command(label='About me')
        helpmenu.add_command(label='Donate :)')
        menubar.add_cascade(label='Help', menu=helpmenu)
        self.config(menu=menubar)

    def ev_toggle_list(self):
        if self.listbox_visible:
            self.sub_frame.place(relheight=1, width=300)
            self.list_option.insert(END, *self.option)
        else:
            self.sub_frame.place_forget()
            self.list_option.delete(0, END)
        self.listbox_visible = not self.listbox_visible

    def listbox_left(self):
        self.scroll_bar = Scrollbar(self.collumn_menu,
                                    orient=VERTICAL)
        self.scroll_bar.pack(side=RIGHT, fill='y')
        self.list_option = Listbox(
            self.collumn_menu,
            font='arial 15',
            width=300,
            bg=self.bg_color,
            fg='white',
            relief='flat',
            activestyle='none',
            bd=1,
            highlightthickness=0)

        self.list_option.bind('<<ListboxSelect>>', self.choice_listbox)
        self.list_option.pack(side=LEFT, fill=BOTH)
        self.list_option.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.list_option.yview)

    def choice_listbox(self, event):
        # Kiểm tra nếu có phần tử nào được chọn trong Listbox
        selection = event.widget.curselection()
        self.sub_frame.destroy()
        if selection:
            option = selection[0]  # Lấy chỉ số của phần tử được chọn
            # Lấy tên của frame tương ứng
            selected_option = self.option[option]

            if selected_option == 'Date calculation':
                self.show_frame('Date_calc')  # Hiển thị frame 'Date_calc'
            else:
                self.show_frame('Standard')  # Hiển thị frame 'Standard'

            print(f'[DEBUG] {selected_option}')
        else:
            print('[DEBUG] No selection in Listbox')

    def exit_program(self):
        self.ask = askyesno(title="QUIT", message="Do you want to exit ?")
        if self.ask:
            self.destroy()

    def start(self):
        self.protocol('WM_DELETE_WINDOW', self.exit_program)
        self.mainloop()


class Standard(Frame):
    def __init__(self, parent, bg_color):
        super().__init__(parent)  # class Standard sẽ đc chứa bởi parent
        self.expression = ['', '', '']
        self.grep_str = ""
        self.num = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
        self.exp = ('+', '-', '*', '/')
        self.math = ('1/x', 'sqrt', '%', 'x^2')
        self.const = 0
        self.bg_color = bg_color

        self.left_frame = Frame(self, style='l.TFrame')
        self.left_frame.place(relx=0, relwidth=0.75, relheight=1)
        self.left_frame.bind("<Configure>", self.ev_resize)

        self.right_frame = Frame(self, style='r.TFrame')
        self.right_frame.place(relx=0.75, relwidth=0.25, relheight=1)

        self.creat_history()
        self.creat_label()
        self.creat_button()

    def creat_button(self):
        Button(self.left_frame, style='sub.TButton', text='MC', command=lambda: self.on_button_click('MC')).place(
            relheight=0.05, relwidth=0.15, relx=0, rely=0.2)
        Button(self.left_frame, style='sub.TButton', text='MR', command=lambda: self.on_button_click('MR')).place(
            relheight=0.05, relwidth=0.15, relx=0.15, rely=0.2)
        Button(self.left_frame, style='sub.TButton', text='M+', command=lambda: self.on_button_click('M+')).place(
            relheight=0.05, relwidth=0.15, relx=0.3, rely=0.2)
        Button(self.left_frame, style='sub.TButton', text='M-', command=lambda: self.on_button_click('M-')).place(
            relheight=0.05, relwidth=0.15, relx=0.45, rely=0.2)
        Button(self.left_frame, style='sub.TButton', text='MS', command=lambda: self.on_button_click('MS')).place(
            relheight=0.05, relwidth=0.15, relx=0.6, rely=0.2)

        Button(self.left_frame, style='b.TButton', text='%', command=lambda: self.on_button_click('%')).place(
            relheight=0.125, relwidth=0.25, relx=0, rely=0.25)
        Button(self.left_frame, style='b.TButton', text='CE', command=lambda: self.on_button_click('CE')).place(
            relheight=0.125, relwidth=0.25, relx=0.25, rely=0.25)
        Button(self.left_frame, style='b.TButton', text='C', command=lambda: self.on_button_click('C')).place(
            relheight=0.125, relwidth=0.25, relx=0.5, rely=0.25)
        Button(self.left_frame, style='b.TButton', text='DEL', command=lambda: self.on_button_click('DEL')).place(
            relheight=0.125, relwidth=0.25, relx=0.75, rely=0.25)

        Button(self.left_frame, style='b.TButton', text='1/x', command=lambda: self.on_button_click('1/x')).place(
            relheight=0.125, relwidth=0.25, relx=0, rely=0.375)
        Button(self.left_frame, style='b.TButton', text='x^2', command=lambda: self.on_button_click('x^2')).place(
            relheight=0.125, relwidth=0.25, relx=0.25, rely=0.375)
        Button(self.left_frame, style='b.TButton', text='sqrt', command=lambda: self.on_button_click('sqrt')).place(
            relheight=0.125, relwidth=0.25, relx=0.5, rely=0.375)
        Button(self.left_frame, style='b.TButton', text='/', command=lambda: self.on_button_click('/')).place(
            relheight=0.125, relwidth=0.25, relx=0.75, rely=0.375)

        Button(self.left_frame, style='b.TButton', text='7', command=lambda: self.on_button_click('7')).place(
            relheight=0.125, relwidth=0.25, relx=0, rely=0.5)
        Button(self.left_frame, style='b.TButton', text='8', command=lambda: self.on_button_click('8')).place(
            relheight=0.125, relwidth=0.25, relx=0.25, rely=0.5)
        Button(self.left_frame, style='b.TButton', text='9', command=lambda: self.on_button_click('9')).place(
            relheight=0.125, relwidth=0.25, relx=0.5, rely=0.5)
        Button(self.left_frame, style='b.TButton', text='*', command=lambda: self.on_button_click('*')).place(
            relheight=0.125, relwidth=0.25, relx=0.75, rely=0.5)

        Button(self.left_frame, style='b.TButton', text='4', command=lambda: self.on_button_click('4')).place(
            relheight=0.125, relwidth=0.25, relx=0, rely=0.625)
        Button(self.left_frame, style='b.TButton', text='5', command=lambda: self.on_button_click('5')).place(
            relheight=0.125, relwidth=0.25, relx=0.25, rely=0.625)
        Button(self.left_frame, style='b.TButton', text='6', command=lambda: self.on_button_click('6')).place(
            relheight=0.125, relwidth=0.25, relx=0.5, rely=0.625)
        Button(self.left_frame, style='b.TButton', text='-', command=lambda: self.on_button_click('-')).place(
            relheight=0.125, relwidth=0.25, relx=0.75, rely=0.625)

        Button(self.left_frame, style='b.TButton', text='1', command=lambda: self.on_button_click('1')).place(
            relheight=0.125, relwidth=0.25, relx=0, rely=0.75)
        Button(self.left_frame, style='b.TButton', text='2', command=lambda: self.on_button_click('2')).place(
            relheight=0.125, relwidth=0.25, relx=0.25, rely=0.75)
        Button(self.left_frame, style='b.TButton', text='3', command=lambda: self.on_button_click('3')).place(
            relheight=0.125, relwidth=0.25, relx=0.5, rely=0.75)
        Button(self.left_frame, style='b.TButton', text='+', command=lambda: self.on_button_click('+')).place(
            relheight=0.125, relwidth=0.25, relx=0.75, rely=0.75)

        Button(self.left_frame, style='b.TButton', text='+/-', command=lambda: self.on_button_click('+/-')).place(
            relheight=0.125, relwidth=0.25, relx=0, rely=0.875)
        Button(self.left_frame, style='b.TButton', text='0', command=lambda: self.on_button_click('0')).place(
            relheight=0.125, relwidth=0.25, relx=0.25, rely=0.875)
        Button(self.left_frame, style='b.TButton', text='.', command=lambda: self.on_button_click('.')).place(
            relheight=0.125, relwidth=0.25, relx=0.5, rely=0.875)
        Button(self.left_frame, style='b.TButton', text='=', command=lambda: self.on_button_click('=')).place(
            relheight=0.125, relwidth=0.25, relx=0.75, rely=0.875)

    def creat_label(self):
        self.lb1 = Label(self.left_frame, text='0', style='lb1.TLabel',
                         font='hack 20', foreground='white')
        self.lb1.place(relx=1, anchor=NE, rely=.005)
        self.lb2 = Label(self.left_frame, text='0', style='lb2.TLabel',
                         font='hack 30', foreground='white')
        self.lb2.place(relx=1, anchor=NE, rely=.1)

    def ev_resize(self, event):  # event
        i, j = 0, 0
        if self.winfo_width() > self.winfo_screenwidth() * 0.45:
            self.left_frame.place(relwidth=0.75, relheight=1)
            self.right_frame.place(relx=0.75, relwidth=0.25, relheight=1)
            i, j = 1, 1
        else:

            self.left_frame.place(relwidth=1, relheight=1)
            self.right_frame.place(relwidth=0, relheight=0)
            i, j = 0, 0
        self.lbx.place(x=0, relwidth=i, relheight=j)

    def creat_history(self):
        self.lbx = Listbox(self.right_frame,
                           font='arial 20',
                           background=self.bg_color,
                           foreground='white')
        self.lbx.place(relx=0, relwidth=1, relheight=1)

    def sub_calc(self,x):
        pass

    def check(self, x):
        if x[0] == '0' or x[0] in self.exp or x[0] in self.math:
            if x[1] != '.':
                self.grep_str = ""
        else:
            self.grep_str += x

    def on_button_click(self, button_text):
        print(button_text, self.grep_str, self.expression)
        try:
            if button_text in self.num:
                self.check(button_text)
                if self.expression[1] == "":
                    self.expression[0] = self.grep_str
                else:
                    self.expression[2] = self.grep_str
            if button_text == '.':
                if self.expression[0] != '':
                    if self.expression[0][-1] == '.':
                        self.expression[0] = self.expression[0][:-1]
                    elif '.' not in self.expression[0]:
                        self.expression[0] += '.'
                elif self.expression[2] != '':
                    if self.expression[2][-1] == '.':
                        self.expression[2] = self.expression[2][:-1]
                    elif '.' not in self.expression[2]:
                        self.expression[2] += '.'
            if button_text in self.exp:
                self.grep_str = ''
                self.expression[1] = button_text

            if button_text in self.math:
                if self.expression[2] == '':
                    k = float(self.expression[0])
                    if button_text == '1/x':
                        self.expression[0] = str(1 / k)
                        pass
                    elif button_text == '%':
                        self.expression[0] = str(k / 100)
                        pass
                    elif button_text == 'x^2':
                        self.expression[0] = str(k * k)
                        pass
                    elif button_text == 'sqrt':
                        self.expression[0] = str(k**0.5)

                else:
                    k = float(self.expression[0])
                    if button_text == '1/x':
                        self.expression[2] = str(1 / k)
                        pass
                    elif button_text == '%':
                        self.expression[2] = str(k / 100)
                        pass
                    elif button_text == 'x^2':
                        self.expression[2] = str(k * k)
                        pass
                    elif button_text == 'sqrt':
                        self.expression[2] = str(k**0.5)

            if button_text == 'C':
                self.lb1.config(text=0)
                self.lb2.config(text=0)
                self.lbx.delete(0, 'end')
                self.grep_str = ''
                self.expression = ['', '', '']

            if button_text == 'CE':
                self.grep_str = ''
            if button_text == 'DEL':
                self.grep_str = self.grep_str[:-1]
                if self.expression[2] != '':
                    self.expression[2] = self.grep_str
                if self.expression[2] == '':
                    if self.expression[1] != '':
                        self.expression[1] = self.grep_str
                    else:
                        if self.expression[0] != '':
                            self.expression[0] = self.grep_str
                # if len(self.expression) > 0:
                #     if self.grep_str == '':
                #         self.expression = ['','','']
            if self.expression[1] == "":
                self.lb2.config(text=''.join(self.expression))
                if button_text == '=':
                    self.lb1.config(text=''.join(self.expression))
                    self.expression = [self.expression[0], '', '']

            else:
                self.lb1.config(text=''.join(self.expression))
                if button_text == '=':
                    ans = str(eval(''.join(self.expression)))
                    self.lb2.config(text=ans)
                    self.lbx.insert(END, f'{"".join(self.expression)}')
                    self.lbx.insert(END, f'={ans}')
                    self.expression = [ans, '', '']
                    self.grep_str = ''
        except:
            self.lb2.config(text='ERROR')

    def update_display(self, expression):
        if '=' in self.temp[0][-1]:
            self.lb1.config(text=self.expression)
            self.lb2.config(text=expression)


class Date_calc(Frame):
    def __init__(self, parent, bg_color):
        super().__init__(parent)

        Label(self, text='Here').place(relx=0.5, rely=0.5)

        pass


if __name__ == '__main__':
    app = App()
    app.start()
