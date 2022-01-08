import os
import shutil


join = os.path.join
listdir = os.listdir
copyfile = shutil.copyfile

folder = join("roi", "result")
source_path = join(folder, "new-dataset", "roi")

train = 0.6
destination_folder = join(folder, "dataset_60v40")

total_files = len([name for name in os.listdir(source_path) if name != ".gitkeep"])
total_train = round(total_files * train)

# eliminate .gitkeep
files = [name for name in listdir(source_path) if name != ".gitkeep"]
for index, name in enumerate(files):
    file_path = join(source_path, name)

    if index < total_train:
        copyfile(file_path, join(destination_folder, "train", name))
    else:
        copyfile(file_path, join(destination_folder, "test", name))
