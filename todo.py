from datetime import date, timedelta
import uuid

class Todo:
    def __init__(self, todo_text, due_date=None, id=None) -> None:
        self.todo_text = todo_text
        self.creation_date = date.today()
        self.due_date = due_date
        if self.due_date is not None:
            self.due_date = date.fromisoformat(due_date)
        self.urgency = ""
        self.id = id
        if self.id is None:
            self.id = uuid.uuid4().hex
        self.done = False

    def determine_urgency(self):
        if self.due_date is None:
            return
            
        time_difference = self.due_date - self.creation_date
        three_days = timedelta(days=3)
        one_week = timedelta(days=7)
        three_weeks = one_week * 3
        if time_difference <= three_days:
            self.urgency = "!!!"
        elif three_days <= time_difference < one_week:
            self.urgency = "!!"
        elif one_week <= time_difference < three_weeks:
            self.urgency = "!"

    def to_file_format(self):
        return "%s,,,%s,,,%s,,,%s,,,%s,,,%s" % (
                    self.id, self.urgency, self.todo_text, self.creation_date, self.due_date, self.done)

    def __str__(self) -> str:
        if self.due_date is None:
            return "%s %s | %s" %(self.urgency, self.todo_text, self.creation_date)
        else:
            return "%s %s | %s - %s" %(self.urgency, self.todo_text, self.creation_date, self.due_date)