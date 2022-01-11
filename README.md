# pcd
Pengolahan Citra Digital B

Double click **workspace.code-workspace** to open VSCode workspace in the root folder. Run with python extension.

# Dependencies
Run `pip install -r requirements.txt` in terminal.

## roi.py
Copy and rename **dataset-base** to **dataset**. Add your dataset files there according to the color. Copy and rename **dataset-base** to **bb** (for original image with bounding-box) and **roi** then run.

## rename.py
Assuming you still have dataset and result files from **roi.py**. Copy and rename **new-dataset-base** to **new-dataset** then run.

## create-train-and-test.py
Run **classification.py** before run this file. Copy and rename **dataset_XvY** according to **destination_folder** (in the file) then run.
