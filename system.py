from todo import Todo
from storage import TodoStorage

class TodoSystem:
    def __init__(self) -> None:
        self.storage = TodoStorage()
        self.todos = self.storage.read_todos()

    def add(self, todo_text, due_date):
        todo = Todo(todo_text, due_date)
        todo.determine_urgency()
        self.todos[todo.id] = todo

        self.storage.save_todos(self.todos)

        return todo

    def update(self, id: str, todo_text=None, due_date=None, done=None):
        if id not in self.todos:
            return

        todo = self.todos[id]
        if todo_text is not None:
            todo.todo_text = todo_text
        if due_date is not None:
            todo.due_date = due_date
        if done is not None:
            todo.done = done

    def mark_done(self, id: str):
        if id not in self.todos:
            return

        todo = self.todos[id]
        todo.done = True
        
    def delete(self, id):
        if id in self.todos:
            del self.todos[id]

    def display_todos(self):
        print("TO DOS")
        for todo in self.todos.values():
            if not todo.done:
                print("%s" %todo)
        print("*"*50)
        for todo in self.todos.values():
            if todo.done:
                print("%s" %todo)

    def display_with_id(self):
        print("TO DO IDS")
        for id, todo in self.todos.items():
            print("%s : %s" %(id, todo))