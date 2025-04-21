import os, sys
import logging
from datetime import date
import shutil
from pathlib import Path

logging.basicConfig(
  filename=str(date.today()) + '_facecount.log', 
  encoding='utf-8', level=logging.INFO)

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from facecount.folder import Folder
MAIN_PATH = "../tmp/Pics/"

def process_sub_folder(folder):
  folder.load_images()
  index = 0
  images = folder.get_images()
  for image in images:
    index += 1
    print(f"Processing image: {index}/{len(images)}")
    
    if image.face_count_exists():
      logging.info(f"{image.file_name} has already Face Count. Skipping!!")
    else:
      logging.info(f"{image.file_name} does not have the Face Count. Adding!!")
      try:
        image.face_count = image.detect_faces()
      except Exception as e:
        logging.info(f"Error: {image.file_name} - {str(e)}")
        image.face_count = 0
      image.update()

    if image.face_count >= 3:
      image_name = Path(image.file_name).name
      shutil.copy2(image.file_name, f"../group/{image_name}")

def facecount():
  logging.info("Executing Face Count Starting ...")
  main_folder = Folder(MAIN_PATH)
  main_folder.load_sub_folders()
  for sub_folder in main_folder.get_subfolders():
    process_sub_folder(sub_folder)
  logging.info("Executing Face Count Completed.")
