import unittest

from . import tools

from ..nodes import NumberNode

from ..data import SetValueToBlock
from ..data import ChangeValueByBlock


class DataTestCase(unittest.TestCase):
    def test_set_value_to_block(self) -> None:
        sprite = tools.sprite([
            SetValueToBlock("a", NumberNode(2))
        ], variables = {
            "a": 1
        })

        self.assertEqual(sprite.get_value("a"), 1)

        tools.update()

        self.assertEqual(sprite.get_value("a"), 2)
    
    def test_change_value_by_block(self) -> None:
        sprite = tools.sprite([
            ChangeValueByBlock("a", 2)
        ], variables = {
            "a": 1
        })

        self.assertEqual(sprite.get_value("a"), 1)

        tools.update()

        self.assertEqual(sprite.get_value("a"), 3)
