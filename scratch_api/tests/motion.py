import math
import unittest

from . import tools

from ..motion.MoveBlock import MoveBlock
from ..motion.TurnRightBlock import TurnRightBlock
from ..motion.TurnLeftBlock import TurnLeftBlock

from ..motion.PointTowardsBlock import PointTowardsBlock

from ..motion.ChangeXByBlock import ChangeXByBlock
from ..motion.SetXToBlock import SetXToBlock
from ..motion.ChangeYByBlock import ChangeYByBlock
from ..motion.SetYToBlock import SetYToBlock

from ..motion.XPositionNode import XPositionNode
from ..motion.YPositionNode import YPositionNode
from ..motion.DirectionNode import DirectionNode


class MotionTestCase(unittest.TestCase):
    def test_move_block(self) -> None:
        sprite1 = tools.sprite([MoveBlock(10)])
        sprite2 = tools.sprite([MoveBlock(10)], direction = 90)
        sprite3 = tools.sprite([MoveBlock(10)], direction = 45)

        tools.update()

        self.assertAlmostEqual(sprite1.coords[0], 10)
        self.assertAlmostEqual(sprite2.coords[1], -10)
        self.assertAlmostEqual(sprite3.coords[0], math.cos(45 * math.pi / 180) * 10)
        self.assertAlmostEqual(sprite3.coords[1], -math.sin(45 * math.pi / 180) * 10)

    def test_turn_right_block(self) -> None:
        sprite1 = tools.sprite([TurnRightBlock(15)])
        sprite2 = tools.sprite([TurnRightBlock(30)], direction = 45)

        tools.update()

        self.assertEqual(sprite1.direction, 345)
        self.assertEqual(sprite2.direction, 15)

    def test_turn_left_block(self) -> None:
        sprite1 = tools.sprite([TurnLeftBlock(15)])
        sprite2 = tools.sprite([TurnLeftBlock(30)], direction = 45)

        tools.update()

        self.assertEqual(sprite1.direction, 15)
        self.assertEqual(sprite2.direction, 75)

    def test_point_towards_block(self) -> None:
        tools.sprite(x = 10, y = 0, name = "Sprite PointToward 1")
        tools.sprite(x = 10, y = 10, name = "Sprite PointToward 2")
        tools.sprite(x = 10, y = 20, name = "Sprite PointToward 3")

        sprite1 = tools.sprite([PointTowardsBlock("Sprite PointToward 1", False)])
        sprite2 = tools.sprite([PointTowardsBlock("Sprite PointToward 2", False)])
        sprite3 = tools.sprite([PointTowardsBlock("Sprite PointToward 3", False)])

        tools.update()

        self.assertAlmostEqual(sprite1.direction, 0)
        self.assertAlmostEqual(sprite2.direction, 315)
        self.assertAlmostEqual(sprite3.direction, math.atan(-2) * 180 / math.pi + 360)

    def test_change_x_by_block(self) -> None:
        sprite1 = tools.sprite([ChangeXByBlock(10)], x = 10)
        sprite2 = tools.sprite([ChangeXByBlock(-10)], x = 20)

        tools.update()

        self.assertEqual(sprite1.coords[0], 20)
        self.assertEqual(sprite2.coords[0], 10)

    def test_set_x_to_block(self) -> None:
        sprite1 = tools.sprite([SetXToBlock(10)])
        sprite2 = tools.sprite([SetXToBlock(-10)])

        tools.update()

        self.assertEqual(sprite1.coords[0], 10)
        self.assertEqual(sprite2.coords[0], -10)

    def test_change_y_by_block(self) -> None:
        sprite1 = tools.sprite([ChangeYByBlock(10)], y = 10)
        sprite2 = tools.sprite([ChangeYByBlock(-10)], y = 20)

        tools.update()

        self.assertEqual(sprite1.coords[1], 0)
        self.assertEqual(sprite2.coords[1], 30)

    def test_set_y_to_block(self) -> None:
        sprite1 = tools.sprite([SetYToBlock(10)])
        sprite2 = tools.sprite([SetYToBlock(-10)])

        tools.update()

        self.assertEqual(sprite1.coords[1], 10)
        self.assertEqual(sprite2.coords[1], -10)

    def test_x_position_node(self) -> None:
        sprite = tools.sprite(x = 30)
        node = XPositionNode()
        node.sprite = sprite

        self.assertEqual(node.get_value(), 30)

    def test_y_position_node(self) -> None:
        sprite = tools.sprite(y = 30)
        node = YPositionNode()
        node.sprite = sprite

        self.assertEqual(node.get_value(), 30)

    def test_direction_node(self) -> None:
        sprite = tools.sprite(direction = 30)
        node = DirectionNode()
        node.sprite = sprite

        self.assertEqual(node.get_value(), 30)
