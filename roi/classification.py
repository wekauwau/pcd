import msvcrt
import os

join = os.path.join

root_folder = join("roi", "result")
source_path = join(root_folder, "new-dataset", "roi")


filenames = [name for name in os.listdir(source_path) if name != ".gitkeep"]
value = []

for index, name in enumerate(filenames, 1):
    print(f"{index} = (1. Lolos, 2. Tidak Lolos)")
    value.append(int(msvcrt.getch()))

print(value)
print("Salin dan tempel ke create-train-and-test.py")
