import os
import shutil


join = os.path.join
listdir = os.listdir

folder = join("roi", "result")
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
    dataset_path = join(folder, dataset_folder)
    new_dataset_path = join(folder, "new-dataset")
    index = 1

    for color in listdir(dataset_path):
        color_folder = join(dataset_path, color)
        new_color_name = color_name[color]

        placeholder = "{}"
        if bool(prefix_name):
            placeholder += f"_{prefix_name}"
        placeholder += f"_{new_color_name}.jpg"

        for img in listdir(color_folder):
            # ignore
            if img == ".gitkeep":
                continue

            old_file = join(color_folder, img)

            new_name = placeholder.format(str(index).zfill(2))
            new_file = join(new_dataset_path, destination_folder, new_name)
            shutil.copyfile(old_file, new_file)

            index += 1


rename("dataset", "asli")
rename("with-roi", "bb", "bb")
rename("cropped-roi", "roi", "roi")
