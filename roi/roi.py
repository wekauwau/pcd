import cv2 as cv
import os


join = os.path.join
root_folder = join("roi", "result")

start_row = 176
end_row = 186
start_col = 171
end_col = 181


def get_img(in_path, filename):
    path = join(in_path, filename)
    img = cv.imread(path)
    img = cv.resize(img, (401, 401))
    return img


def save_img(img, out_path, filename):
    path = join(out_path, filename)
    cv.imwrite(path, img)


def add_roi(in_path, out_path, filename):
    img = get_img(in_path, filename)

    start_point = (start_col, start_row)
    end_point = (end_col, end_row)
    color = (64, 177, 0)  # green
    thickness = 2
    img = cv.rectangle(img, start_point, end_point, color, thickness)

    save_img(img, out_path, filename)


def crop_roi(in_path, out_path, filename):
    img = get_img(in_path, filename)
    img = img[start_row:end_row, start_col:end_col]

    save_img(img, out_path, filename)


dataset_path = join(root_folder, "dataset")
for color in os.listdir(dataset_path):
    color_folder_path = join(dataset_path, color)

    filenames = [name for name in os.listdir(color_folder_path) if name != ".gitkeep"]
    for name in filenames:
        bounding_box_path = join(root_folder, "bb", color)
        cropped_roi_path = join(root_folder, "roi", color)

        add_roi(color_folder_path, bounding_box_path, name)
        crop_roi(color_folder_path, cropped_roi_path, name)
