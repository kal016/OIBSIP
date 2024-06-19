import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import string
import pyperclip


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("400x400")

        self.create_widgets()

    def create_widgets(self):
        # Password length
        self.length_label = ttk.Label(self.root, text="Password Length:")
        self.length_label.grid(column=0, row=0, padx=10, pady=10)
        self.length_var = tk.IntVar(value=12)
        self.length_spinbox = ttk.Spinbox(self.root, from_=8, to_=64, textvariable=self.length_var, width=5)
        self.length_spinbox.grid(column=1, row=0, padx=10, pady=10)

        # Character types
        self.include_uppercase_var = tk.BooleanVar(value=True)
        self.include_uppercase_check = ttk.Checkbutton(self.root, text="Include Uppercase", variable=self.include_uppercase_var)
        self.include_uppercase_check.grid(column=0, row=1, padx=10, pady=5)

        self.include_lowercase_var = tk.BooleanVar(value=True)
        self.include_lowercase_check = ttk.Checkbutton(self.root, text="Include Lowercase", variable=self.include_lowercase_var)
        self.include_lowercase_check.grid(column=0, row=2, padx=10, pady=5)

        self.include_digits_var = tk.BooleanVar(value=True)
        self.include_digits_check = ttk.Checkbutton(self.root, text="Include Digits", variable=self.include_digits_var)
        self.include_digits_check.grid(column=0, row=3, padx=10, pady=5)

        self.include_symbols_var = tk.BooleanVar(value=True)
        self.include_symbols_check = ttk.Checkbutton(self.root, text="Include Symbols", variable=self.include_symbols_var)
        self.include_symbols_check.grid(column=0, row=4, padx=10, pady=5)

        # Custom exclusions
        self.exclude_label = ttk.Label(self.root, text="Exclude Characters:")
        self.exclude_label.grid(column=0, row=5, padx=10, pady=10)
        self.exclude_entry = ttk.Entry(self.root, width=20)
        self.exclude_entry.grid(column=1, row=5, padx=10, pady=10)

        # Complexity
        self.complexity_label = ttk.Label(self.root, text="Password Complexity:")
        self.complexity_label.grid(column=0, row=6, padx=10, pady=10)
        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Medium")  # Default value
        self.complexity_menu = ttk.OptionMenu(self.root, self.complexity_var, "Low", "Medium", "High")
        self.complexity_menu.grid(column=1, row=6, padx=10, pady=10)

        # Generate button
        self.generate_button = ttk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(column=0, row=7, columnspan=2, padx=10, pady=10)

        # Output
        self.result_label = ttk.Label(self.root, text="Generated Password:")
        self.result_label.grid(column=0, row=8, padx=10, pady=10)
        self.result_entry = ttk.Entry(self.root, width=30)
        self.result_entry.grid(column=1, row=8, padx=10, pady=10)

        # Copy button
        self.copy_button = ttk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(column=0, row=9, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        length = self.length_var.get()
        exclude_chars = self.exclude_entry.get()

        char_sets = {
            "uppercase": string.ascii_uppercase if self.include_uppercase_var.get() else "",
            "lowercase": string.ascii_lowercase if self.include_lowercase_var.get() else "",
            "digits": string.digits if self.include_digits_var.get() else "",
            "symbols": string.punctuation if self.include_symbols_var.get() else ""
        }

        # Combine selected character sets and remove excluded characters
        all_chars = "".join(char_sets.values())
        if exclude_chars:
            all_chars = "".join([ch for ch in all_chars if ch not in exclude_chars])

        if not all_chars:
            messagebox.showerror("Error", "No characters available for password generation.")
            return

        # Adjust length based on complexity
        complexity = self.complexity_var.get()
        if complexity == "Low":
            length = max(8, length)
        elif complexity == "Medium":
            length = max(12, length)
        elif complexity == "High":
            length = max(16, length)

        # Generate password
        password = ''.join(random.choice(all_chars) for _ in range(length))

        # Display password
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, password)

    def copy_to_clipboard(self):
        password = self.result_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard.")
        else:
            messagebox.showwarning("Warning", "No password to copy.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
