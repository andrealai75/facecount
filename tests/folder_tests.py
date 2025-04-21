import os, sys

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..\\src')))

from facecount.folder import Folder

import unittest

class TestFolder(unittest.TestCase):
  def test_get_path(self):
    folder_1 = Folder('C:\\andrea\\lai')
    self.assertEqual(folder_1.get_path(), 'C:\\andrea\\lai', msg='{0}, {1}')

if __name__=='__main__':
	unittest.main()
