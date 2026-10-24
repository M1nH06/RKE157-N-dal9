def add_task_to_file(file_path):
    new_task = "Celebrate small wins with a cookie."
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n" + new_task)
    #"a" lisab lause faili

add_task_to_file("Data/todo.txt")