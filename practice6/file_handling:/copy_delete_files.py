import shutil
import os

# копирование
shutil.copy("example.txt", "copy_example.txt")

# удаление
if os.path.exists("copy_example.txt"):
    os.remove("copy_example.txt")
    