import tkinter as tk
from tkinter import messagebox

class FlatListboxMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flat Listbox Column Menu Example")

        # Button to toggle the menu visibility
        self.toggle_button = tk.Button(root, text="Toggle Menu", command=self.toggle_menu)
        self.toggle_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Frame for the menu
        self.menu_frame = tk.Frame(root, width=200, height=400)
        self.menu_frame.pack_propagate(False)  # Prevent frame from resizing to fit its contents

        # Create a Listbox with a vertical scrollbar
        self.listbox = tk.Listbox(self.menu_frame, bg='lightgrey', selectmode=tk.SINGLE,
                                 relief=tk.FLAT, bd=0, highlightthickness=0)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.menu_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Add many items to the Listbox
        for i in range(50):  # Example: Add 50 items
            self.listbox.insert(tk.END, f"Item {i + 1}")

        # Bind selection event
        self.listbox.bind('<<ListboxSelect>>', self.on_listbox_select)

        # Initially hide the menu
        self.menu_frame.pack_forget()

    def toggle_menu(self):
        if self.menu_frame.winfo_ismapped():
            self.menu_frame.pack_forget()
        else:
            self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)

    def on_listbox_select(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            selected_item = self.listbox.get(index)
            # Show a message box with the selected item
            messagebox.showinfo("Listbox Item Selected", f"You selected {selected_item}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlatListboxMenuApp(root)
    root.mainloop()
