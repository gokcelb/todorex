# todorex

Todorex is a command line application to manage todos.

If you want to learn how this works you can check the command below in your terminal.

```bash
$ python ./main.py help
```

The output will look like the following.

```bash
$ python ./main.py help
# COMMAND                                           DESCRIPTION
# add <text> due <yyyy-mm-dd>                       Adds new to do, if no date is given date is equaled to none.
# display                                           Displays to dos.
# display-with-id                                   Displays to dos with ids.
# delete <id>                                       Deletes to do based on id.
# done <id>                                         Marks to do done based on id.
# undone <id>                                       Marks to do undone based on id.
# edit <id> text <text> due <yyyy-mm-dd>            Edits to do based on id, either to do text or date or both can be edited.
# help                                              Displays commands and descriptiosn on screen.
```

## Quick Tour of todorex

1. Add a new todo
2. Add another todo
3. List todos
4. Edit one of the todos
5. List todos again

```bash
# First go to the project directory
# cd <project-directory>

$ python ./main.py add 'Check todorex application'
# New to do created.

$ python ./main.py add 'Try to contribute to todorex application'
# New to do created.

$ python ./main.py display-with-id
# TO DO IDS
# 2d037fe33d634847a0575b2757553b9f :   Check todorex application | 2021-09-11
# 28d31e857aef48f68545c97f3feaa51a :   Try to contribute to todorex application | 2021-09-11

$ python ./main.py edit 2d037fe33d634847a0575b2757553b9f due 2021-9-12
# To do edited.

$ python ./main.py display
# TO DOS
#   2021-9-12 | 2021-09-11
#   Try to contribute to todorex application | 2021-09-11
# **************************************************
```
