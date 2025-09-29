import tkinter as tk
from tkinter import ttk, messagebox

class ContactBook:
    def _init_(self, root):
        self.root = root
        self.root.title("📒 Contact Book")
        self.root.geometry("800x500")
        self.root.config(bg="#eaf6f6")

        # Contact storage (empty list at start)
        self.contacts = []

        # Tkinter Variables
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.search_var = tk.StringVar()

        # ------------------ Search Bar ------------------
        search_frame = tk.Frame(root, bg="#eaf6f6")
        search_frame.pack(fill=tk.X, pady=10)

        tk.Label(search_frame, text="🔍 Search:", font=("Arial", 12), bg="#eaf6f6").pack(side=tk.LEFT, padx=5)
        tk.Entry(search_frame, textvariable=self.search_var, width=40).pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Search", command=self.search_contact, bg="#0288d1", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Show All", command=self.update_table, bg="#455a64", fg="white").pack(side=tk.LEFT, padx=5)

        # ------------------ Contact Table ------------------
        self.tree = ttk.Treeview(root, columns=("Name", "Phone", "Email", "Address"), show="headings", height=10)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

        for col in ("Name", "Phone", "Email", "Address"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")

        # ------------------ Input Form ------------------
        form_frame = tk.Frame(root, bg="#eaf6f6")
        form_frame.pack(fill=tk.X, pady=10)

        tk.Label(form_frame, text="Name:", bg="#eaf6f6").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(form_frame, textvariable=self.name_var, width=25).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Phone:", bg="#eaf6f6").grid(row=0, column=2, padx=5, pady=5)
        tk.Entry(form_frame, textvariable=self.phone_var, width=25).grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Email:", bg="#eaf6f6").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(form_frame, textvariable=self.email_var, width=25).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Address:", bg="#eaf6f6").grid(row=1, column=2, padx=5, pady=5)
        tk.Entry(form_frame, textvariable=self.address_var, width=25).grid(row=1, column=3, padx=5, pady=5)

        # ------------------ Buttons ------------------
        button_frame = tk.Frame(root, bg="#eaf6f6")
        button_frame.pack(fill=tk.X, pady=10)

        tk.Button(button_frame, text="Add Contact", command=self.add_contact, bg="#4caf50", fg="white").pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Update Contact", command=self.update_contact, bg="#2196f3", fg="white").pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Delete Contact", command=self.delete_contact, bg="#f44336", fg="white").pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Exit", command=root.quit, bg="black", fg="white").pack(side=tk.RIGHT, padx=10)

        self.tree.bind("<<TreeviewSelect>>", self.load_contact)

    # ------------------ Core Functions ------------------
    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        if name and phone and email and address:
            self.contacts.append([name, phone, email, address])
            self.update_table()
            self.clear_fields()
            messagebox.showinfo("Success", "Contact Added Successfully!")
        else:
            messagebox.showerror("Error", "Please fill all fields")

    def update_table(self):
        self.tree.delete(*self.tree.get_children())
        for contact in self.contacts:
            self.tree.insert("", tk.END, values=contact)

    def load_contact(self, event):
        selected = self.tree.selection()
        if selected:
            contact = self.tree.item(selected[0], "values")
            self.name_var.set(contact[0])
            self.phone_var.set(contact[1])
            self.email_var.set(contact[2])
            self.address_var.set(contact[3])

    def update_contact(self):
        selected = self.tree.selection()
        if selected:
            idx = self.tree.index(selected[0])
            self.contacts[idx] = [self.name_var.get(), self.phone_var.get(), self.email_var.get(), self.address_var.get()]
            self.update_table()
            self.clear_fields()
            messagebox.showinfo("Updated", "Contact Updated Successfully")

    def delete_contact(self):
        selected = self.tree.selection()
        if selected:
            idx = self.tree.index(selected[0])
            del self.contacts[idx]
            self.update_table()
            self.clear_fields()
            messagebox.showinfo("Deleted", "Contact Deleted Successfully")

    def clear_fields(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set("")

    def search_contact(self):
        query = self.search_var.get().lower()
        results = [c for c in self.contacts if query in c[0].lower() or query in c[1]]
        self.tree.delete(*self.tree.get_children())
        for contact in results:
            self.tree.insert("", tk.END, values=contact)


# ------------------ Run App ------------------
if _name_ == "_main_":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()