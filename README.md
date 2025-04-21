# Group Images

This repository loops all images JPG files in a given folder, finds how many faces the image contains and adds a FaceCount element to the metadata Comments field.

## Prerequisite

```BASH
pip install opencv-python
pip install face_recognition
pip install piexif
```

The application is using OpenCV and face-recognition (which is built on top of dlib and very accurate for face detection). 

Dlib can be tricky to install on some systems.

## Installing Dlib on Ubuntu

These are the steps to install on Ubuntu 24.04.1

### Step 1: Install OS libraries
```BASH
sudo apt install
sudo apt upgrade

sudo apt install python3
sudo apt-get install python3-pip
```

### Step 2: Install Python libraries

```BASH
sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libx11-dev libatlas-base-dev
sudo apt-get install libgtk-3-dev libboost-python-dev
```

### Step 3: use Virtual Environment to install Python libraries

```BASH
python3.12 -m pip install virtualenv virtualenvwrapper

cd /mnt/c/data/Fotografie/PIC/groupimages
python3.12 -m venv myenv
source myenv/bin/activate
python3.12 -m pip install numpy scipy matplotlib scikit-image scikit-learn ipython
deactivate
```

### Step 4: Compile C++ binary

```BASH
git clone https://github.com/davisking/dlib
python3 setup.py install
```

