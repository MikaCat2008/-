import unittest

from pygame.display import set_mode

from scratch_api import set_screen

from scratch_api.tests.nodes import NodesTestCase as t1
from scratch_api.tests.motion import MotionTestCase as t2
from scratch_api.tests.data import DataTestCase as t3
from scratch_api.tests.events import EventsTestCase as t4
from scratch_api.tests.control import ControlTestCase as t5
from scratch_api.tests.operators import OperatorsTestCase as t6

set_screen(set_mode((32, 32)))

if __name__ == "__main__":
    unittest.main()
