# pcd
Pengolahan Citra Digital B

Double click **workspace.code-workspace** to open VSCode workspace in the root folder.

# Dependencies
pip install -r requirements.txt

## roi.py
Copy and rename **dataset-base** to **dataset**. Add your dataset files there according to the color. Copy and rename **dataset-base** to **with-roi** (for original image with bounding-box) and **cropped-roi** then run.

## rename.py
Assuming you still have dataset and result files from **roi.py**. Copy and rename **new-dataset-base** to **new-dataset** then run.

## create-train-and-test.py
Copy and rename **dataset_XvY** according to **destination_folder** (in the file) then run.
