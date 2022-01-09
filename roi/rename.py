import os
import shutil

import natsort


join = os.path.join

root_folder = join("roi", "result")
result_path = join(root_folder, "new-dataset")
color_name = {
    "Kuning": "front_yellow",
    "Kuning-Back": "back_yellow",
    "Maroon": "front_maroon",
    "Maroon-Back": "back_maroon",
    "Merah": "front_red",
    "Merah-Back": "back_red",
    "Orange": "front_orange",
    "Orange-Back": "back_orange",
}


def rename(dataset_folder, destination_folder, prefix_name=""):
    dataset_path = join(root_folder, dataset_folder)
    index = 1

    for color in os.listdir(dataset_path):
        color_folder = join(dataset_path, color)
        new_color = color_name[color]

        placeholder = "{}"
        if bool(prefix_name):
            placeholder += f"_{prefix_name}"
        placeholder += f"_{new_color}.jpg"

        filenames = [name for name in os.listdir(color_folder) if name != ".gitkeep"]
        # sorting like your file browser
        filenames = natsort.os_sorted(filenames)

        for name in filenames:
            old_file = join(color_folder, name)

            new_name = placeholder.format(str(index).zfill(2))
            new_file = join(result_path, destination_folder, new_name)
            shutil.copyfile(old_file, new_file)

            index += 1


rename("dataset", "original")
rename("bb", "bb", "bb")
rename("roi", "roi", "roi")
