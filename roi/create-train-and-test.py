import os
import shutil

join = os.path.join
listdir = os.listdir
copyfile = shutil.copyfile

root_folder = join("roi", "result")
source_path = join(root_folder, "new-dataset", "roi")
color_group = {
    "yellow": [],
    "maroon": [],
    "red": [],
    "orange": [],
}
color_change = {
    "yellow": "Kuning",
    "maroon": "Maroon",
    "red": "Merah",
    "orange": "Orange",
}

train = 0.8
destination_folder = join(root_folder, "dataset_80v20")

# tempel di bawah sini
classification_value = []
filenames = [name for name in os.listdir(source_path) if name != ".gitkeep"]
data_with_label = zip(filenames, classification_value)
pass_data = [data for data in data_with_label if data[1] == 1]

# group file based on color
for data in pass_data:
    name = data[0]

    for key in color_group:
        if key in name:
            color_group[key].append(name)

print("--- Data ---\n")
train_data = 0
test_data = 0

for color, names in color_group.items():
    total = len(names)
    total_train = round(train * total)

    print(f"{color} = {total}")
    print(f"train = {total_train}")
    print(f"test = {total - total_train}\n")

    name_group = {
        "train": [],
        "test": [],
    }

    for index, name in enumerate(names):
        file_path = join(source_path, name)

        if index < total_train:
            destination = "train"
            name_group["train"].append(name)
            train_data += 1
        else:
            destination = "test"
            name_group["test"].append(name)
            test_data += 1

        new_color = color_change[color]
        destination_path = join(destination_folder, destination, new_color, name)
        copyfile(file_path, destination_path)

    for key, value in name_group.items():
        print(f"-- {key} --\n")
        for name in value:
            print(name)
        print()

# remove .gitkeep files
for key, color in color_change.items():
    for folder in ["train", "test"]:
        file_path = join(destination_folder, folder, color, ".gitkeep")
        os.remove(file_path)

print("\n--- Total Data ---\n")
print(f"Train = {train_data}")
print(f"Test = {test_data}")
