import unittest
import re

from laserkittys_speech_bubble_generator import Shapes
from laserkittys_speech_bubble_generator.Shapes import *

PATH_PATTERN = "M\s(\d+[.]?\d*\s){2}((L|H|V|C|S|Q|T|A)\s(\d+[.]?\d*\s)+)+Z$"

class GetPreview(unittest.TestCase):

    def test_bubble_errors(self):
        for bType in Shapes.__all__:
            with self.assertRaises(ValueError):
                getattr(Shapes,bType).getPreview()

    def test_bubble_format(self):
        for bType in Shapes.__all__:
            getattr(Shapes,bType).setWidth(2*8)
            getattr(Shapes,bType).setHeight(2*3)
            getattr(Shapes,bType).setTailAnglePosition(0)
            getattr(Shapes,bType).setTailLength(10)
            getattr(Shapes,bType).setTailWidth(2)
            self.assertTrue(re.search(PATH_PATTERN,getattr(Shapes,bType).getPreview()) is not None)
            
            getattr(Shapes,bType).setWidth(2*273)
            getattr(Shapes,bType).setHeight(2*187)
            getattr(Shapes,bType).setTailAnglePosition(0)
            getattr(Shapes,bType).setTailLength(10)
            getattr(Shapes,bType).setTailWidth(2)
            self.assertTrue(re.search(PATH_PATTERN,getattr(Shapes,bType).getPreview()) is not None)

if __name__ == '__main__':
    unittest.main()