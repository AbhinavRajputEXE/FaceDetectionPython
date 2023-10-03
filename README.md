# Face Detection & Image Processing Project

A comprehensive solution that integrates OpenCV functionalities, offering both face detection with Haar cascades and interactive drawing capabilities. The repository also encapsulates a warehouse parcel system management feature.

## Main Highlights

1. **Face Detection**:

   - Employs OpenCV in conjunction with Haar cascades to pinpoint faces in photos.

2. **Geometric Shape Illustration**:

   - Leverages OpenCV to sketch elementary geometric figures:
     - Lines
     - Rectangles
     - Ellipses
     - Circles

3. **Parcel System Management**:
   - Python class to oversee warehouse parcel particulars.
   - Capabilities comprise:
     - Recording parcel specifics: number, weight, category.
     - Visualization and archiving of parcel details in CSV format.

## Repository Overview

- `data`: Hosts sample imagery and associated CSV files.
- `utils`: Contains auxiliary scripts: setup and shape-rendering functions.
- `face_detection.py`: Core script for the facial detection feature.
- `warehouse.py`: Script overseeing the warehouse parcel system.

## Configuration & Deployment

**Essential Components**:

### Installations:

1. **Python**:

   - Mandatory for the execution. Obtain from [Python's home page](https://www.python.org/downloads/).

2. **OpenCV**:

   - A robust computer vision library.

3. **csv module**:
   - Incorporated in Python's core library for CSV I/O operations.

### Installation Procedures:

1. **Python Set Up**:

   - Download suitable variant from [Python's home page](https://www.python.org/downloads/).
   - Follow the installation steps. Ensure Python is added to PATH.

2. **Initiate a Virtual Environment (Suggested)**:

   - Aids in preventing package version discrepancies.

   ```bash
   python -m venv my_env
   ```

   - Activate it:
     - Windows:
     ```bash
     .\my_env\Scripts\activate
     ```
     - macOS & Linux:
     ```bash
     source my_env/bin/activate
     ```

3. **Incorporate OpenCV**:
   ```bash
   pip install opencv-python
   ```

### Project Initialization:

1. **CSV Set Up**:

   - Initialize `parcels.csv` by executing `initialize_csv.py`.

2. **Image Placement**:

   - Deposit images intended for facial detection into `images/`.

3. **Script Execution**:
   - Execute desired scripts (`face_detection.py`, `shape_drawing.py`, `warehouse.py`).

Remember to activate the virtual environment prior to executing scripts or introducing supplementary packages.

**Script Execution Guidelines**:

1. Change to project directory.
2. For facial detection, use `python face_detection.py`.
3. For shape rendering, input `python shape_drawing.py`.
4. For the warehouse system's parcel management, run `python warehouse.py`.
