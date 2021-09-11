from system import TodoSystem
import sys

if __name__ == "__main__":
    system = TodoSystem()
    if len(sys.argv) == 5 and sys.argv[1] == 'add' and sys.argv[3] == 'due':
        system.add(sys.argv[2], sys.argv[4])
    elif len(sys.argv) == 3 and sys.argv[1] == 'add':
        system.add(sys.argv[2])
    
    if len(sys.argv) == 2 and sys.argv[1] == 'display':
        system.display_todos()

    if len(sys.argv) == 2 and sys.argv[1] == 'display-with-id':
        system.display_with_id()

    if len(sys.argv) == 3 and sys.argv[1] == 'delete':
        system.delete(sys.argv[2])

    if len(sys.argv) == 3 and sys.argv[1] == 'done':
        system.mark_done(sys.argv[2])
    
    if len(sys.argv) == 3 and sys.argv[1] == 'undone':
        system.mark_undone(sys.argv[2])

    if len(sys.argv) <= 5 and sys.argv[1] == 'edit':
        if sys.argv[3] == 'text':
            system.edit(sys.argv[2], sys.argv[4])
        elif sys.argv[3] == 'due':
            system.edit(sys.argv[2], sys.argv[4])
    elif len(sys.argv) > 5 and sys.argv[1] == 'edit' and sys.argv[3] == 'text' and sys.argv[5] == 'due':
        system.edit(sys.argv[2], sys.argv[4], sys.argv[6])

    if len(sys.argv) == 2 and sys.argv[1] == 'help':
        print("COMMAND".ljust(50), end="")
        print("DESCRIPTION")
        print('add <text> due <yyyy-mm-dd>'.ljust(50), end="")
        print("Adds new to do, if no date is given date is equaled to none.")
        print("display".ljust(50), end="")
        print("Displays to dos.")
        print("display-with-id".ljust(50), end="")
        print("Displays to dos with ids.")
        print('delete <id>'.ljust(50), end="")
        print("Deletes to do based on id.")
        print('done <id>'.ljust(50), end="")
        print("Marks to do done based on id.")
        print('undone <id>'.ljust(50), end="")
        print("Marks to do undone based on id.")
        print('edit <id> text <text> due <yyyy-mm-dd>'.ljust(50), end="")
        print("Edits to do based on id, either to do text or date or both can be edited.")
        print('help'.ljust(50), end="")
        print("Displays commands and descriptiosn on screen.")