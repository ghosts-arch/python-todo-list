from model import Session, Task
from sqlalchemy import select, delete


class Controller:
    def __init__(self, view):
        self.view = view
        self.view.create_new_task_button.config(command=self.create_task)
        self.view.tasks_treeview.bind("<Double-1>", self.on_click)
        self.view.delete_task_button.config(command=self.delete_task)

    def on_click(self, event):
        item = self.view.tasks_treeview.identify("item", event.x, event.y)
        task_id = int(self.view.tasks_treeview.item(item, "text"))
        with Session() as session:
            statement = select(Task).where(Task.id == task_id)
            task = session.scalars(statement).first()
            if not task.is_completed:
                tags = ("completed",)
                task.is_completed = True

            else:
                tags = ()
                task.is_completed = False
        session.add(task)
        self.view.tasks_treeview.item(item, tags=tags)
        session.commit()

    def delete_task(self):
        item = self.view.tasks_treeview.selection()
        task_id = int(self.view.tasks_treeview.item(item, "text"))
        with Session() as session:
            try:
                statement = delete(Task).where(Task.id == task_id)
                session.execute(statement)
                session.commit()
            except:
                self.view.show_error("Erreur lors de la suppression")
                return
        self.view.tasks_treeview.delete(item)

    def create_task(self):
        new_task_label = self.view.new_task_entry.get()
        if new_task_label == "":
            self.view.show_error("La tâche ne peut être vide")
            return
        with Session() as session:
            new_task = Task(label=new_task_label)
            session.add(new_task)
            session.commit()
            task_id = new_task.id
        self.view.create_task(
            text=new_task_label, task_id=task_id, is_completed=False
        )
        self.view.clear_new_task_entry()

    def get_all_tasks(self):
        with Session() as session:
            statement = select(Task)
            tasks = session.scalars(statement).all()
        return tasks
