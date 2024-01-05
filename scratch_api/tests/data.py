import unittest

from . import tools

from ..nodes.NumberNode import NumberNode

from ..data.SetValueToBlock import SetValueToBlock
from ..data.ChangeValueByBlock import ChangeValueByBlock


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
