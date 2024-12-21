from controller import Controller
from tkinter import Entry, Button, BooleanVar, Checkbutton, Label, END, Frame
from tkinter.messagebox import showerror
from tkinter.ttk import Treeview


class View:
    def __init__(self, root):
        self.root = root
        self.root.rowconfigure(3, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.create_widgets()

        self.controller = Controller(self)
        tasks = self.controller.get_all_tasks()
        for task in tasks:
            self.create_task(
                task_id=task.id,
                text=task.label,
                is_completed=task.is_completed,
            )

    def create_widgets(self):
        main_menu_label = Label(
            self.root,
            text="My Todo List",
            font=("Helvetica", 20, "bold"),
            background="#DCE9F2",
            foreground="#2C3E50",
        )
        main_menu_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))
        add_new_task_frame = Frame(self.root, background="#DCE9F2")
        add_new_task_frame.grid(
            row=1, column=0, sticky="ew", padx=(10, 10), pady=(10, 10)
        )
        add_new_task_frame.columnconfigure(0, weight=1)
        add_new_task_frame.columnconfigure(1, weight=1)
        self.new_task_entry = Entry(
            add_new_task_frame, width=64, font=("Helvetica", 12), relief="flat"
        )
        self.new_task_entry.grid(
            row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="ens"
        )

        self.create_new_task_button = Button(
            add_new_task_frame,
            text="Ajouter",
            font=("Helvetica", 12),
            relief="flat",
            background="#28A745",
            foreground="white",
        )
        self.create_new_task_button.grid(
            row=0, column=1, padx=(10, 10), pady=(5, 5), sticky="wns"
        )
        menus_frame = Frame(self.root, background="#DCE9F2")
        menus_frame.grid(
            row=2, column=0, sticky="e", padx=(10, 10), pady=(10, 10)
        )
        self.delete_task_button = Button(
            menus_frame,
            text="Supprimer",
            font=("Helvetica", 12),
            relief="flat",
            background="#DC3545",
            fg="white",
        )
        self.delete_task_button.grid(
            row=0, column=0, padx=(10, 10), pady=(5, 5)
        )
        self.tasks_treeview = Treeview(self.root)
        self.tasks_treeview["columns"] = ("label",)
        self.tasks_treeview.column("#0", width=50, stretch=False)
        self.tasks_treeview.column("label", width=100)
        self.tasks_treeview.heading("#0", text="id", anchor="center")
        self.tasks_treeview.heading("label", text="Tache", anchor="center")
        self.tasks_treeview.grid(
            row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew"
        )
        self.tasks_treeview.tag_configure(
            "completed", background="#D5F5E3", foreground="#1D8348"
        )

    def create_task(
        self, text: str, task_id: int, is_completed: bool
    ) -> Label:
        tags = []
        if is_completed:
            tags.append("completed")
        item = self.tasks_treeview.insert(
            "", "end", text=task_id, values=(text,), tags=tags
        )
        self.tasks_treeview.tag_bind(
            item,
            "<Button-1>",
            lambda event: self.controller.on_click(event, task_id),
        )
        """new_task_label.bind(
            "<Button-1>", lambda event: self.controller.on_click(event, task_id)
        )"""
        """delete_task_button = Button(self.root, text="Supprimer")
        delete_task_button.grid(padx=24, pady=24)
        delete_task_button.config(
            command=lambda: self.controller.delete_task(
                task_id, new_task_label, delete_task_button
            )
        )"""

    def clear_new_task_entry(self):
        self.new_task_entry.delete(0, END)

    def show_error(self, message: str):
        showerror(title="Erreur", message=message)
