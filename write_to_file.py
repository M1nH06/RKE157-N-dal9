def use_write_mode(file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        pass
    #"w" kustutab algandmed ära ning valmistab faili ette uute andmete jaoks

use_write_mode("Data/todo.txt")