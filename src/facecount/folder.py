import os, sys

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from facecount.img import Img

class Folder:
  def __init__(self, path):
    self.path = path
    self.subfolders = []
    self.images = []

  def get_path(self) -> str:
    return self.path

  def name(self):
    return os.path.basename(self.path)

  def get_subfolders(self):
    return self.subfolders

  def get_images(self):
    return self.images

  def load_sub_folders(self):
    for item in os.listdir(self.path):
      full_path = self.path + item
      if os.path.isdir(full_path):
        self.subfolders.append(Folder(full_path))

  def load_images(self):
    for item in os.listdir(self.path):
      full_path = self.path + "/" + item
      if os.path.isfile(full_path) and os.path.splitext(full_path)[1].lower() == ".jpg":
        self.images.append(Img(full_path))

  def __str__(self) -> str:
    ret_val = self.path + ":\n"
    for image in self.images:
      ret_val = ret_val + " - " + str(image) + "\n"
    return ret_val

