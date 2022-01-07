import cv2 as cv
import os


join = os.path.join
folder = join("roi", "result")
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


dataset_folder = join(folder, "dataset")
for subfolder in os.listdir(dataset_folder):
    folder_path = join(dataset_folder, subfolder)

    for image in os.listdir(folder_path):
        with_roi_out_folder = join(folder, "with-roi", subfolder)
        cropped_roi_out_folder = join(folder, "cropped-roi", subfolder)

        add_roi(folder_path, with_roi_out_folder, image)
        crop_roi(folder_path, cropped_roi_out_folder, image)
