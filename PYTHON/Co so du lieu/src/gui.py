#!usr/bin/python3
import tkinter as tk
from tkinter import Menu, PhotoImage, Toplevel, font, Listbox ,Text, StringVar
from tkinter.ttk import *
from csdl import FILE, PATH
import os
import sys
import config


class DATABASE:
    def __init__(self) -> None:
        # +=
        self.img_dir = PATH().img_dir

        self.root = tk.Tk()
        self.width = config.WIDTH
        self.height = config.HEIGHT

        self.root.geometry("1000x600")
        self.root.minsize(self.width, self.height)
        # self.root.maxsize(self.width, self.height)
        self.root.title('ZFLASH')
        self.database_icon = PhotoImage(file=self.img_dir)
        self.root.iconphoto(False, self.database_icon)

        self.root.config(background=config.FRAME_COLOR)
        self.style = Style()
        self.style.configure('TLabel', background=config.FRAME_COLOR, font='arial')
        self.style.configure('TFrame', background=config.FRAME_COLOR)
        # Load frame
        self.login_frame = LOGIN_FRAME(self.root, self.LOGIN)
        self.login_frame.pack(expand=True, fill='both')

    def LOGIN(self, username, password, key):
        # self.login_frame.pack_forget()
        login_notice = Label(
            self.login_frame, font='Arial 16', foreground='red')
        login_notice.place(relx=0.35, rely=0.75)
        self.login_frame.pack_forget()
        self.admin_frame = ADMIN_FRAME(self.root, self.show_login_frame)
        self.admin_frame.pack(expand=True, fill='both')
        # if key == 'ADM':
        #     print('Admin login')
        #     if username == 'truong van dai' and password == 'dai@2005':
        #         self.login_frame.pack_forget()
        #         self.admin_frame = ADMIN_FRAME(self.root, self.show_login_frame)
        #         self.admin_frame.pack(expand=True, fill='both')
        #     else:
        #         login_notice.configure(text='Username or password incorrect !')
        if key == 'TER-1988-03-28':
            print('Subadmin login')
            if username == 'nguyen van dung' and password == 'dung@1988':
                self.login_frame.pack_forget()
                self.user_frame = USER_FRAME(self.root, self.show_login_frame)
                self.user_frame.pack(expand=True, fill='both')
            else:
                login_notice.configure(text='Username or password incorrect !')
        else:
            print('Student login')
        pass

    def show_login_frame(self):
        # Quay lại trang login
        if hasattr(self, 'admin_frame'):
            self.admin_frame.pack_forget()
        if hasattr(self, 'user_frame'):
            self.user_frame.pack_forget()
        self.login_frame.pack(expand=True, fill='both')

        # reset tittle
        self.root.title('ZFLASH')

        # Turn off menu bar
        menu_bar = Menu(self.root)
        self.root.configure(menu=menu_bar)

    def START(self):
        self.root.mainloop()


class LOGIN_FRAME(Frame):
    def __init__(self, parent, login_callback) -> None:
        super().__init__(parent)
        self.width = 1000
        self.height = 600
        print()

        # Label(self, text='DATABASE', font='Arial 100').pack(side='top', anchor='center',)
        self.marquee = MARQUEE(parent=self, text="ZFLASH DATABASE",font="Arial 100")
        self.marquee.pack(side="top", fill="x")
        # Username
        Label(self, text='Username').place(
            relx=0.35, rely=0.45)
        self.username = Entry(self, width=30)
        self.username.place(relx=0.45, rely=0.45)

        # Password
        self.hide_status = True
        Label(self, text='Password').place(
            relx=0.35, rely=0.55)
        self.password = Entry(self, show="*", width=30)
        self.password.place(relx=0.45, rely=0.55)
        self.hide_pass_btn = Button(self, text='Unhide', command=self.HIDEPASS)
        self.hide_pass_btn.place(relx=0.65, rely=0.55)

        # Key lisence - STT : student, TER-[year] : teacher ,ADM-[year] : adminirator
        Label(self, text='Key').place(relx=0.35, rely=0.65)
        self.key = Entry(self, show="*", width=30)
        self.key.place(relx=0.45, rely=0.65)

        Button(self, text='Ok', command=lambda: login_callback(self.username.get(), self.password.get(), self.key.get())).place(
            relx=0.65, rely=0.75)
        Button(self, text='Cancel', command=parent.destroy).place(
            relx=0.75, rely=0.75)

    # def get_key(self):
    #     return self.username.get(), self.password.get(), self.key.get()

    def HIDEPASS(self):
        if self.hide_status:
            self.hide_pass_btn.config(text='Hide')
            self.password.config(show='')
            self.key.config(show='')
        else:
            self.hide_pass_btn.config(text='UnHide')
            self.password.config(show='*')
            self.key.config(show='*')
        self.hide_status = not self.hide_status


class USER_FRAME(Frame):
    def __init__(self, parent, show_login_frame) -> None:
        super().__init__(parent)
        MENU(parent=parent)
        Label(self, text='User home', font='Arial 30').pack(
            anchor='center', side='top')
        Button(self, text='Back home', command=show_login_frame).place(x=1, y=1)


class ADMIN_FRAME(Frame):
    def __init__(self, parent, show_login_frame) -> None:
        super().__init__(parent)
        MENU(parent=parent)
        self.parent = parent
        parent.title('ADMIN')
        self.parent.bind("<Configure>", self.events_resize)
        self.width = self.parent.winfo_width()
        self.height = self.parent.winfo_height()
        self.index = 0
        self.login = True
        
        self.s_heading = ('ID','NAME','DATE','GENDER','CLASS')
        self.s_ratio = (0.09,0.16,0.1,0.04,0.08)
        self.t_heading = ('ID','NAME','DATE','GENDER','SUBJECT','PHONE')
        self.t_ratio = (0.025,0.12,0.06,0.03,0.06,0.06)
        
        file = FILE()
        file.IMPORT('A')
        self.s_data = file.student_data
        self.t_data = file.teacher_data

        # Label(self, text='Admin home', font='Arial 30').pack(anchor='center',side='top')
        # Button(self, text='Back home', command=show_login_frame).pack(side='bottom', anchor='sw')
        self.btn_gv = Button(self,text='Quan ly giao vien,nhan su', command=self.teacher_manager)
        self.btn_gv.place(relx=0,rely=0.1)
        self.btn_sv = Button(self,text='Quan ly hoc sinh,sinh vien',command=self.student_manager)
        self.btn_sv.place(relx=0,rely=0.2)

        # self.INFO()
        # self.TABLE()
    def teacher_manager(self):
        self.btn_gv.destroy()
        self.INFO()
        self.TABLE(self.t_heading,self.t_data,self.t_ratio)
    def student_manager(self):
        self.login = False
        self.btn_sv.destroy()
        self.INFO()
        self.TABLE(self.s_heading,self.s_data,self.s_ratio)


    def TABLE(self, heading: tuple, data: list, ratio: tuple):
        self.table_frame = Frame(self)
        self.table_frame.place(relx=0.5,rely=0,relwidth=0.5,relheight=1)

        # Creat treeview
        self.table = Treeview(self.table_frame,show='tree headings',height=int(self.height*0.0485))
        # self.table.bind("<<TreeviewSelect>>",self.events_treeview)
        # Define column
        self.table['column'] = heading
        
        # Creat column
        self.table.column("#0", width=0, stretch=tk.NO) #hinden column
        self.table.heading('#0',text='')

        # Define heading
        for i in range(len(heading)):
            items = heading[i]
            self.table.column(items,width=int(self.width*ratio[i]),anchor='center',stretch=True)
            self.table.heading(items,text=items)

        # Insert data
        # self.table.insert('','end',values=('1','Dai','12/03/2005','NAM','9A1'))
        for items in data:
            items = tuple(i.upper() for i in items)
            self.table.insert('','end',values=items)

        # add scrollbar in table
        scrollbar = Scrollbar(self.table_frame, orient='vertical', command=self.table.yview)
        scrollbar.pack(side='right', fill='y',expand=False)
        self.table.configure(yscrollcommand=scrollbar.set)
        self.table.pack(side='left',fill='both',expand=True)
    
    def events_resize(self, event):
        if self.width != self.parent.winfo_width() or self.height != self.parent.winfo_height():
            if self.width != self.parent.winfo_width():
                self.width = self.parent.winfo_width()
            if self.height != self.parent.winfo_height():
                self.height = self.parent.winfo_height()
            self.table_frame.destroy()
            if self.login:
                self.TABLE(self.t_heading,self.t_data,self.t_ratio)
            else:
                self.TABLE(self.s_heading,self.s_data,self.s_ratio)
    def events_treeview(self,event):
        self.index = self.table.index(self.table.selection()[0])
        self.fill(self.index)

    def INFO(self):
        self.info_frame = Frame(self)
        self.info_frame.place(relx=0,rely=0,relwidth=0.5,relheight=1)
        # Label(self.info_frame,text='Thong tin hoc sinh',font='Arial 45').pack(anchor='center',side='top')
        MARQUEE(self.info_frame,text='Thong tin hoc sinh',font="Arial 45").pack(fill='x',side='top')

        Label(self.info_frame,text='ID').place(relx=0.05,rely=0.25)
        self.id = Entry(self.info_frame)
        self.id.place(relx=0.15,rely=0.25)

        Label(self.info_frame,text="Ho").place(relx=0.05,rely=0.35)
        self.surname = Entry(self.info_frame)
        self.surname.place(relx=0.15,rely=0.35)

        Label(self.info_frame,text="Ten").place(relx=0.55,rely=0.35)
        self.name = Entry(self.info_frame)
        self.name.place(relx=0.65,rely=0.35)

        Label(self.info_frame,text="Date").place(relx=0.05,rely=0.45)
        self.date = Entry(self.info_frame)
        self.date.place(relx=0.15,rely=0.45)

        Label(self.info_frame,text="Gioi tinh").place(relx=0.5,rely=0.45)
        self.gender = Entry(self.info_frame)
        self.gender.place(relx=0.65,rely=0.45)

        Label(self.info_frame,text="Lop").place(relx=0.05,rely=0.55)
        self.classes = Entry(self.info_frame)
        self.classes.place(relx=0.15,rely=0.55)

        self.fill_set = (self.id,self.surname,self.name,self.date,self.gender,self.classes)

        Button(self.info_frame,text='>>',command=self.next).place(relx=0.55,rely=0.65)
        Button(self.info_frame,text='<<',command=self.prev).place(relx=0.25,rely=0.65)
        self.next()
    
    def next(self):
        if self.index < len(self.s_data):
            # += \n
            self.fill(index=self.index)
            self.index += 1

    def prev(self):
        if self.index > -1:
            # += \n
            self.fill(index=self.index)
            self.index -= 1
    def fill(self,index: int):
        data = self.s_data[self.index]
        temp = self.s_data[self.index][1].split(" ")
        data = data[:1] + [" ".join(temp[:2]),temp[2]] + data[2:] 
        for i in range(len(data)):
            self.fill_set[i].config(state='normal')
            self.fill_set[i].delete(0,'end')
            self.fill_set[i].insert(0,data[i].upper())
            # self.fill_set[i].config(state='readonly')







class MENU:
    def __init__(self, parent):
        self.parent = parent
        menu_bar = Menu(parent)

        home = Menu(menu_bar, tearoff=0)
        home.add_command(label='New (Ctrl N)', command=lambda: NEW_DATABASE(parent=parent))
        home.add_command(label='Open (Ctrl O)')
        home.add_command(label='Save (Ctrl S)')
        home.add_command(label='Export (Ctrl E)')
        menu_bar.add_cascade(label='Home', menu=home)

        tool = Menu(menu_bar, tearoff=0)
        tool.add_command(label='Sort by')
        tool.add_command(label='Filter')
        tool.add_command(label='Find')
        tool.add_command(label='Replace')
        menu_bar.add_cascade(label='Tool', menu=tool)

        view = Menu(menu_bar, tearoff=0)
        view.add_command(label='Chart')
        view.add_command(label='Rank')
        view.add_command(label='Point')
        menu_bar.add_cascade(label='View', menu=view)

        option = Menu(menu_bar, tearoff=0)
        option.add_command(label='Apperament', command=self.apperament)
        option.add_command(label='Help')
        option.add_command(label='Document')
        menu_bar.add_cascade(label='Option', menu=option)
        parent.config(menu=menu_bar)

    def apperament(self):
        theme = APPERAMENT()
        theme.start()

    def OPEN_FILE(self):
        pass


class NEW_DATABASE(Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        


        pass


class APPERAMENT:
    def __init__(self):
        super().__init__()
        self.theme = Toplevel()
        self.theme.geometry('600x400')
        self.theme.title('Apperament')
        self.theme_icon = PhotoImage(file=PATH().img_dir)
        self.theme.iconphoto(False, self.theme_icon)
        self.theme.configure(bg='lightblue')

        # [background color, text color]
        self.theme_set = {'Dark' : ['#1A1A19','#F6FCDF'],
                          'White' : ['#CBDCEB','#030303'],
                          'Vintage' : ['#808000','#1A1A19'],
                          'Material' : ['#6200EA','#FFFFFF'],
                          'Nord' : ['#3B4252','#ECEFF4']}
        self.font_set = [i for i in font.families()]
        self.text_displayed = '“The biggest adventure you can take is to live the life of your dreams.”'
        self.font_style = 'Arial'
        self.text_color = ''
        self._size = 12

        self.theme_selected = StringVar()
        self.font_selected = StringVar()
        self.size_selected = StringVar()

        self.frame_left = Frame(self.theme)
        self.frame_left.place(relwidth=0.65, relheight=1)
        
        self.frame_right = Frame(self.theme)
        self.frame_right.place(relx=0.65, relwidth=.35, relheight=1)
        
        self.labelframefont = LabelFrame(self.frame_left, text='Font setting')
        self.labelframefont.place(relx=0, rely=0, relwidth=1, relheight=0.55)
        
        self.labelframetheme = LabelFrame(self.frame_left, text='Color setting')
        self.labelframetheme.place(relx=0, rely=0.55, relwidth=1, relheight=0.45)
        
        self.labelframedebug = LabelFrame(self.frame_right, text='DEBUG')
        self.labelframedebug.place(relwidth=1, relheight=1)
        
        self.debug_event = Listbox(self.labelframedebug, background='lightgreen', font='hack 9', activestyle='none')
        self.debug_event.place(relwidth=1, relheight=1)

    def gui_setting_font(self):
        # Font setting
        Label(self.labelframefont, text='Font').place(relx=0, rely=0.5)
        self.combobox_font = Combobox(self.labelframefont, width=20, height=10, font='arial 10',
                                 textvariable=self.font_selected, values=self.font_set)
        self.combobox_font.place(relx=0.3, rely=0.5)
        
        # Size setting
        Label(self.labelframefont, text='Font size').place(relx=0, rely=0.65)
        self.combobox_size = Combobox(self.labelframefont, width=5, height=10, font='arial 10',
                                 textvariable=self.size_selected, values=[str(i) for i in range(9, 31)])
        self.combobox_size.place(relx=0.3, rely=.65)

        self.combobox_font.current(1)
        self.combobox_size.current(9)

        self.text = Text(self.labelframefont, width=300, height=400, selectbackground='blue', border=10)
        self.text.insert('end', self.text_displayed)
        self.text.place(relx=0, relwidth=1, relheight=.45)

        #Get event when user change action on widget
        self.combobox_font.bind('<<ComboboxSelected>>', self.on_select_font)
        self.combobox_size.bind('<<ComboboxSelected>>', self.on_select_size)

    def on_select_font(self, event):
        self.font_style = event.widget.get()
        self.text.configure(font=(self.font_style, self._size))
        self.debug_event.insert(0, f"[DEBUG] Font: {self.font_style}, Size: {self._size}")
        # print(f"[DEBUG] Font: {self.font_style}, Size: {self._size}")

    def on_select_size(self, event):
        self._size = event.widget.get()
        self.text.configure(font=(self.font_style, self._size))
        self.debug_event.insert(0, f"[DEBUG] Font: {self.font_style}, Size: {self._size}")
        # print(f"[DEBUG] Font: {self.font_style}, Size: {self._size}")
    
    # Theme setting

    def gui_setting_theme(self):
        Label(self.labelframetheme, text='Style theme').place(relx=0, rely=0)

        self.combobox_theme = Combobox(self.labelframetheme, width=20, height=10, font='arial 10',
                                 textvariable=self.theme_selected, values=list(self.theme_set.keys()))
        self.combobox_theme.place(relx=0.3, rely=0)
        self.combobox_theme.current(1)
        #Get event when user change action on widget
        self.combobox_theme.bind('<<ComboboxSelected>>', self.on_select_theme)

        #Button
        Button(self.labelframetheme, text='Cancel', command=self.cancel).place(
            relx=0.45, rely=0.75, relwidth=0.25)
        Button(self.labelframetheme, text='Save',
               command=self.save).place(relx=0.75, rely=0.75)


    def on_select_theme(self, event):
        self.selected_theme = event.widget.get()
        self.text.configure(background=self.theme_set[self.selected_theme][0],
                            foreground=self.theme_set[self.selected_theme][1])
        config.FRAME_COLOR = self.theme_set[self.selected_theme][0]
        self.debug_event.insert(0, f"[DEBUG] Theme: {self.selected_theme}")
        print(f"[DEBUG] Theme: {self.selected_theme}")

    def save(self) -> None:
        self.theme.destroy()

    def cancel(self) -> None:
        self.theme.destroy()

    def start(self):
        self.gui_setting_font()
        self.gui_setting_theme()
        self.theme.mainloop()


class MARQUEE(tk.Canvas):
    def __init__(self, parent, text, font, margin=5, borderwidth=10, fps=45):
        super().__init__(parent, borderwidth=borderwidth
            , relief='groove',background=config.BANNER_COLOR)

        self.fps = fps
        
        # start by drawing the text off screen, then asking the canvas
        # how much space we need. Use that to compute the initial size
        # of the canvas. 
        text = self.create_text(0, -1000, text=text, anchor="w", tags=("text",), font=font)
        (x0, y0, x1, y1) = self.bbox("text")
        width = (x1 - x0) + (2*margin) + (2*borderwidth)
        height = (y1 - y0) + (2*margin) + (2*borderwidth)
        self.configure(width=width, height=height)

        # start the animation
        self.animate()

    def animate(self):
        (x0, y0, x1, y1) = self.bbox("text")
        if x1 < 0 or y0 < 0:
            # everything is off the screen; reset the X
            # to be just past the right margin
            x0 = self.winfo_width()
            y0 = int(self.winfo_height()/2)
            self.coords("text", x0, y0)
        else:
            self.move("text", -1, 0)

        # do again in a few milliseconds
        self.after_id = self.after(int(1000/self.fps), self.animate)


class CONFIG_GUI:
    def __init__(self, parent) -> None:
        self.parent = parenty
        self.config_file = os.path.join(PATH().src_dir,'config.p') 
        # Mở file và đọc nội dung
        with open(self.config_file, 'r') as file:
            lines = file.readlines()

        # Thay đổi dòng có chứa COLOR = 'RED'
        for i, line in enumerate(lines):
            if "COLOR = 'RED'" in line.strip():  # Sử dụng strip() để bỏ qua khoảng trắng
                lines[i] = "COLOR = 'BLUE'\n"  # Thay đổi dòng

        # Ghi lại các dòng đã thay đổi vào file
        with open(self.config_file, 'w') as file:
            file.writelines(lines)

# file = FILE()
# file.IMPORT('A')
# print(file.student_data)

if __name__ == '__main__':
    database = DATABASE()
    database.START()
    pass


def promt_lock_database():
    print(' '*30, '[DATABASE - unlock gui]')
    while True:
        username = input('User name : ')
        password = input('Password  : ')
        if username == '' and password == '':
            print('Login start ...')
            if __name__ == '__main__':
                database = DATABASE()
                database.START()
            print('Exit !')
            break
        else:
            print('Username or password incorrect !')

# promt_lock_database()
