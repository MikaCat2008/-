import time
import unittest
import threading

from . import tools

from ..motion.ChangeXByBlock import ChangeXByBlock

from ..control.WaitBlock import WaitBlock

from scratch_api.control.RepeatBlock import RepeatBlock
from scratch_api.control.ForeverBlock import ForeverBlock

from scratch_api.control.IfThenBlock import IfThenBlock
from scratch_api.control.IfThenElseBlock import IfThenElseBlock
from scratch_api.control.WaitUntilBlock import WaitUntilBlock
from scratch_api.control.RepeatUntilBlock import RepeatUntilBlock


class ControlTestCase(unittest.TestCase):
    def test_wait_block(self) -> None:
        t1 = time.time()

        sprite = tools.sprite([
            WaitBlock(0.1),
            ChangeXByBlock(10)
        ])

        tools.update()

        self.assertEqual(sprite.coords[0], 10)
        self.assertAlmostEqual(round(time.time(), 1), round(t1 + 0.1, 1))

    def test_repeat_block(self) -> None:
        sprite1 = tools.sprite([
            RepeatBlock(3, [
                ChangeXByBlock(1)
            ])
        ])
        sprite2 = tools.sprite([
            RepeatBlock(1, [
                ChangeXByBlock(1)
            ])
        ])
        sprite3 = tools.sprite([
            RepeatBlock(0, [
                ChangeXByBlock(1)
            ])
        ])

        tools.update()

        self.assertEqual(sprite1.coords[0], 3)
        self.assertEqual(sprite2.coords[0], 1)
        self.assertEqual(sprite3.coords[0], 0)

    def test_forever_block(self) -> None:
        sprite = tools.sprite([ForeverBlock([])])

        t = threading.Thread(target=tools.update)
        t.start()

        time.sleep(0.1)

        self.assertTrue(t.is_alive)

        sprite.delete()
