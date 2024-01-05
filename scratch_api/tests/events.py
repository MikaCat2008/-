import unittest

from . import tools

from ..events.OnStartBlock import OnStartBlock
from ..events.OnKeyPressBlock import OnKeyPressBlock


class EventsTestCase(unittest.TestCase):
    def test_on_start_block(self) -> None:
        result1 = tools.test_listener_block(
            listener_block = OnStartBlock,
            event = "start"
        )
        result2 = tools.test_listener_block(
            listener_block = OnStartBlock,
            event = "update"
        )
        
        self.assertTrue(result1)
        self.assertFalse(result2)

    def test_on_key_press_block(self) -> None:
        result1 = tools.test_listener_block(
            listener_block = OnKeyPressBlock,
            event = "key",
            args = ("a", ),
            test_data = {
                "key": "a"
            }
        )
        result2 = tools.test_listener_block(
            listener_block = OnKeyPressBlock,
            event = "update",
            args = ("a", )
        )
        result3 = tools.test_listener_block(
            listener_block = OnKeyPressBlock,
            event = "key",
            args = ("a", ),
            test_data = {
                "key": "b"
            }
        )
        
        self.assertTrue(result1)
        self.assertFalse(result2)
        self.assertFalse(result3)
