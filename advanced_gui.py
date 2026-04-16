import tkinter as tk
from tkinter import messagebox

class AdvancedGUI:
    def __init__(self, master):
        self.master = master
        master.title("Advanced GUI App")
#
        self.label_text = tk.StringVar()
        self.label_text.set("Welcome to the Advanced GUI!")

        self.label = tk.Label(master, textvariable=self.label_text, font=("Arial", 14))
        self.label.pack(pady=20)

        self.button_click_count = 0
        self.button = tk.Button(master, text="Click Me!", command=self.on_button_click, font=("Arial", 12))
        self.button.pack(pady=10)

        self.entry_label = tk.Label(master, text="Enter your name:", font=("Arial", 12))
        self.entry_label.pack()

        self.name_entry = tk.Entry(master, width=30, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        self.submit_button = tk.Button(master, text="Submit Name", command=self.on_submit_name, font=("Arial", 12))
        self.submit_button.pack(pady=10)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit, font=("Arial", 12), bg="red", fg="white")
        self.quit_button.pack(pady=20)

    def on_button_click(self):
        self.button_click_count += 1
        self.label_text.set(f"Button clicked {self.button_click_count} times!")
        messagebox.showinfo("Button Clicked", f"You clicked the button {self.button_click_count} times!")

    def on_submit_name(self):
        name = self.name_entry.get()
        if name:
            self.label_text.set(f"Hello, {name}!")
            messagebox.showinfo("Greeting", f"Nice to meet you, {name}!")
        else:
            messagebox.showwarning("Input Error", "Please enter your name.")

if __name__ == "__main__":
    root = tk.Tk()
    my_gui = AdvancedGUI(root)
    root.mainloop()
