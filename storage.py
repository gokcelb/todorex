from todo import Todo

class TodoStorage:
    def read_todos(self):
        todos = {}
        with open("./todos.txt", "r") as file:
            file_content = file.read()
            lines = file_content.split("\n")
            for line in lines:
                if ",,," not in line:
                    continue
                id, urgency, todo_text, creation_date, due_date, done = line.split(",,,")
                t = Todo(todo_text, due_date, id=id)
                t.urgency = urgency
                t.creation_date = creation_date
                t.done = done == "True"
                todos[t.id] = t
        return todos

    def save_todos(self, todos):
        with open("./todos.txt", "w") as file:
            for todo in todos.values():
                file.write(todo.to_file_format() + "\n")