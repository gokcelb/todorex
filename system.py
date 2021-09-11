from todo import Todo
from storage import TodoStorage

class TodoSystem:
    def __init__(self) -> None:
        self.storage = TodoStorage()
        self.todos = self.storage.read_todos()

    def add(self, todo_text, due_date=None):
        todo = Todo(todo_text, due_date)
        todo.determine_urgency()
        self.todos[todo.id] = todo

        self.storage.save_todos(self.todos)

        print("New to do created.")

        return todo

    def edit(self, id: str, todo_text=None, due_date=None, done=None):
        if id not in self.todos:
            return

        todo = self.todos[id]
        if todo_text is not None:
            todo.todo_text = todo_text
        if due_date is not None:
            todo.due_date = due_date
        if done is not None:
            todo.done = done

        self.storage.save_todos(self.todos)

        print("To do edited.")

    def mark_done(self, id: str):
        if id not in self.todos:
            return

        todo = self.todos[id]
        todo.done = True

        self.storage.save_todos(self.todos)

        print("To do marked done.")

    def mark_undone(self, id: str):
        if id not in self.todos:
            return

        todo = self.todos[id]
        todo.done = False
        
        self.storage.save_todos(self.todos)

        print("To do marked undone.")
        
    def delete(self, id):
        if id not in self.todos:
            return

        del self.todos[id]
        self.storage.save_todos(self.todos)

        print("To do deleted.")

    def display_todos(self):
        BPURPLE = '\033[45m' # Purple Background

        print("TO DOS")
        for todo in self.todos.values():
            if not todo.done:
                print("%s" %todo)
        print("*"*50)
        for todo in self.todos.values():
            if todo.done:
                print(BPURPLE + "%s" %todo)

    def display_with_id(self):
        print("TO DO IDS")
        for id, todo in self.todos.items():
            print("%s : %s" %(id, todo))