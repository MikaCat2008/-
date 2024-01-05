import math
import unittest

from . import tools

from scratch_api.operators.AddNode import AddNode
from scratch_api.operators.SubNode import SubNode
from scratch_api.operators.MulNode import MulNode
from scratch_api.operators.DivNode import DivNode

from scratch_api.operators.RandomNumberNode import RandomNumberNode

from scratch_api.operators.LessThanNode import LessThanNode
from scratch_api.operators.EqualsToNode import EqualsToNode
from scratch_api.operators.BiggerThanNode import BiggerThanNode

from scratch_api.operators.AndNode import AndNode
from scratch_api.operators.OrNode import OrNode
from scratch_api.operators.NotNode import NotNode

from scratch_api.operators.MathFuncOfNode import MathFuncOfNode


class OperatorsTestCase(unittest.TestCase):
    def test_add_node(self) -> None:
        node1 = AddNode(1, 2)
        node2 = AddNode(1, AddNode(2, 1))

        self.assertEqual(node1.get_value(), 3)
        self.assertEqual(node2.get_value(), 4)

    def test_sub_node(self) -> None:
        node1 = SubNode(1, 2)
        node2 = SubNode(1, SubNode(2, 1))

        self.assertEqual(node1.get_value(), -1)
        self.assertEqual(node2.get_value(), 0)

    def test_mul_node(self) -> None:
        node1 = MulNode(1, 2)
        node2 = MulNode(1, MulNode(3, 1))

        self.assertEqual(node1.get_value(), 2)
        self.assertEqual(node2.get_value(), 3)

    def test_div_node(self) -> None:
        node1 = DivNode(1, 4)
        node2 = DivNode(1, DivNode(2, 1))

        self.assertEqual(node1.get_value(), 0.25)
        self.assertEqual(node2.get_value(), 0.5)

    def test_random_number_node(self) -> None:
        node1 = RandomNumberNode(1, 10)
        node2 = RandomNumberNode(-10, -1)
        node3 = RandomNumberNode(0, 1)

        self.assertIn(node1.get_value(), range(1, 11))
        self.assertIn(node2.get_value(), range(-10, -1))
        self.assertIn(node3.get_value(), range(2))

    def test_less_than_node(self) -> None:
        node1 = LessThanNode(1, 2)
        node2 = LessThanNode(2, 1)

        self.assertTrue(node1.get_value())
        self.assertFalse(node2.get_value())

    def test_equals_to_node(self) -> None:
        node1 = EqualsToNode(1, 1)
        node2 = EqualsToNode(1, 2)

        self.assertTrue(node1.get_value())
        self.assertFalse(node2.get_value())

    def test_bigger_than_node(self) -> None:
        node1 = BiggerThanNode(2, 1)
        node2 = BiggerThanNode(1, 2)

        self.assertTrue(node1.get_value())
        self.assertFalse(node2.get_value())

    def test_and_node(self) -> None:
        node1 = AndNode(True, True)
        node2 = AndNode(True, False)

        self.assertTrue(node1.get_value())
        self.assertFalse(node2.get_value()) 

    def test_or_node(self) -> None:
        node1 = OrNode(True, False)
        node2 = OrNode(False, False)

        self.assertTrue(node1.get_value())
        self.assertFalse(node2.get_value()) 

    def test_not_node(self) -> None:
        node1 = NotNode(False)
        node2 = NotNode(True)

        self.assertTrue(node1.get_value())
        self.assertFalse(node2.get_value()) 

    def test_math_func_of_node(self) -> None:
        node1 = MathFuncOfNode("sin", 45 * math.pi / 180)
        node2 = MathFuncOfNode("cos", 45 * math.pi / 180)

        self.assertAlmostEqual(node1.get_value(), math.sin(45 * math.pi / 180))
        self.assertAlmostEqual(node2.get_value(), math.cos(45 * math.pi / 180))
