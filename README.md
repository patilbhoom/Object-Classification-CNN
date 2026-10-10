# Object Classification using CNN

This project uses a Convolutional Neural Network (CNN) built with TensorFlow/Keras to classify images into four classes: chair, clock, fans, and speaker.

## Repository contents

- `train.py` — original model-training script.
- `test.py` — original script for running predictions on images.
- `my_model.h5` — supplied trained Keras model.
- `Dataset/train/` — training images arranged in class folders (`0`, `1`, `2`, `3`).
- `Dataset/test/` — supplied test images.
- `modelsummary.txt` — saved model summary.
- `outputvisual.png`, `outputvisual1.png` — model architecture visualizations.
- `converting.py` — original image conversion utility.
- `datasetfromgoogle.py` — original image-download utility.

## Technologies

- Python
- TensorFlow / Keras
- NumPy
- Pillow
- scikit-learn
- Matplotlib
- PyQt5 (imported by the original training script)

## Setup

Use Python in a virtual environment, then install the packages used by the original scripts:

```bash
pip install tensorflow numpy pillow scikit-learn matplotlib pyqt5 visualkeras pydot
```

Graphviz may also be required for the `plot_model` call in `train.py`.

## Dataset and labels

The training script reads images from `Dataset/train/0` through `Dataset/train/3` and maps the four output classes to chair, clock, fans, and speaker. The original script resizes images to 30×30 pixels and trains a CNN with a softmax output layer.

## Running the original scripts

Run commands from the repository root.

```bash
python train.py
```

The original training script trains for 200 epochs and saves `my_model.h5`. This can take a long time and may require a compatible TensorFlow/Python environment.

The supplied `test.py` attempts to load `my_model.h5` and classify images under a test directory. Note that the original scripts use Windows-style path separators and have inconsistent folder-name casing (`Dataset` versus `dataset`). On non-Windows systems, or when running the test script as-is, these paths may need to be adjusted. The original code is preserved and has not been silently rewritten.

## Notes

- The saved model and model summary are included as supplied.
- The original `converting.py` contains a local absolute Windows path; update those paths before using that utility on another computer.
- `datasetfromgoogle.py` is a helper script; its image-download statements are not the main training workflow.
- No accuracy metric is claimed in this README because the supplied files do not establish a verified evaluation result.
