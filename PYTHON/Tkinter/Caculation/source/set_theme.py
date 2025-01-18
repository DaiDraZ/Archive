#Font seting


from tkinter import *
from tkinter import font
from tkinter.ttk import *





class Themes:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x400')
        self.root.maxsize(800, 400)
        self.root.minsize(800, 400)
        self.root.title('Theme setting')
        self.fact = '“The biggest adventure you can take is to live the life of your dreams.”'
        self.list_font = [i for i in font.families()]
        self._theme = {
        'Aqua': ('#92cace', '#325158', '#ffffff', '#3795BD'),
        'Dark': ('#202020', '#323232', '#3B3B3B', '#ffffff'),
        'Light': ('#FFFFFF', '#EEEDEB', '#323232', 'black'),
        'Cover': ('#944527', '#c55e38', '#ebdbc9'),
        'Gradient': ('#7A1CAC', '#2E073F', '#EBD3F8', 'FFFBE6'),
        'Modern': ('#D5ED9F', '#00712D')
        }
        self.string_theme = StringVar()
        self.string_font = StringVar()
        self.string_size = StringVar()
        self._font = 'Arial'
        self._size = 12
        # creat frame
        self.frame_L = Frame(self.root)
        self.frame_L.place(relwidth=0.65, relheight=1)
        self.frame_R = Frame(self.root)
        self.frame_R.place(relx=0.65, relwidth=.35, relheight=1)
        self.labelframefont = LabelFrame(self.frame_L, text='Font setting')
        self.labelframefont.place(relx=0, rely=0, relwidth=1, relheight=0.55)
        self.labelframetheme = LabelFrame(self.frame_L, text='Color setting')
        self.labelframetheme.place(
            relx=0, rely=0.55, relwidth=1, relheight=0.45)
        self.labelframedebug = LabelFrame(self.frame_R, text='DEBUG')
        self.labelframedebug.place(relwidth=1, relheight=1)
        self.lbx_debug = Listbox(
            self.labelframedebug, background='lightgreen', font='hack 9', activestyle='none')
        self.lbx_debug.place(relwidth=1, relheight=1)

    def gui_setting_font(self):
        #================================
        Label(self.labelframefont, text='Font').place(relx=0, rely=0.5)

        self.combobox_font = Combobox(self.labelframefont, width=20, height=10, font='arial 10',
                                 textvariable=self.string_font, values=self.list_font)
        self.combobox_font.place(relx=0.3, rely=0.5)
        #================================
        Label(self.labelframefont, text='Font size').place(relx=0, rely=0.65)
        self.combobox_size = Combobox(self.labelframefont, width=5, height=10, font='arial 10',
                                 textvariable=self.string_size, values=[str(i) for i in range(5, 50)])
        self.combobox_size.place(relx=0.3, rely=.65)

        self.combobox_font.current(1)
        self.combobox_size.current(9)

        self.text = Text(self.labelframefont, width=300,
                         height=400, selectbackground='blue', border=10)
        self.text.insert(END, self.fact)
        self.text.place(relx=0, relwidth=1, relheight=.45)

        #Get event when user change action on widget
        self.combobox_font.bind('<<ComboboxSelected>>', self.on_select_font)
        self.combobox_size.bind('<<ComboboxSelected>>', self.on_select_size)

    def on_select_font(self, event):
        self._font = event.widget.get()
        self.text.configure(font=(self._font, self._size))
        self.lbx_debug.insert(
            0, f"[DEBUG] Font: {self._font}, Size: {self._size}")
        print(f"[DEBUG] Font: {self._font}, Size: {self._size}")

    def on_select_size(self, event):
        self._size = event.widget.get()
        self.text.configure(font=(self._font, self._size))
        self.lbx_debug.insert(
            0, f"[DEBUG] Font: {self._font}, Size: {self._size}")
        print(f"[DEBUG] Font: {self._font}, Size: {self._size}")
    #========================theme==================================

    def gui_setting_theme(self):
        Label(self.labelframetheme, text='Style theme').place(relx=0, rely=0)

        self.combobox_theme = Combobox(self.labelframetheme, width=20, height=10, font='arial 10',
                                 textvariable=self.string_theme, values=list(self._theme.keys()))
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
        self.text.configure(background=self._theme[self.selected_theme][0],
                            foreground=self._theme[self.selected_theme][1])
        self.lbx_debug.insert(0, f"[DEBUG] Theme: {self.selected_theme}")
        print(f"[DEBUG] Theme: {self.selected_theme}")

    def save(self) -> None:
        self.root.destroy()
        pass

    def cancel(self) -> None:
        self.root.destroy()
        pass

    def start(self):
        
        self.root.mainloop()
        return self._font, self._size






Themes().start()
