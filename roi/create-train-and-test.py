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

train = 0.6
destination_folder = join(root_folder, "dataset_60v40")

# tempel di bawah
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

for color, names in color_group.items():
    print(f"{color} = {len(names)}")
    total_train = round(train * len(names))

    for index, name in enumerate(names):
        file_path = join(source_path, name)

        if index < total_train:
            destination = "train"
        else:
            destination = "test"

        new_color = color_change[color]
        destination_path = join(destination_folder, destination, new_color, name)
        copyfile(file_path, destination_path)
