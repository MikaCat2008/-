import math
import unittest

from . import tools

from ..nodes.NumberNode import NumberNode

from ..motion.MoveBlock import MoveBlock
from ..motion.TurnRightBlock import TurnRightBlock
from ..motion.TurnLeftBlock import TurnLeftBlock


class MotionTestCase(unittest.TestCase):
    def test_move_block(self) -> None:
        sprite1 = tools.sprite(MoveBlock(NumberNode(10)))
        sprite2 = tools.sprite(MoveBlock(NumberNode(10)), direction = 90)
        sprite3 = tools.sprite(MoveBlock(NumberNode(10)), direction = 45)

        tools.update()

        self.assertAlmostEqual(sprite1.coords[0], 10)
        self.assertAlmostEqual(sprite2.coords[1], -10)
        self.assertAlmostEqual(sprite3.coords[0], math.cos(45 * math.pi / 180) * 10)
        self.assertAlmostEqual(sprite3.coords[1], -math.sin(45 * math.pi / 180) * 10)

    def test_turn_right_block(self) -> None:
        sprite1 = tools.sprite(TurnRightBlock(NumberNode(15)), direction = 0)
        sprite2 = tools.sprite(TurnRightBlock(NumberNode(30)), direction = 45)

        tools.update()

        self.assertEqual(sprite1.direction, -15)
        self.assertEqual(sprite2.direction, 15)

    def test_turn_left_block(self) -> None:
        sprite1 = tools.sprite(TurnLeftBlock(NumberNode(15)), direction = 0)
        sprite2 = tools.sprite(TurnLeftBlock(NumberNode(30)), direction = 45)

        tools.update()

        self.assertEqual(sprite1.direction, 15)
        self.assertEqual(sprite2.direction, 75)
