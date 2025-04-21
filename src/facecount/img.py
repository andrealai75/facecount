import sys
import json
import piexif
import piexif.helper
import logging
import face_recognition

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

class Img:
  def __init__(self, file_name):
    self.file_name = file_name
    self.current_comments = self.get_metadata_comments()
    if self.face_count_exists():
       self.face_count = int(self.current_comments['FaceCount'])
    else:
       self.face_count = 0

  def get_metadata_comments(self):
    try:
      exif_dict_exif = piexif.load(self.file_name)["Exif"]
      if piexif.ExifIFD.UserComment in exif_dict_exif:
        user_comment = piexif.helper.UserComment.load(exif_dict_exif[piexif.ExifIFD.UserComment])
        user_comment_json = json.loads(user_comment)
      else:
        user_comment_json = {}         
    except Exception as e:
        user_comment_json = {}
    return user_comment_json

  def face_count_exists(self):
    user_comment_json = self.current_comments
    if 'FaceCount' in user_comment_json.keys():
        return True
    return 

  def detect_faces(self):
    image = face_recognition.load_image_file(self.file_name)
    face_locations = face_recognition.face_locations(image)
    return len(face_locations)

  def update(self):
    self.current_comments['FaceCount'] = self.face_count
    exif_dict = piexif.load(self.file_name)
    exif_dict["Exif"][piexif.ExifIFD.UserComment] = piexif.helper.UserComment.dump(
     json.dumps(self.current_comments),
     encoding="unicode"
    )
    piexif.insert(piexif.dump(exif_dict), self.file_name)
