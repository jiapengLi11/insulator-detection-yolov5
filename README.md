# Insulator Detection with YOLOv5

This repository is a cleaned project snapshot for insulator detection based on a YOLOv5-style codebase.

It keeps the training, validation, detection, UI, and utility scripts that were actually used in the local project, while removing large weights, videos, and repeated runtime outputs that do not belong in a normal GitHub repository.

## Included

- `detect.py`: inference / detection logic
- `train.py`: training script
- `val.py`: validation script
- `ui.py`: PyQt-based demo interface
- `cfg/`, `models/`, `utils/`: model configs and supporting YOLO code
- `custom_tools/`: extra project-specific helper scripts
- `figures/`: exported training and validation result images
- `notes/detect_commented.py`: a commented learning copy of the detection script

## Not Included

The original local folder contained large or environment-specific files that are not stored in this GitHub version:

- trained weights such as `best.pt`, `last.pt`, `yolov7.pt`
- detection output videos under `runs/`
- environment tutorial videos and local setup documents
- local IDE files and caches

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

If you want to use the PyQt interface in `ui.py`, also install:

```bash
pip install PyQt5
```

## Typical Usage

Run detection:

```bash
python detect.py --weights path/to/best.pt --source path/to/image_or_video
```

Run training:

```bash
python train.py --data your_dataset.yaml --cfg cfg/training/yolov7.yaml --weights ''
```

Run validation:

```bash
python val.py --weights path/to/best.pt --data your_dataset.yaml
```

Run the UI:

```bash
python ui.py
```

## Notes

- The upstream codebase origin is a YOLO-style object detection repository, but this cleaned version is focused on the insulator-detection project itself.
- Because large `.pt` files are excluded, this repository is best treated as a code-and-results snapshot rather than a full runnable bundle.
- To reproduce inference or training, you need to provide your own weights and dataset paths locally.
