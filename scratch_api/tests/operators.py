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
