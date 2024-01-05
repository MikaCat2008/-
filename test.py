import unittest

from pygame.display import set_mode

from scratch_api import set_screen

from scratch_api.tests.motion import MotionTestCase as t1
from scratch_api.tests.control import ControlTestCase as t2
from scratch_api.tests.operators import OperatorsTestCase as t3

set_screen(set_mode((32, 32)))

if __name__ == "__main__":
    unittest.main()
