from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Toggle Listbox")
        self.geometry("300x200")

        # Tạo một Frame chứa Listbox và Scrollbar
        self.frame = Frame(self)
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Tạo Listbox
        self.listbox = Listbox(self.frame, bg='lightgray', activestyle='none')
        self.listbox.place(relx=0, rely=0, relwidth=0.9, relheight=1)

        # Tạo Scrollbar
        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL)
        self.scrollbar.place(relx=0.9, rely=0, relwidth=0.1, relheight=1)

        # Kết nối Scrollbar với Listbox
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Thêm dữ liệu vào Listbox
        for i in range(50):
            self.listbox.insert(END, f"Item {i+1}")

        # Tạo nút để toggle Listbox
        self.toggle_button = Button(self, text="Toggle Listbox", command=self.toggle_listbox)
        self.toggle_button.place(relx=0.5, rely=0.9, anchor=CENTER)

        # Biến trạng thái để theo dõi Listbox có hiển thị hay không
        self.listbox_visible = True

    def toggle_listbox(self):
        # Nếu Listbox đang hiển thị, ẩn nó đi
        if self.listbox_visible:
            self.frame.place_forget()  # Ẩn frame chứa Listbox
        else:
            self.frame.place(relx=0, rely=0, relwidth=1, relheight=0.8)  # Hiển thị lại frame chứa Listbox

        # Cập nhật trạng thái
        self.listbox_visible = not self.listbox_visible

if __name__ == "__main__":
    app = App()
    app.mainloop()
