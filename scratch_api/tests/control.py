import time
import unittest
import threading

from . import tools

from ..objects import *


class ControlTestCase(unittest.TestCase):
    def test_wait_block(self) -> None:
        t1 = time.time()

        sprite = tools.sprite([
            WaitBlock(0.1),
            ChangeXByBlock(10)
        ])

        tools.update()

        self.assertEqual(sprite.coords[0], 10)
        self.assertGreater(time.time(), t1 + 0.1)

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

    def test_if_then_block(self) -> None:
        sprite1 = tools.sprite([
            IfThenBlock(True, [
                ChangeXByBlock(1)
            ])
        ])
        sprite2 = tools.sprite([
            IfThenBlock(False, [
                ChangeXByBlock(1)
            ])
        ])

        tools.update()

        self.assertEqual(sprite1.coords[0], 1)
        self.assertEqual(sprite2.coords[0], 0)

    def test_if_then_else_block(self) -> None:
        sprite1 = tools.sprite([
            IfThenElseBlock(True, [
                ChangeXByBlock(1)
            ], [
                ChangeXByBlock(2)
            ])
        ])
        sprite2 = tools.sprite([
            IfThenElseBlock(False, [
                ChangeXByBlock(1)
            ], [
                ChangeXByBlock(2)
            ])
        ])

        tools.update()

        self.assertEqual(sprite1.coords[0], 1)
        self.assertEqual(sprite2.coords[0], 2)

    def test_wait_until_block(self) -> None:
        t1 = time.time()

        sprite = tools.sprite([
            WaitUntilBlock(EqualsToNode(XPositionNode(), 10)),
            ChangeXByBlock(10)
        ], [
            WaitBlock(0.1),
            ChangeXByBlock(10)
        ])

        tools.update()

        self.assertEqual(sprite.coords[0], 20)
        self.assertGreater(time.time(), t1 + 0.1)

    def test_repeat_until_block(self) -> None:
        sprite = tools.sprite([
            RepeatUntilBlock(EqualsToNode(XPositionNode(), 20), [
                ChangeXByBlock(1)
            ])
        ])

        tools.update()

        self.assertEqual(sprite.coords[0], 20)
